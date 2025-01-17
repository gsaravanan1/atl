import requests
import pandas as pd

# Step 1: Function to get event data for a specific venue from the SeatGeek API
def get_venue_events(venue_id):
    # SeatGeek API URL for events at a specific venue
    url = f"https://api.seatgeek.com/2/events"
    params = {
        "venue.id": venue_id,
        "client_id": "YOUR_CLIENT_ID",  # Replace with your actual SeatGeek client ID
        "per_page": 100,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['events']
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Step 2: Function to process event pricing data
def process_pricing_data(events):
    event_list = []
    
    for event in events:
        event_name = event['title']
        avg_price = event['stats']['average_price'] if 'average_price' in event['stats'] else 0
        ticket_count = event['stats']['listing_count'] if 'listing_count' in event['stats'] else 0
        total_revenue = avg_price * ticket_count
        
        event_list.append({
            'event_name': event_name,
            'avg_price': avg_price,
            'ticket_count': ticket_count,
            'total_revenue': total_revenue
        })
    
    df = pd.DataFrame(event_list)
    return df

# Step 3: Function to analyze pricing data
def analyze_pricing_data(df):
    # Calculate overall average ticket price
    avg_ticket_price = df['avg_price'].mean()
    
    # Calculate total revenue for all events
    total_revenue = df['total_revenue'].sum()
    
    return avg_ticket_price, total_revenue

# Main function to execute the process
def main():
    venue_id = 1234  # Replace with the actual SeatGeek venue ID
    print(f"Fetching events for venue ID: {venue_id}")
    
    # Step 1: Pull event data for the specific venue
    events = get_venue_events(venue_id)
    
    if events:
        # Step 2: Process the pricing data
        df = process_pricing_data(events)
        
        # Step 3: Analyze pricing data
        avg_ticket_price, total_revenue = analyze_pricing_data(df)
        
        print(f"\nAverage Ticket Price: ${avg_ticket_price:.2f}")
        print(f"Total Revenue for All Events: ${total_revenue:.2f}")
    else:
        print("No event data available for the selected venue.")

if __name__ == "__main__":
    main()
