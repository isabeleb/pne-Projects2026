import json
import termcolor
from pathlib import Path

jsonstring = Path("people-e1.json").read_text()

users = json.loads(jsonstring)

for user  in users['people']:
    f_name = user["Firstname"]
    l_name = user["Lastname"]
    Age = user["age"]
    Phone_nums = user["phoneNumber"]

    termcolor.cprint("Name:", "green",  end="")
    print(f_name, l_name)

    termcolor.cprint("Age:", "green", end="")
    print(Age)

    termcolor.cprint("Phone numbers: " , "green", end="")
    print(len(Phone_nums))

    for i, phone in enumerate(Phone_nums):
        termcolor.cprint(f"  Phone {i}:", "green")

        termcolor.cprint(f"    Type:", "red", end="")
        print(phone["type"])

        termcolor.cprint(f"     Number:", "red", end="")
        print(phone["number"])

