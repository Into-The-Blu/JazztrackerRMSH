#Jazztracker v0.9
#by Into-The-Blu (https://github.com/Into-The-Blu) for a roadmap.sh project
#free use license but I doubt anyone will

from datetime import datetime
from dataclasses import dataclass
import sys

# Todo:
# - add json handling
# - add more qol and error handling

# test list:
# - 

taskList = [] # temporary, in place of json
@dataclass
class Task:  # self explanatory
    taskId_objAttr: int
    body: str
    status: str
    createUpdateAt: str
    
def help():  # self explanatory
    print("\nCommands:\n============================================================================\nadd <task>...................adds a task with the default status \"todo\"\ndelete <taskid>..............deletes the task associated with the given id\nupdate <taskid> <task>.......overwrites the task associated with the given id\nmark-in-progress <taskid>....marks the task at a given id as in-progress\nmark-done <taskid>...........marks the task at a given id as done\nlist.........................lists all tasks\nlist todo....................lists all tasks tagged as todo\nlist in-progress.............lists all tasks tagged as in-progress\nlist done....................lists all tasks tagged as done\nexit.........................exits program\n============================================================================\n")

# takes processed args from inputMonitor():
# - commandCalled dictates what case is met, and so what actions are taken on the other 3 parameters
# - param1 will always have a value unless the list command is called with no args
# - param2 has a value when a command has 2 args, or when the task body in an add command is longer than one word
# - param2 can and often does contain more than one word - if the add command is used and the task body is longer than one word, 
# param1 and param2 are stitched together to create the task body
# - taskId is the output of the function idHandler(), used as an arg when taskManager() is called. 
# is the id the current task will be given if using the add command
def taskManager(commandCalled, param1, param2, taskId):  
    tag = param1  # ln 28 to 33 formats CLI syntax to user-presentable form for printList()
    match param1:
        case "in-progress":
            param1 = "In progress"
        case "done":
            param1 = "    Done   "
    match commandCalled:
        case "add":
            taskTemp = Task(taskId_objAttr=taskId, body=str, status="    Todo   ", createUpdateAt=datetime.now()) # blank template to be written to, has a lifespan of the add case
            taskTemp.taskId_objAttr = taskId
            if param2:
                taskTemp.body = param1 + param2
            else:
                taskTemp.body = param1
            taskList.insert(taskId, taskTemp)
            print(f"\nTask succesfully created! ID: {taskId}\n")
            return taskList
        case "delete":
            for i, task in enumerate(taskList): # repeatedly used algorithm to find a task object in the list with a given id, then take actions on that task object. further examples marked by #*
                if str(task.taskId_objAttr) == param1:
                    task.pop()
                    return taskList
            else:
                print(f"\n[ERROR]: task with ID {param1} does not exist")
        case "update":
            for i, task in enumerate(taskList): #*
                if str(task.taskId_objAttr) == param1:
                    task.body = param2
                    task.createUpdateAt = datetime.now()
                    print(f"\nTask with ID {param1} succesfully updated!\n")
                    return taskList
            else:
                print(f"\n[ERROR]: task with ID {param1} does not exist")
        case "list": # used to decide whether a filter gets passed to printList() 
            if param1:
                printList(param1, True, tag)
            else:
                printList(None, False, "")
        case "mark-in-progress":
            for i, task in enumerate(taskList): #*
                if str(task.taskId_objAttr) == param1:
                    task.status = "In progress"
                    task.createUpdateAt = datetime.now()
                    return taskList
            else:
                print(f"\n[ERROR]: task with ID {param1} does not exist")
        case "mark-done":
            for i, task in enumerate(taskList): #*
                if str(task.taskId_objAttr) == param1:
                    task.status = "    Done   "
                    task.createUpdateAt = datetime.now()
                    return taskList
            else:
                print(f"\n[ERROR]: task with ID {param1} does not exist")
        case "help":
            help()
        case "exit":
            sys.exit()
        case _:
            print(f"[ERROR]: command '{commandCalled}' not recognised")

def printList(statusFilter, filterActive, tagParam):
    print("\nID |   Created/updated   |    Status   |     Task") # formatting
    lineCount = 0
    for i, task in enumerate(taskList):
        if task.status == statusFilter or not filterActive: # prints a task if its status meets the filter or if the filter isn't active
            lineCount += 1 
            if taskList[i].taskId_objAttr > 9:
                print(f"{taskList[i].taskId_objAttr} | {taskList[i].createUpdateAt.replace(microsecond=0)} | {taskList[i].status} |   {taskList[i].body}")
            else: # purely for formatting, would become wonky if lineCount > 9 otherwise
                print(f"{taskList[i].taskId_objAttr}  | {taskList[i].createUpdateAt.replace(microsecond=0)} | {taskList[i].status} |   {taskList[i].body}")
    if lineCount == 0:
        print(f"No tasks tagged as {tagParam}") # tagParam was created specifically for this line. i am very sorry
    print(" ") # formatting

# as tasks' id values are added to taskList in ascending order, you can find the biggest id by reading the last index.
# after doing so, it adds one to create the next id to be written
# if there's nothing in the list, the next id to be written is 1 
def idHandler(): 
    try:
        return taskList[-1].taskId_objAttr + 1
    except IndexError:
         return 1

def inputMonitor():
    taskBodyHalf = None 
    # ^initialises the var so it doesn't whine at me - var gets sent as the param2 arg in taskManager() if it needs to exist. 
    # called as such because in a multi word task body it is stitched together with param1
    userInput = input().split(" ") # formats command and its args
    if len(userInput) > 2: # ln 125 to 131 decides what the args contain
        taskBodyHalf = " " + userInput[2]
        if len(userInput) > 3:
          i = 3
          while i < len(userInput):
            taskBodyHalf = taskBodyHalf + " " + userInput[i]
            i += 1
    try: # ln 132 to 139 decides what args get sent
        x = userInput[2] # deliberate, botched solution to tripping the index error 
        taskManager(userInput[0], userInput[1], taskBodyHalf, idHandler())
    except IndexError:
        try: 
            taskManager(userInput[0], userInput[1], None, idHandler())
        except IndexError: 
            taskManager(userInput[0], None, None, idHandler())
    inputMonitor() # recurses once taskManager() finishes its task to allow another command

print("\nWelcome to Jazztracker v0.9! Get started by adding a task, or use the \"help\" command if you're stuck.\n")     
inputMonitor()

#commands: 
#help
#add <task>
#delete <taskid>
#update <taskid> <task>
#mark-in-progress <taskid>
#mark-done <taskid>
#list
#list in-progress
#list done
#exit




