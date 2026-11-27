import psycopg2
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from testcontainers.community.postgres import PostgresContainer
from testcontainers.community.redis import RedisContainer

from app.visits import create_visits_router


@pytest.fixture()
def app_client():
    with PostgresContainer("postgres:16") as pg, RedisContainer("redis:7") as redis_c:
        conn = psycopg2.connect(
            pg.get_connection_url().replace(
                "postgresql+psycopg2",
                "postgresql",
            )
        )
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE visits (id SERIAL PRIMARY KEY, created_at TIMESTAMP)"
            )
            conn.commit()

        redis_url = (
            f"redis://{redis_c.get_container_host_ip()}"
            f":{redis_c.get_exposed_port(6379)}"
        )

        app = FastAPI()
        app.include_router(create_visits_router(conn, redis_url))
        yield TestClient(app)
        conn.close()
