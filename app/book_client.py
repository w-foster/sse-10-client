from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
import requests
import os


app = FastAPI()


@app.get("/books", response_model=List[dict])
async def get_books(request: Request):
    url = os.getenv("books_api_url")  

    if not url:
        raise HTTPException(status_code=500, detail="books_api_url environment variable is not set")

    params = dict(request.query_params)

    response = requests.get(url, params=params)

    return response.json()


app.mount("/", StaticFiles(directory="static", html=True), name="static")