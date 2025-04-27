# utils/events_utils.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz
from typing import List, Dict, Optional
import streamlit as st
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IndiaEventManager:
    def __init__(self):
        self.sources = {
            "GDG India": "https://gdg.community.dev/india/",
            "Eventbrite Tech": "https://www.eventbrite.com/d/india--bangalore/technology/"
        }
        self.ist = pytz.timezone('Asia/Kolkata')
        self.registrations = []
        
        # Directly set your Eventbrite API key here
        self.EVENTBRITE_TOKEN = "SMIOEF4QM62K3KL2HN"  # ← Replace this with your actual key

    @st.cache_data(ttl=3600, show_spinner="Fetching events from all sources...")
    def fetch_events(_self) -> List[Dict]:
        """Fetch tech events from multiple sources"""
        all_events = []
        
        try:
            # GDG Events
            gdg_events = _self._fetch_gdg_events()
            all_events.extend(gdg_events)
            logger.info(f"Fetched {len(gdg_events)} GDG events")
            
            # Eventbrite Events (only if API key is set)
            if _self.EVENTBRITE_TOKEN and _self.EVENTBRITE_TOKEN != "YOUR_EVENTBRITE_API_KEY_HERE":
                eb_events = _self._fetch_eventbrite_events()
                all_events.extend(eb_events)
                logger.info(f"Fetched {len(eb_events)} Eventbrite events")
            else:
                logger.warning("Eventbrite API key not configured - skipping Eventbrite events")
                st.warning("Note: Eventbrite events not available (API key not configured)")
                
        except Exception as e:
            logger.error(f"Error fetching events: {e}")
            st.error("Failed to fetch some events. Showing partial results.")

        return sorted(all_events, key=lambda x: x['start'])

    def _fetch_eventbrite_events(_self) -> List[Dict]:
        """Fetch Eventbrite events using API"""
        try:
            url = "https://www.eventbriteapi.com/v3/events/search/"
            headers = {"Authorization": f"Bearer {_self.EVENTBRITE_TOKEN}"}
            
            params = {
                "location.address": "India",
                "categories": "102,108",  # Technology & Science categories
                "expand": "venue,organizer",
                "sort_by": "date",
                "start_date.range_start": datetime.now(_self.ist).strftime("%Y-%m-%dT%H:%M:%S"),
                "start_date.range_end": (datetime.now(_self.ist) + timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%S")
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
            
            events = []
            for event in response.json().get('events', []):
                try:
                    # Required fields
                    title = event['name']['text'].strip()
                    url = event.get('url', '').strip()
                    if not title or not url:
                        continue
                        
                    # Date handling
                    start_utc = datetime.strptime(event['start']['utc'], "%Y-%m-%dT%H:%M:%S")
                    end_utc = datetime.strptime(event['end']['utc'], "%Y-%m-%dT%H:%M:%S")
                    
                    # Venue handling
                    venue = event.get('venue', {})
                    location = venue.get('name', 'Online Event').strip()
                    city = venue.get('address', {}).get('city', 'Online').strip()
                    
                    events.append({
                        'title': title,
                        'start': start_utc.replace(tzinfo=pytz.utc).astimezone(_self.ist),
                        'end': end_utc.replace(tzinfo=pytz.utc).astimezone(_self.ist),
                        'location': location,
                        'city': city,
                        'source': 'Eventbrite',
                        'link': url,
                        'logo': event.get('logo', {}).get('url'),
                        'is_free': event.get('is_free', False),
                        'organizer': event.get('organizer', {}).get('name', 'Unknown').strip(),
                        'description': event.get('description', {}).get('text', '').strip()[:300] + '...'
                    })
                except Exception as e:
                    logger.warning(f"Error parsing Eventbrite event: {e}")
                    continue
                    
            return events
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Eventbrite API request failed: {e}")
            st.error("Failed to fetch Eventbrite events. Please check your API key and try again later.")
            return []
        except Exception as e:
            logger.error(f"Unexpected Eventbrite error: {e}")
            return []

    def _fetch_gdg_events(_self) -> List[Dict]:
        """Fetch events from GDG India website"""
        try:
            response = requests.get(_self.sources["GDG India"], timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            event_cards = soup.find_all('div', class_='event-card')
            
            events = []
            for card in event_cards:
                try:
                    # Extract basic info
                    title = card.find('h3').text.strip()
                    url = card.find('a')['href']
                    if not url.startswith('http'):
                        url = f"https://gdg.community.dev{url}"
                        
                    # Date parsing
                    date_str = card.find('div', class_='date').text.strip()
                    # Example format: "Saturday, October 15, 2022 · 10:00 AM IST"
                    date_part, time_part = date_str.split('·')
                    date_obj = datetime.strptime(date_part.strip(), "%A, %B %d, %Y")
                    time_obj = datetime.strptime(time_part.strip(), "%I:%M %p")
                    event_date = _self.ist.localize(datetime.combine(
                        date_obj.date(),
                        time_obj.time()
                    ))
                    
                    # Location
                    location_div = card.find('div', class_='location')
                    city = location_div.text.strip() if location_div else 'Online'
                    
                    events.append({
                        'title': title,
                        'start': event_date,
                        'end': event_date + timedelta(hours=2),  # Default 2-hour duration
                        'location': city,
                        'city': city,
                        'source': "GDG India",
                        'link': url,
                        'logo': card.find('img')['src'] if card.find('img') else None,
                        'is_free': True,  # GDG events are typically free
                        'organizer': "Google Developer Groups",
                        'description': card.find('p', class_='description').text.strip()[:300] + '...' if card.find('p', class_='description') else ''
                    })
                except Exception as e:
                    logger.warning(f"Error parsing GDG event: {e}")
                    continue
                    
            return events
            
        except requests.exceptions.RequestException as e:
            logger.error(f"GDG website request failed: {e}")
            st.error("Failed to fetch GDG events. Please try again later.")
            return []
        except Exception as e:
            logger.error(f"Unexpected GDG error: {e}")
            return []

    def register(_self, event: Dict, user_data: Dict) -> Dict:
        """Handle event registration"""
        try:
            registration = {
                'event': event['title'],
                'date': event['start'].strftime("%Y-%m-%d"),
                'location': event['location'],
                'source': event.get('source', 'Unknown'),
                **user_data,
                'timestamp': datetime.now(_self.ist).strftime("%Y-%m-%d %H:%M")
            }
            _self.registrations.append(registration)
            return registration
        except Exception as e:
            logger.error(f"Registration failed: {e}")
            raise

    def get_registrations(_self) -> List[Dict]:
        """Get all registrations"""
        return _self.registrations

    def filter_events(_self, events: List[Dict], filters: Dict) -> List[Dict]:
        """Filter events based on user criteria"""
        filtered = []
        today = datetime.now(_self.ist)
        
        for event in events:
            try:
                # Time filter
                time_frame = filters.get('time_frame', "This Week")
                if time_frame == "Today" and event['start'].date() != today.date():
                    continue
                elif time_frame == "This Week" and event['start'].date() > (today + timedelta(days=7)).date():
                    continue
                elif time_frame == "Next 30 Days" and event['start'].date() > (today + timedelta(days=30)).date():
                    continue
                
                # Type filter
                event_type = filters.get('event_type', "All")
                if (event_type != "All" and 
                    event_type.lower() not in event.get('title', '').lower()):
                    continue
                
                # Location filter
                cities = filters.get('cities', ["Bangalore", "Online"])
                if (cities and 
                    event.get('city') not in cities and 
                    'Online' not in cities):
                    continue
                
                filtered.append(event)
            except Exception as e:
                logger.warning(f"Error filtering event: {e}")
                continue
                
        return sorted(filtered, key=lambda x: x['start'])