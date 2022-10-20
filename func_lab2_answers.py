tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]

# 1
def uncompleted_tasks():
    uncomp_tasks = []
    for task in tasks:
        if task["completed"] == False:
            uncomp_tasks.append(task["description"])

    print(uncomp_tasks)


# 2
uncompleted_tasks()


def completed_tasks():
    comp_tasks = []
    for task in tasks:
        if task["completed"] == True:
            comp_tasks.append(task["description"])

    print(comp_tasks)


completed_tasks()

# 3
def task_descriptions():
    task_desc = []
    for task in tasks:
        task_desc.append(task["description"])

    print(task_desc)


task_descriptions()

4
def at_least():
    user_inp = input("Filter tasks by time: ")
    at_least_list = []
    for task in tasks:
        if task["time_taken"] >= int(user_inp):
            at_least_list.append(task["description"])

    print(at_least_list)


at_least()

# 5
def pick_by_desc():
    user_inp = input("Pick a task by description: ")
    for task in tasks:
        if task["description"] == user_inp:
            print(task)


pick_by_desc()

# 6
def update_by_desc():
    user_inp = input("Description to complete: ")
    for task in tasks:
        if (user_inp == task['description']):
            task['completed'] = True
        

update_by_desc()

# 7
def add_task():
    user_inp = input("Add task as dict: ")
    tasks.append(user_inp)


add_task()

print(tasks)



"""
def quit_func():
    return

 
# 8
menu_list = [
    "Menu:",
    "1: Display All Tasks",
    "2: Display Uncompleted Tasks",
    "3: Display Completed Tasks",
    "4: Mark Task as Complete",
    "5: Get Tasks Which Take Longer Than a Given Time",
    "6: Find Task by Description",
    "7: Add a new Task to list",
    "M or m: Display this menu",
    "Q or q: Quit",
]

func_list = [
    {1: print(tasks)},
    {2: uncompleted_tasks()},
    {3: completed_tasks()},
    {4: print("not a function")},
    {5: at_least(4)},
    {6: pick_by_desc()},
    {7: add_task()},
    {"M": "menu_choice()"},
    {"Q": quit_func()},
]


def menu_choice(foo):
    for i in foo:
        print(i)
    user_inp = input()
    for j in func_list:
        if user_inp == func_list[j]:
 """
