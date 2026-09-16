#To_do_list
file = open("todo.txt", "a", encoding="utf-8")
file.write("MY TO DO LIST\n")
file.close()

#to do input
while True:
    task=input("do you want to add a task? (y/n): ")
    if task == "y":
        task=input("enter your task: ")
        file = open("todo.txt", "a", encoding="utf-8")
        file.write(task + "\n")
        file.close()
    else:
        print("Thank you for using the To-Do program")
        break   
