import json

# Display File Names from JSON
aggregator = open("aggregator.txt","r+")
indices = aggregator.read().split("\n")[0]
index_dict = json.loads(indices)
for filename in index_dict:
    print(filename)
