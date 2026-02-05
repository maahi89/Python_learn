FILE="list.txt"
def load_tasks():
    tasks = []
    try:
        with open(FILE,'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return[]
def save_tasks(tasks):
    with open(FILE,'w') as f:
        for task in tasks:
            f.write(f"{task}\n")
def add_task(tasks):
    task=input("enter the task")
    tasks.append(task)
    print(f"{task} addded successfully")
def delete_task(tasks):
    task=input("enter the task to be deleted ")
    if task in tasks:
        tasks.remove(task)
        print(f"{task} succesfully removed")
    else:
        print(f"{task} not found in the list")
def search_task(tasks):
    task= input("enter the task yu want to search ")
    if task in tasks:
        print(f"{task} found in the list")
    else:
        print(f"{task} not found in the list")    

def display_task(tasks):
    if not tasks:
        print("no tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def main():
    tasks=load_tasks()
    while True:
        print("\n to do list menu")
        print("1. add task")
        print("2. delete task")
        print("3. display tasks")
        print("4. search task")
        print("5. exit")
        choice= int(input("enter the choices 1/2/3/4/5: "))
        if choice==1:
            add_task(tasks)
        elif choice==2:
            delete_task(tasks)
        elif choice==3:
            display_task(tasks)
        elif choice==4:
            search_task(tasks)
        elif choice==5:
            print("exiting the to do list application")
            break    
main() 



           
