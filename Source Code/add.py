import sys
import json
import os

if len(sys.argv) != 2:
	print("One Argument should be passed")
	exit()

filename = sys.argv[1]

# Create aggregator if not present
if not os.path.isfile('aggregator.txt'):
	aggregator = open("aggregator.txt","w")
	aggregator.write('{}')
	aggregator.close()


# Open the file to be appended
addedfile = open(filename,"r" )
addedcontent = addedfile.read()
filelength = addedcontent.split("\n")
filelength = len(filelength)
addedfile.close()

# Open the aggregator
aggregator = open("aggregator.txt","r")
aggcontent = aggregator.read().split("\n")
aggregator.close()
filestart = len(aggcontent)

# Update indices
indices = aggcontent.pop(0)
index_dict = json.loads(indices)
index_dict[filename] = json.loads('{ "start" : '+str(filestart)+', "length" : '+str(filelength)+' }')
indices = json.dumps(index_dict)

# Write to aggregator.txt
aggregator = open("aggregator.txt","w+")
aggregator.write(indices)
for line in aggcontent:
	aggregator.write('\n'+line)
aggregator.write('\n'+addedcontent)
aggregator.close()

# Delete file
os.remove(filename)
