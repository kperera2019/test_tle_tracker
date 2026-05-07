import asyncio
import json

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()

ISS_API_URL = "https://api.wheretheiss.at/v1/satellites/25544"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/iss-location")
async def iss_location():
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(ISS_API_URL)
            response.raise_for_status()
            data = response.json()

        return {
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "altitude": data.get("altitude"),
            "velocity": data.get("velocity"),
            "timestamp": data.get("timestamp"),
        }

    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=f"ISS API request failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(status_code=502, detail="ISS API returned non-JSON data") from exc


@app.get("/iss-stream")
async def iss_stream():
    async def event_generator():
        async with httpx.AsyncClient(timeout=10) as client:
            while True:
                try:
                    response = await client.get(ISS_API_URL)
                    response.raise_for_status()
                    data = response.json()

                    payload = {
                        "latitude": data.get("latitude"),
                        "longitude": data.get("longitude"),
                        "altitude": data.get("altitude"),
                        "velocity": data.get("velocity"),
                        "timestamp": data.get("timestamp"),
                    }

                    yield f"data: {json.dumps(payload)}\n\n"

                except Exception as exc:
                    yield f"event: error\ndata: {json.dumps({'error': str(exc)})}\n\n"

                await asyncio.sleep(2)

    return StreamingResponse(event_generator(), media_type="text/event-stream")