from fastapi import FastAPI

app = FastAPI()


# Проверка кэша
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/health1")
async def health1():
    status = "ok"
    response = {"status": status}
    return response
