"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#Part 1  -Get unique phone numbers in calls csv and text csv
import numpy as np

def unique_list(nestedlist):
    np_nestedlist = np.array(nestedlist)
    sending_telephones = list(np_nestedlist[:,0])
    receiving_telephones = list(np_nestedlist[:,1])
    return list(set(sending_telephones+receiving_telephones))


text_unique = unique_list(texts)
calls_unique = unique_list(calls)

#Part 2 - Compare calls and texts records and get unqiue number
finallist = list(set(text_unique+calls_unique))

#Part 3 - Print desired results
print ("There are "+ str(len(finallist))+" different telephone numbers in the records.")