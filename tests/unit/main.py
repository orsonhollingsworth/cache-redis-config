import os
import logging
from dotenv import load_dotenv
from redis import Redis

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
        self.REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
        self.REDIS_DB = int(os.getenv('REDIS_DB', 0))
        self.REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
        self.REDIS_TIMEOUT = int(os.getenv('REDIS_TIMEOUT', 60))

    def get_redis(self):
        return Redis(host=self.REDIS_HOST, 
                    port=self.REDIS_PORT, 
                    db=self.REDIS_DB, 
                    password=self.REDIS_PASSWORD, 
                    socket_timeout=self.REDIS_TIMEOUT)

def main():
    config = RedisConfig()
    redis_client = config.get_redis()

if __name__ == '__main__':
    main()