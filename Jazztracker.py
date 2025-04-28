#Jazztracker v0.5
#by Into-The-Blu (https://github.com/Into-The-Blu) for a roadmap.sh project
#free use license but I doubt anyone will

import re
import datetime
import math

#Todo:
#-rework whole thing for that way you thought of
#-add json handling

#test list:
#add case works, function half works
#inputMonitor function - works so far
#everything else - not tested

taskList = [] #temporary, in place of json
#cmdList = "^add|^delete|^update|^mark|^list"
class task:
    def __init__(self, id, body, status, createdAt, updatedAt):
        self.id = id
        self.body = body
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
statusFilter = None
def help():
    print(f"\nCommands:\n============================================================================\nadd <task>...................adds a task with the default status \"todo\"\ndelete <taskid>..............deletes the task associated with the given id\nupdate <taskid> <task>.......overwrites the task associated with the given id\nmark-in-progress <taskid>....marks the task at a given id as in-progress\nmark-done <taskid>...........marks the task at a given id as done\nlist.........................lists all tasks\nlist todo....................lists all tasks tagged as todo\nlist in-progress.............lists all tasks tagged as in-progress\nlist done....................lists all tasks tagged as done\n============================================================================\n")

def add():
    taskTemp = task(0, None, "todo", datetime.datetime.now() , 0) #refine the dt
    taskTemp.id = id
    taskTemp.body = userInput[1]
    taskList.insert(id, taskTemp)
    print(taskList)
    print(taskList[0].body)
    if len(taskList) > 1:
        print(taskList[1].body)
    print(f"\nTask succesfully created! ID: {id}\n")
    del taskTemp
    
def delete():
    taskList[id] = None
    print(f"\nTask ID: {userInput[1]} succesfully deleted!\n")

def printList():
    for i in range(len(taskList)):
        if (taskList[i] == True) and (statusFilter == taskList[i].status or False):
            print(f"ID: {i + 1} | Date created/updated: {taskList[i].createdAt} | {taskList[i].body}")
        else:
            continue

def idHandler():
    pass

def inputMonitor():
    global userInput
    userInput = input().split(" ")
    match userInput[0]:
        case "add":
            idHandler()
            add()
        case "delete":
            delete()
        case "update":
            taskList[id].updatedAt = datetime.datetime.now() #refine this
        case "mark-in-progress":
            id = userInput[1] - 1
            taskList[id].status = "in progress"
        case "mark-done":
            id = userInput[1] - 1
            taskList[id - 1].status = "done"
        case "list":
            if len(userInput) > 1:
                match userInput[1]:
                    case "done":
                        printList()
                    case "todo":
                        statusFilter = userInput[1]
                        printList()
                    case "in-progress":
                        statusFilter = userInput[1]
                        printList()
            else:
                printList()
        case "help":
            help()
        case _:
            print(f"[ERROR]: command '{userInput[0]}' not recognised")
    userInput = []
    inputMonitor()

print(f"\nWelcome to Jazztracker v0.5! Get started by adding a task, or use the \"help\" command if you're stuck.\n")     
inputMonitor()

#commands: 
#add <task>
#delete <taskid>
#update <taskid> <task>
#mark-in-progress <taskid>
#mark-done <taskid>
#list
#list todo
#list in-progress
#list done




