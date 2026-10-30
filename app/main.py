from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/readiness")
async def readiness_probe():
    status = "ready"
    response = {"status": status}
    return response
