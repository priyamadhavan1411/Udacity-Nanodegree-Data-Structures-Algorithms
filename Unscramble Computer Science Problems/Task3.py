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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140."""
def codeslist(lists_calls):
    codescalled=[]
    for record in lists_calls:
        if record[0].startswith('(080)'):
            code = (record[1]).strip('(').replace(')'," ").split(" ")
            codescalled.append(code[0])
    return codescalled

def shorten(list_value):
    uniquecodes_final = []
    for code in list_value:
        if len(code)>4:
            code_new = code[:-1]
            uniquecodes_final.append(code_new)
        else:
            uniquecodes_final.append(code)
    return uniquecodes_final


list_codes = codeslist(calls)
uniquecodes = sorted(list(set(list_codes)))
print(len(uniquecodes))
    
uniquecodes_final = sorted(list(set(shorten(uniquecodes))))
print ('\n'.join([ str(codes) for codes in uniquecodes_final]))

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_percentage(nestedlist, string_value_code):
    count=0
    for record in nestedlist:
        if record[0].startswith(string_value_code) and record[1].startswith(string_value_code):
            count +=1
    percentage = count/len(list_codes)
    formated = ('{0:.2f}'.format(percentage))
    return formated 


formated = get_percentage(calls,'(080)')
print(formated + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")