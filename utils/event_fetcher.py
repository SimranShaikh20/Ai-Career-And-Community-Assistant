# utils/event_fetcher.py
import requests
from datetime import datetime, timedelta
import pytz
from typing import List, Dict
import streamlit as st

class IndiaEventFetcher:
    def __init__(self):
        self.ist = pytz.timezone('Asia/Kolkata')
        
    @st.cache_data(ttl=3600, show_spinner="Fetching events...")
    def fetch_events(_self) -> List[Dict]:
        """Fetch tech events from Eventbrite API"""
        try:
            EVENTBRITE_TOKEN = st.secrets.get("EVENTBRITE_TOKEN", "BSAUF7QDHTGQXGRUKTD2")
            url = "https://www.eventbriteapi.com/v3/events/search/"
            headers = {"Authorization": f"Bearer {EVENTBRITE_TOKEN}"}
            
            params = {
                "q": "technology OR hackathon",
                "sort_by": "date",
                "location.address": "India",
                "start_date.keyword": "today",
                "expand": "venue,organizer",
                "categories": "102,108",
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return _self._process_events(response.json().get("events", []))
            
        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Error fetching events: {str(e)}")
            return []
    
    def _process_events(_self, events: List[Dict]) -> List[Dict]:
        """Process raw event data"""
        processed = []
        for event in events:
            try:
                start_utc = datetime.strptime(event['start']['utc'], "%Y-%m-%dT%H:%M:%S")
                end_utc = datetime.strptime(event['end']['utc'], "%Y-%m-%dT%H:%M:%S")
                start_ist = start_utc.replace(tzinfo=pytz.utc).astimezone(_self.ist)
                end_ist = end_utc.replace(tzinfo=pytz.utc).astimezone(_self.ist)
                
                processed.append({
                    'id': event['id'],
                    'name': event['name']['text'],
                    'description': event['description']['text'][:300] + '...' if event.get('description') else 'No description',
                    'start': start_ist,
                    'end': end_ist,
                    'venue': event.get('venue', {}).get('name', 'Online Event'),
                    'city': event.get('venue', {}).get('address', {}).get('city', 'Online'),
                    'url': event['url'],
                    'logo': event.get('logo', {}).get('original', {}).get('url'),
                    'is_free': event['is_free'],
                    'organizer': event.get('organizer', {}).get('name', 'Unknown organizer')
                })
            except Exception as e:
                continue
        return processed