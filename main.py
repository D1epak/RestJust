from fastapi import FastAPI

from utils import open_ai

app = FastAPI()


@app.get("/test/{data}")
async def root(data):
    try:
        response = open_ai(data)
        return response
    except Exception as error:
        print(error)
        return {"status": 500, "message": "Incorrect API key provided: YOUR_API_KEY."}
