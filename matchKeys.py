import redis
import sys

def find_keys_matching_pattern(redis_client, pattern):
    cursor = 0
    keys = []

    while True:
        cursor, partial_keys = redis_client.scan(cursor, match=pattern)
        keys.extend(partial_keys)

        # Check if the cursor is 0, indicating the end of the iteration
        if cursor == 0:
            break

    return keys

# Replace these values with your Redis server information
redis_host = 'dev-server-redis.35ox5r.ng.0001.usw2.cache.amazonaws.com'
redis_port = 6378
#redis_password = 'your_redis_password'

print("Arguments provided:",sys.argv[1])
pattern_to_match = str("*"+sys.argv[1]+"*")
redis_db = str(sys.argv[2])

# Replace 'bltf0b91991129a1644*' with your desired pattern
#pattern_to_match = 'bltf0b91991129a1644*'

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

# Find keys matching the pattern
matching_keys = find_keys_matching_pattern(redis_client, pattern_to_match)

# Print the matching keys
print("Total keys matching pattern:", len(matching_keys))

print("Keys matching the pattern '{}':".format(pattern_to_match))
for key in matching_keys:
    print(key)
