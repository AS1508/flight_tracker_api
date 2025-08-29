from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from apps.service import get_flight_data_by_callsign

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")
router = APIRouter()

def fake_decode_token(token):
  if token != "example_token":
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")
  return {"sub": "user_id"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
  return fake_decode_token(token)

@router.get("/flights/{callsign}")
async def flight_by_callsign(callsign: str, user: dict = Depends(get_current_user)):
    flight_data = get_flight_data_by_callsign(callsign)
    if flight_data is None:
        raise HTTPException(status_code=404, detail=f"Flight with callsign {callsign} not found")
    return flight_data