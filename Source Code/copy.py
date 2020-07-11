import sys
import json

if len(sys.argv) != 2:
	print("One Argument should be passed")
	exit()

filename = sys.argv[1]
copyfilename = 'copy_'+filename

# Fetch lines from aggregator
aggregator = open("aggregator.txt","r")
aggcontent = aggregator.read().split("\n")
aggregator.close()

# Fetch indices from json
indices = aggcontent[0]
index_dict = json.loads(indices)
filestart = index_dict[filename]['start']
filelength = index_dict[filename]['length']

# Create copy_file
copiedfile = open(copyfilename,"w")
for index in range(filestart,filestart+filelength):
    copiedfile.write(aggcontent[index]+"\n")
copiedfile.close()
