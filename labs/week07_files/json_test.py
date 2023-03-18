# store a simple Dict to a file as JSON.

import json

FILENAME = "testdict.json"
sample = dict(name='Fred', age=31, grades = [1,3,4,55])

def write_dict(obj):
    with open (FILENAME, 'wt') as f:
        json.dump(obj,f)


# test the function
write_dict (sample)

