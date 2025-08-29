from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

def fake_decode_token(token):
    if token != "example_token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"sub": "user_id"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return fake_decode_token(token)

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "usuario" or form_data.password != "contraseña":
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos",
        )
    return {"access_token": "example_token", "token_type": "bearer"}
