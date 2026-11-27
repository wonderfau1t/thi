import redis as redis_lib
from fastapi import APIRouter


def create_visits_router(db_conn, redis_url):
    router = APIRouter()
    r = redis_lib.from_url(redis_url)

    @router.get("/visits")
    def visits():
        cached = r.get("visits_count")
        if cached:
            return {"count": int(cached), "source": "cache"}

        with db_conn.cursor() as cur:
            cur.execute("INSERT INTO visits (created_at) VALUES (NOW()) RETURNING id")
            new_id = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM visits")
            count = cur.fetchone()[0]
            db_conn.commit()

        r.set("visits_count", count, ex=10)
        return {"count": count, "source": "db", "lastId": new_id}

    return router
