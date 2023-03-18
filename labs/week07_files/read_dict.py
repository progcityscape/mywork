# Write a function that will read in a dict object from file
import json
FILENAME = "testdict.json"

def read_dict ():
    with open (FILENAME) as f:
        return json.load(f)

# test the function
somedict = read_dict ()
print (somedict)