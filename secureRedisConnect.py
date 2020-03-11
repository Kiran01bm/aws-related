import redis

r = redis.StrictRedis(
host='redis.dev.example.com',
port=6379,
password='redispassword',
ssl=True,
)

r.set('foo', 'bar')
response = r.get('foo')
print response
