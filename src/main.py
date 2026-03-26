import os
import redis
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv("REDIS_HOST", "localhost")
        self.port = int(os.getenv("REDIS_PORT", 6379))
        self.password = os.getenv("REDIS_PASSWORD")
        self.db = int(os.getenv("REDIS_DB", 0))
        self.ssl = os.getenv("REDIS_SSL", "False").lower() == "true"

    def get_connection(self) -> redis.Redis:
        return redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db,
            ssl=self.ssl,
            decode_responses=True
        )

def get_cached_value(key: str) -> Optional[str]:
    redis_config = RedisConfig()
    try:
        with redis_config.get_connection() as conn:
            return conn.get(key)
    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return None

def set_cached_value(key: str, value: str, ttl: int = 3600) -> bool:
    redis_config = RedisConfig()
    try:
        with redis_config.get_connection() as conn:
            conn.set(key, value, ex=ttl)
            return True
    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return False

if __name__ == "__main__":
    set_cached_value("test_key", "test_value")
    print(get_cached_value("test_key"))