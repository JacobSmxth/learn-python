from todo import Task,  TaskManager

def display_menu():
    zeroTask = True
    if tm.taskCount() < 1:
        print("1. Add Task")
        print("2. Exit Program")
    else:
        zeroTask = False
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Clear Tasks")
        print("6. Exit Program")

    return {
        "choice": input("Make a choice\n> "),
        "zeroType": zeroTask
    }


def check_menu_choice(choice):
    mType = choice["zeroType"]
    choice = choice["choice"]

    if mType:
        if (choice == '2'):
            exit(0)
        else:
            add()

def add():
    


tm = TaskManager()
try: 
    tm.load()
    print(f"{tm.taskCount()} {"tasks" if tm.taskCount() > 1 else "task"} loaded.")
except FileNotFoundError:
    print("No tasks loaded.")


check_menu_choice(display_menu())




