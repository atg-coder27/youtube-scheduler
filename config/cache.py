import redis
import json
from django.conf import settings
import os



class RedisHash():
    def __init__(self) -> None:
        self.redisClient = redis.StrictRedis(
            host = "redis",
            port = "6379",
            db = 0,
            password= "redis"
        )
    
    def add_to_hash(self,hash_key,key,value):
        self.redisClient.hset(hash_key,key,value)
    
    def get_all_key_values(self,hash_key):
        return self.redisClient.hgetall(hash_key)
    
    def get_value(self,hash_key,key):
        return self.redisClient.hget(hash_key,key)
    
    def get_all_values(self,hash_key):
        return self.redisClient.hvals(hash_key)
    
    def delete_set(self,hash_key):
        self.redisClient.delete(hash_key)


# RedisHash().add_to_hash("TAGS","football",json.dumps(1))
# RedisHash().add_to_hash("TAGS","foot",json.dumps(2))
# print(json.loads(RedisHash().get_value("TAGS","football")))
