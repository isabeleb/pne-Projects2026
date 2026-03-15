from Client3 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("127.0.0.1", 8080)

print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")


#PING COMMAND
print("* Testing PING...")

print(c.talk("PING"))


#GET COMMAND
print("* Testing GET...")
get_tests = {'get_0': c.talk("GET 0").replace("\n", ""), 'get_1': c.talk("GET 1").replace("\n", ""),
             'get_2': c.talk("GET 2").replace("\n", ""),'get_3': c.talk("GET 3").replace("\n", ""),
             'get_4' : c.talk("GET 4")}

for test_num, seq in get_tests.items():
    print(f"GET {test_num.replace('get_', '')} : {seq}")


#INFO COMMAND
print("* Testing INFO...")
seq = c.talk("GET 0")
info_test = c.talk(f"INFO {seq}")

print(info_test)


#COMP COMMAND
print("* Testing COMP...")
comp_test = c.talk(f"COMP {seq}")

print("COMP" , seq.replace('\n', ''))
print(f"{comp_test}")


#REV COMMAND
print("* Testing REV...")
rev_test = c.talk(f"REV {seq}")

print("REV" , seq.replace('\n', ''))
print(f"{rev_test}")

#GENE COMMAND
print("* Testing GENE...")

print("GENE U5:")
print(c.talk("GENE U5"))
print(" ")
print("GENE ADA:")
print(c.talk("GENE ADA"))
print(" ")
print("GENE FRAT1:")
print(c.talk("GENE FRAT1"))
print(" ")
print("GENE FXN:")
print(c.talk("GENE FXN"))
print(" ")
print("GENE RNU6_269P:")
print(c.talk("GENE RNU6_269P"))


