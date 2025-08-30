import requests

URL_BASE = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"

def get_token(client_id: str, client_secret: str):
  try:
    url = f"{URL_BASE}"
    response = requests.post(url, data={
      "client_id": client_id,
      "client_secret": client_secret,
      "grant_type": "client_credentials"
    })
    print(response.json())
    if response.status_code == 200:
      return response.json()
    else:
      return {"error": "Failed to get token"}
  except requests.RequestException as e:
    print(f"Error in contact with OS API: {e}")
    return {"error": "Failed to get token"}


