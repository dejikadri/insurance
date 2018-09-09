import redis
# r = redis.Redis(host='172.18.0.2', port=6379, db=0)
# r.set('name', 'Deji')
# print(r.get('name'))


client = redis.StrictRedis(host='172.17.0.3', port=6379, db=0)

client.set("key01", "value01")
print(client.get("key01"))