import sys
import json
import os

if len(sys.argv) != 2:
	print("One Argument should be passed")
	exit()

filename = sys.argv[1]
cutfilename = 'cut_'+filename

# Remove file from Aggregation
aggregator = open("aggregator.txt","r")
aggcontent = aggregator.read().split("\n")
aggregator.close()

# Fetch indices
indices = aggcontent[0]
index_dict = json.loads(indices)
filestart = index_dict[filename]['start']
filelength = index_dict[filename]['length']

# Update Indices - Delete and Update the others
del index_dict[filename]
for key in index_dict:
    if index_dict[key]['start'] > filestart:
        index_dict[key]['start'] = index_dict[key]['start'] - filelength

# Update Json
indices = json.dumps(index_dict)
aggcontent[0] = indices

# Create cut_file
cutfile = open(cutfilename,"w")


# Prepare Cutfile
cutfilecontent = aggcontent[slice(filestart,filestart+filelength,1)]
for line in cutfilecontent:
    cutfile.write(line+"\n")
cutfile.close()

del aggcontent[slice(filestart,filestart+filelength,1)]

# Update aggregator
aggregator = open("aggregator.txt","w")
for line in aggcontent:
    aggregator.write(line+"\n")
aggregator.close()
