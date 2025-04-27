# pages/events.py
from typing import Dict, List
import streamlit as st
from utils.event_fetcher import IndiaEventFetcher
from datetime import datetime, timedelta
import logging

# Initialize fetcher
fetcher = IndiaEventFetcher()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def display_event_card(event: Dict):
    """Display an event card with consistent styling"""
    try:
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.image(event.get('logo', "https://via.placeholder.com/150"), width=150)
            
            with col2:
                badge = "🟢 FREE" if event.get('is_free', False) else "🔵 PAID"
                st.markdown(f"""
                **{event.get('name', 'Unnamed Event')}** {badge}  
                📅 {event['start'].strftime('%a, %d %b %Y %I:%M %p') if 'start' in event else 'Date not available'} IST  
                📍 {event.get('venue', 'Venue not specified')} ({event.get('city', 'Location not specified')})  
                👤 {event.get('organizer', 'Organizer not specified')}  
                {event.get('description', 'No description available')}  
                [🔗 Register/More Info]({event.get('url', '#')})  
                """)
                st.markdown("---")
    except Exception as e:
        logger.error(f"Error displaying event card: {e}")
        st.error(f"Error displaying event: {str(e)}")

def apply_filters(events: List[Dict], filters: Dict) -> List[Dict]:
    """Apply filters to events"""
    filtered_events = []
    today = datetime.now(fetcher.ist)
    
    for event in events:
        try:
            # Time filter
            time_frame = filters.get('time_frame', "This Week")
            event_date = event.get('start')
            
            if not isinstance(event_date, datetime):
                logger.warning(f"Invalid date format for event: {event.get('name')}")
                continue
                
            if time_frame == "Today" and event_date.date() != today.date():
                continue
            elif time_frame == "This Week" and event_date.date() > (today + timedelta(days=7)).date():
                continue
            elif time_frame == "Next 7 Days" and event_date.date() > (today + timedelta(days=7)).date():
                continue
            elif time_frame == "Next 30 Days" and event_date.date() > (today + timedelta(days=30)).date():
                continue
            
            # Type filter
            event_type = filters.get('event_type', "All")
            if event_type != "All" and event_type.lower() not in event.get('name', '').lower():
                continue
            
            # Location filter
            cities = filters.get('cities', ["Bangalore", "Online"])
            if cities and event.get('city') not in cities and 'Online' not in cities:
                continue
            
            filtered_events.append(event)
        except Exception as e:
            logger.error(f"Error filtering event {event.get('name')}: {e}")
            continue
            
    return filtered_events

def events_page():
    """Main events page function called from main.py"""
    st.title("🇮🇳 Tech Events Across India")
    
    # Initialize filters in session state
    if 'event_filters' not in st.session_state:
        st.session_state.event_filters = {
            'time_frame': "This Week",
            'event_type': "All",
            'cities': ["Bangalore", "Online"]
        }
    
    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filters")
        st.session_state.event_filters['time_frame'] = st.selectbox(
            "Time Frame",
            ["Today", "This Week", "Next 7 Days", "Next 30 Days"],
            index=1
        )
        st.session_state.event_filters['event_type'] = st.selectbox(
            "Event Type",
            ["All", "Hackathon", "Conference", "Workshop", "Meetup"],
            index=0
        )
        st.session_state.event_filters['cities'] = st.multiselect(
            "Cities",
            ["Bangalore", "Delhi", "Mumbai", "Hyderabad", "Pune", "Chennai", "Online"],
            default=["Bangalore", "Online"]
        )
    
    # Fetch and display events
    try:
        with st.spinner("Loading events..."):
            events = fetcher.fetch_events()
            logger.info(f"Fetched {len(events) if events else 0} events")
            
            if not events:
                st.warning("No events found. Try adjusting filters or check back later.")
                return
            
            # Apply filters
            filtered_events = apply_filters(events, st.session_state.event_filters)
            logger.info(f"Filtered down to {len(filtered_events)} events")
            
            # Display results
            st.subheader(f"🎯 Found {len(filtered_events)} events")
            
            if not filtered_events:
                st.info("No events match your filters. Try adjusting criteria.")
                return
            
            for event in sorted(filtered_events, key=lambda x: x.get('start', datetime.max)):
                display_event_card(event)
                
    except Exception as e:
        logger.error(f"Error in events page: {e}")
        st.error("Failed to load events. Please try again later.")