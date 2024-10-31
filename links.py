from fastapi import FastAPI, HTTPException
from typing import Dict
import string
import random

app = FastAPI()
url_storage: Dict[str, str] = {}


class URLShortener:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits
        self.short_length = 6

    def generate_short_url(self, original_url: str) -> str:
        while True:
            short = ''.join(random.choices(self.alphabet, k=self.short_length))
            if short not in url_storage:
                url_storage[short] = original_url
                return short

    def get_original_url(self, short_url: str) -> str:
        return url_storage.get(short_url)


url_shortener = URLShortener()


@app.post("/shorten")
async def shorten_url(original_url: str):
    short = url_shortener.generate_short_url(original_url)
    return {"shortened_url": f"http://localhost:8000/{short}"}


@app.get("/{short_url}")
async def redirect_to_original(short_url: str):
    original_url = url_shortener.get_original_url(short_url)
    if original_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": original_url}
