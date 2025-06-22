# USING OBJECTS (Classes) TO MAKE A TASK MANAGER

import time

class Task:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.completed = False
        self.created = time.ctime()

    def __repr__(self):
        return f"Task({self.name!r}, {self.desc!r} : {self.completed!r})"

    def __str__(self):
        return f'[{self.created}] {self.name}: {self.desc} ({"Complete" if self.completed else "Incomplete"})'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, name, desc):
        self.tasks.append(Task(name, desc))

    def viewTasks(self):
        for task in self.tasks:
            print(task)

    def findTasks(self, attempt):
        possible = []
        for index, task in enumerate(self.tasks):
            if attempt.lower() in task.name.lower():
                possible.append({
                    "name": task.name,
                    "index": index
                })
        if (len(possible) == 0):
            return None
        elif (len(possible) == 1):
            return possible[0]
        else:
            return possible


    def deleteTask(self, index):
        del self.tasks[index]

    def toggleCompletion(self, index):
        self.tasks[index].completed = not self.tasks[index].completed





manager = TaskManager()


manager.addTask("Walk", "pls")
manager.addTask("Dog", "pls")
manager.addTask("Test", "pls")

manager.viewTasks()


manager.deleteTask(manager.findTasks("Dog")["index"]) #test case. need to check what is return by the findTasks
manager.toggleCompletion(manager.findTasks("Walk")["index"])

print("----------------")
manager.viewTasks()




