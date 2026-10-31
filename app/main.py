from fastapi import FastAPI

app = FastAPI()


# Проверка кэша
@app.get("/health")
async def health():
    return {"status": "ok"}
