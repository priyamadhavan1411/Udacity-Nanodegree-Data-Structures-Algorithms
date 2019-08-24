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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def gettelenumbers(list_values,string_value):
    tele = []
    for record in list_values:
        if record[0].startswith(string_value):
            tele.append(record[0])
    uniquetele = sorted(list(set(tele)))
    return uniquetele   

uniquetelenumbers = gettelenumbers(calls,'140')
print("These numbers could be telemarketers: ")
print ('\n'.join([ str(codes) for codes in uniquetelenumbers]))

