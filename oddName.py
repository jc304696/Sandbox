""" This is for a git commit process
    author __Lyle Martin__"""

prompt = "Enter your name below"
print(prompt)
name = input(">>> ")
if len(name) == 0 :
    print('invalid name please try again')
    name = input(">>> ")

NewName = ""
for LoopNumber in range(0,len(name),2):
    NewName += name[LoopNumber+1]
print(NewName)
