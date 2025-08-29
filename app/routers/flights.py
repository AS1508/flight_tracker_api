from fastapi import APIRouter, HTTPException
from .. import schemas, services

router = APIRouter(
  prefix="/flights",
  tags=["flights"]
)

@router.get("/{callsign}", response_model=schemas.FlightState)
def get_flight_by_callsign(callsign: str):
  flight_data = services.get_flight_by_callsign(callsign)
  if not flight_data or "error" in flight_data:
    raise HTTPException(status_code=404, detail="Flight with callsign {callsign} not found / Data source error")
  return flight_data