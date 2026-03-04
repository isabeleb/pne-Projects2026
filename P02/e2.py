from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


c = Client("212.128.255.65", 8081)

IP, PORT = c._str_()

print("Connection to SERVER at", IP, ",PORT:" , PORT)





