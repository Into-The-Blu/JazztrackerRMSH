Project URL: https://roadmap.sh/projects/task-tracker

Requires: Python 3.6+, jsonpickle, a POSIX compliant terminal

Program is a standalone .py file. Store wherever you want it to live (creates an additional JSON file in current dir)


Thank you for taking the time to use this!

This is my roadmap.sh Task Tracker project entry - it (should) meet the following requirements:

1. Runs from CLI
2. Accepts user actions and inputs as arguments
3. Store tasks in a JSON file, which should be created if it doesn't already exist
3. Add, update and delete tasks
4. Mark tasks as in progress or done
5. List all tasks, or list tasks tagged as done, todo or in progress
6. Handles errors and edge cases

Unfortunately I wasn't able to meet these two requirements:

7. Use the native file system of the programming language to interact with the JSON file
8. Must not use any external libraries

as my use of dataclasses made the list unserialisable.

Code is sparsely commented, my apologies.

Jazz :3