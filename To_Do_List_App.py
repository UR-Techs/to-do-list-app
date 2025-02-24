#24/2/2025
import os 

# Defining function for the options to be given to the user
def opt_list():
    print("\nSelect an option from the menu below:")
    print("1. Add tasks to the list.")
    print("2. Remove a task from the list by its name.")
    print("3. Display all tasks.")
    print("4. Exit the program.")

#22/2/2025 Defining a new function to load data from a text file
def load_tasks():
    global tasks
    tasks = []
    if os.path.exists('To_Do_list_Data.txt'):
        with open('To_Do_list_Data.txt','r') as task_data:
            tasks.extend(task_data.read().splitlines())
    else:
        print("⚠️ No saved tasks found.")
       

def add_task():
    """Function to add a task"""
    new_task = input("Please enter the task to add to your To-Do List: ")
    tasks.append(new_task)
#saving the added task in the file
    if os.path.exists('To_Do_list_Data.txt'):
        with open('To_Do_list_Data.txt','a') as task_data:
            task_data.write(new_task + "\n")
            print(f"✅ '{new_task}' has been added to your To-Do List.")

    else:
        print("⚠️ No saved tasks found.")

    
'''    print(f"✅ '{new_task}' has been added to your To-Do List.")
    print("\n📌 Your To-Do List:")
    for i, task in enumerate(tasks, 1):  # Numbering tasks
        print(f"{i}. {task}")'''

def remove_task():
    """Function to remove a task"""
    if tasks:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, 1):  # Numbering tasks
            print(f"{i}. {task}")
        new_task = input("Please enter the task to delete from your To-Do List: ")
        if new_task in tasks:
            tasks.remove(new_task)
            print(f"❌ '{new_task}' has been deleted from your list.")
            if tasks:
                print("\n📌 Your To-Do List:")
                for i, task in enumerate(tasks, 1):  # Numbering tasks
                    print(f"{i}. {task}")
            else:
                print("Your task list is now empty.")
        else:
            print(f"⚠️ '{new_task}' is not in your list.")
    else:
        print("\n⚠️ Your To-Do List is already empty.")

def display_tasks():
    """Function to display all tasks"""
    if tasks:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, 1):  # Numbering tasks
            print(f"{i}. {task}")
    else:
        print("\n⚠️ Your To-Do List is empty.")

def exit_prog():
    """Function to exit the program"""
    print("👋 Exiting the program. Goodbye!")

def cond_logic():
    """Main function to handle user input"""
    while True:
        opt_list()
        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                #24/2/2025
                load_tasks()
                display_tasks()
                add_task()
                display_tasks()
            elif user_input == 2:
                #24/2/2025
                load_tasks()
                remove_task()
            elif user_input == 3:
                #24/2/2025
                load_tasks()
                display_tasks()
                ##display_tasks()
            elif user_input == 4:
                exit_prog()
                break
            else:
                print("⚠️ Invalid input! Please select a number between 1 and 4.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    cond_logic()
