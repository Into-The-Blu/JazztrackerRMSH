#Jazztracker v0.5
#by Into-The-Blu (https://github.com/Into-The-Blu) for a roadmap.sh project
#free use license but I doubt anyone will

import re
import datetime
import math
from dataclasses import dataclass

#Todo:
#-rework whole thing for that way you thought of
#-add json handling

#test list:

taskList = [] #temporary, in place of json
@dataclass
class Task:
    taskId_objAttr: int
    body: str
    status: str
    createdAt: str
    updatedAt: str

def help():
    print(f"\nCommands:\n============================================================================\nadd <task>...................adds a task with the default status \"todo\"\ndelete <taskid>..............deletes the task associated with the given id\nupdate <taskid> <task>.......overwrites the task associated with the given id\nmark-in-progress <taskid>....marks the task at a given id as in-progress\nmark-done <taskid>...........marks the task at a given id as done\nlist.........................lists all tasks\nlist todo....................lists all tasks tagged as todo\nlist in-progress.............lists all tasks tagged as in-progress\nlist done....................lists all tasks tagged as done\n============================================================================\n")

def taskManager(commandCalled, param1, param2):
    match commandCalled:
        case "add":
            taskTemp = Task(taskId_objAttr=taskId, body=str, status="todo", createdAt=datetime.datetime.now() , updatedAt=str) #refine the dt
            taskTemp.taskId_objAttr = taskId
            taskTemp.body = param1
            taskList.insert(taskId, taskTemp)
            print(f"\nTask succesfully created! ID: {taskId}\n")
            return taskList
        case "delete":
            taskList.taskId_objAttr.remove(param1)
            return taskList
        case "update":
            taskList[taskList.taskId_objAttr.index(param1)].body = param2
            return taskList
        case "list":
            if param1 == True:
                printList(param1, True)
            else:
                printList(None, False)
        case "mark-in-progress":
            taskList[taskList.taskId_objAttr.index(param1)].status = "in progress"
            return taskList
        case "mark-done":
            taskList[taskList.taskId_objAttr.index(param1)].status = "done"
            return taskList
        case "help":
            help()
        case _:
            print(f"[ERROR]: command '{commandCalled}' not recognised")

def printList(statusFilter, filterActive):
    for i in enumerate(taskList):
        if taskList[i].status == statusFilter or filterActive == False:
            print(f"ID: {taskList[i].taskId_objAttr} | Date created/updated: {taskList[i].createdAt} | {taskList[i].body}")

def idHandler():
    return taskId

def inputMonitor():
    userInput = input().split(" ")
    try:
        taskManager(userInput[0], userInput[1], userInput[2])
    except:
        try: 
            taskManager(userInput[0], userInput[1], False)
        except: 
            taskManager(userInput[0], False, False)
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
#list in-progress
#list done




