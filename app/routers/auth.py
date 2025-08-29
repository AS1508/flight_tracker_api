from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from ..auth_service import get_token

router = APIRouter(tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

def fake_decode_token(token):
    if token != "example_token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"sub": "user_id"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return fake_decode_token(token)

class ClientCredentialsForm(BaseModel):
    client_id: str
    client_secret: str

def client_credentials_form(
    client_id: str = Form(...),
    client_secret: str = Form(...),
):
    return ClientCredentialsForm(client_id=client_id, client_secret=client_secret)

@router.post("/token")
async def login(form_data: ClientCredentialsForm = Depends(client_credentials_form)):
    if not form_data.client_id or not form_data.client_secret:
        raise HTTPException(
            status_code=401,
            detail="Client ID or Client Secret incorrect",
        )
    return get_token(form_data.client_id, form_data.client_secret)
