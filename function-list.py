# bro, these defs so uselessss i can`t(((
def add_to_list(a):
	return a

def delete_from_list(a):
	return a

print("------Welcome to our list!------")
print("you can add or delete names, or clear list fully")

names = []

while True:
	name = input("print any name here: ")
	action = input("add, delete, clear or exit: ").lower
	if action == "add":
		names.append(add_to_list(name))
	elif action == "delete":
		names.pop(delete_from_list(name))
	elif action == "clear":
		names.clear
	elif action == "exit":
		print("Thank you for using my program!")
		break
	else:
		print("maybe you typed something wrong, try again")
		continue
else:
	print("what? why is True not Truing?")
print("ok, need another change")
<<<<<<< HEAD

print("i`m tired, bro")
=======
print("and another one...")
>>>>>>> aa062ea8d70a0f46a2691d89d6e2236a3c7a7f62
