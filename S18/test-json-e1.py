import json
import termcolor
from pathlib import Path


jsonstring = Path("people-e1.json").read_text()

person = json.loads(jsonstring)

FirstNames = person['Firstname']
LastNames = person['Lastname']
Ages = person['age']


print("Total people on the database:" , len(FirstNames))

termcolor.cprint("Name:" , 'green') , print(FirstNames[0])

print()

#FirstNames = person['Firstname']
#LastNames = person['Lastname']
#Ages = person['age']

#for i, dict_firstname in enumerate(FirstNames):
    #termcolor.cprint("Name" , 'green')
    #print(dict_firstname)

#print(person['Firstname'], person['Lastname'])

#termcolor.cprint("Age: ", 'green', end="")
#print(person['age'])


#phoneNumbers = person['phoneNumber']


#termcolor.cprint("Phone numbers: ", 'green', end='')
#print(len(phoneNumbers))


#for i, dictnum in enumerate(phoneNumbers):
    #termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    # The element num contains 2 fields: number and type
    #termcolor.cprint("\t- Type: ", 'red', end='')
    #print(dictnum['type'])
    #termcolor.cprint("\t- Number: ", 'red', end='')
    #print(dictnum['number'])
