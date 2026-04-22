# from voice import listen, speak
# from commands import execute_command

# speak("Assistant is ready. Say 'hey assistant' to start")

# while True:
#     command = listen()

#     if "hey assistant" in command:
#         speak("Yes, I am listening")

#         command = listen()

#         if command == "":
#             speak("I didn't catch that")
#             continue

#         print("Executing command:", command)

#         if not execute_command(command):
#             break
from voice import listen, speak
from commands import execute_command

speak("Hello, I am your slave")

while True:
    command = listen()

    if command == "":
        continue

    print("Command:", command)

    if not execute_command(command):
        break