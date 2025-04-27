import re
import time

taskList = [] #temporary, in place of json
cmdList = "^add|^delete|^update|^mark|^list"
class task:
    def __init__(self, body, status, createdAt, updatedAt):
        self.body = body
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
taskTemp = task() #creates task object to be written to in current session

def add():
    taskList.append(taskTemp)
    id = taskList.index(taskTemp)
    print(f"task succesfully created! ID: {id}")
    return id

def delete():
    taskList[id] = None
    print(f"task ID: {id} succesfully deleted!")

def inputMonitor():
    userInput = input().split(" ").strip("['']")
    match userInput[0]:
        case "add":
            taskTemp.body = userInput[1]
            taskTemp.status = "todo"
            taskTemp.createdAt = datetime.datetime("%x","%X")
            add()
        case "delete":
            id = userInput[1]
            delete()
        case "update":
            id = userInput[1]
            taskList[id].body = userInput[2]
            taskList[id].createdAt = datetime.datetime("%x","%X")
        case "mark":
            pass
        case "list":
            pass
        case _:
            print(f"[ERROR]: command '{userInput[0]}' not recognised")
            inputMonitor()
        

    







