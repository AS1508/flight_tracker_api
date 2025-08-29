from pydantic import BaseModel as bm
from typing import Optional

class FlightState(bm):
  icao24: str
  callsign: str
  origin_country: str
  longitude: Optional[float]
  latitude: Optional[float]
  altitude: Optional[float]
  on_ground: bool
  velocity: Optional[float] #m/s
  heading: Optional[float] #degrees
  vertical_speed: Optional[float]