# -*- coding: utf-8 -*-

def clearspace():
    print('\n' *3)

clearspace()

print("*** A poor man's Eliza program to help you! ***")
print("         (Input 'stop' to terminate)")

answer = input("You have a problem with someone? Tell me: ")

Family = ["Mum","mum","Dad","dad"]

while True:
    words = answer.split(" ")
    if len(words) == 1 and words[0] == "stop":
        print("Goodbye!")
        break

    family_len=len(Family)
    for i in range(0, family_len):
           if(Family[i] in words):
                answer=input("Tell me more about your family: ")
                break
    else:
        answer=input("I do not understand! What problem you have with whom? Tell me: ")

# your code
# your code
# your code
# your code
# your code
# your code
