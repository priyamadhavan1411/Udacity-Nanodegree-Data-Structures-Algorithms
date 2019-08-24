"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import numpy as np


#Part 1 - Find max duration
def get_maxdurationnumber(list_input):
    list_input_array = np.array(list_input)
    maxv = max(list_input_array[:,3])
#Part 2 - return required results using obtained max duration spent
    for record in list_input:
        if record[3] == maxv:
            telephonenumber,duration = record[0],record[3]
            return telephonenumber,duration
        else:
            continue
            
#Part 3 - call function and print required results
telephonenumber, duration =  get_maxdurationnumber(calls)  
print(telephonenumber +" spent the longest time, "+ duration +" seconds, on the phone during September 2016.")
