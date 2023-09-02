from fastapi import FastAPI

app = FastAPI()


@app.get("/test/")
async def root(data):
    print(data)
    return {"message": "Hello World"}
