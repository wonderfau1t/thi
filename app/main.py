from fastapi import FastAPI

app = FastAPI()


# Проверка кэша
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/test")
async def test():
    status = "ready"
    response = {"status": status}
    return response
