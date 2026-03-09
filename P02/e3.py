from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("127.0.0.1", 8081)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
