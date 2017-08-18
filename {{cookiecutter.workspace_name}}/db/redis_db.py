# -*- coding:utf8 -*-

import redis
import platform


DEBUGGING = True if 'local' in platform.node().lower() else False

if DEBUGGING:
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = None
else:
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = ''


class RedisManager():
    redis_conn = None

    @classmethod
    def get_redis(cls,
                  host=REDIS_HOST,
                  port=REDIS_PORT,
                  db=REDIS_DB,
                  password=REDIS_PASSWORD,
                  charset='utf-8',
                  decode_responses=True):
        if not cls.redis_conn:
            redis_conn = redis.StrictRedis(
                    host=host,
                    port=port,
                    db=db,
                    password=password,
                    charset=charset,
                    decode_responses=decode_responses
                )
        return redis_conn


if __name__ == '__main__':
    redis_connection = RedisManager.get_redis()
    redis_connection.rpush('a', 'b', 'f')
    print(redis_connection.exists('a'))
    pass