import re

taskList = [] #test, temporary

cmdList = "^add|^delete|^update|^mark|^list"

class task:
    def __init__(self, body, id, status, createdAt, updatedAt):
        self.body = body
        self.id = id
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

def inputMonitor():
    x = re.search(cmdList, input())
    if x == true:
        match x:
            case "add":
                pass
            case "delete":
                pass
            case "update":
                pass
            case "mark":
                pass
            case "list":
                pass
    else: 
        y = input()
        y = y.split(" ")
        del y[1]
        y = str(y)
        y = y.strip("['']")
        print(f"[ERROR]: command '{y}' not recognised")


    







