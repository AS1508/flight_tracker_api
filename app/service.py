import requests
import os

URL_BASE = "https://opensky-network.org/api/"
def get_flight_data_by_callsign(callsign: str):
  try:
    url = f"{URL_BASE}/states/all"
    
    response = requests.get(url)
    if response.status_code == 200:
      response.raise_for_status() #If the petition fails
    
    all_flights = response.json().get('states', [])
    
    #Callsign clear
    for flight in all_flights:
      if flight[1].strip() == callsign.upper():
        #format
        return {
          "icao24": flight[0],
          "callsign": flight[1].strip(),
          "origin_country": flight[2],
          "longitude": flight[5],
          "latitude": flight[6],
          "altitude": flight[7],
          "on_ground": flight[8],
          "velocity_mps": flight[9],
          "heading_grades": flight[10],
          "vertical_rate_mps" : flight[11]
        }

    return None #if don't see the flight
  except requests.RequestException as e:
    print(f"Error in contact with OS API: {e}")
    return {"error": "information not found"}
  