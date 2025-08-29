# Flight Tracker API

API para consultar información de vuelos usando OpenSky Network.

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

4. Copia `.env.example` a `.env` y completa tus variables.

## Uso

Levanta el servidor con:

```
uvicorn app.main:app --reload
```

Abre [http://localhost:8000/docs](http://localhost:8000/docs) para ver la documentación interactiva.

## Endpoints principales

- `POST /api/token` — Obtener token de autenticación
- `GET /api/flights/{callsign}` — Consultar vuelo (requiere token)

## Autenticación

1. Usa `/api/token` con usuario `usuario` y contraseña `contraseña` para obtener un token.
2. Usa ese token como `Bearer` en los endpoints protegidos.

---