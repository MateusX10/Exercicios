from classes import ToDoList
from funcs import *
from sys import exit


ToDoList1 = ToDoList()


menu_valid_options = [1, 2, 3, 4, 5]


list_of_titles = ["Add task", "Change task status", "list tasks", "Remove task", "quit"]


while True:

    menu()

    while True:

        user_choice = leiaInt("Enter your choice: ")

        if user_choice in menu_valid_options:

            break

        print("\033[1;31mInvalid option.Please, enter a valid number that exits in the menu options!.\033[m")


    title(list_of_titles[user_choice - 1])

    # add task
    if user_choice == 1:

        while True:

            task_name = str(input("Task name: ")).strip().capitalize()

            if len(task_name) >= 3:

                break

            print("\033[1;31mThe task need to have at least 3 characters.\033[m")

        while True:

            task_description = str(input("Task description: ")).strip()

            if len(task_description) >= 5:

                break
            print("\033[1;31mThe task description need to have at least 5 characters.\033[m")

        while True:

            print("Task possible status:\n[ 1 ] - Pending\n[ 2 ] - Compleded\n")

            task_status = leiaInt("Which is the status of the task? ")

            if task_status in [1, 2]:

                if task_status == 1:

                    task_status = "pending"

                else:

                    task_status = "completed"

                break

            print('Invalid option.Please, enter just "1" or "2".\033[m')


    
        ToDoList1.add_task(task_name, task_description, task_status)

    # mark task as completed
    elif user_choice == 2:

        ToDoList1.list_tasks()

        task_position = ToDoList1.get_task_position()

        ToDoList1.change_task_status(task_position)





    # list tasks
    elif user_choice == 3:

        ToDoList1.list_tasks()

    # remove tasks
    elif user_choice == 4:

        ToDoList1.list_tasks()

        task_position = ToDoList1.get_task_position()

        ToDoList1.remove_task(task_position)
    
    # quit the program
    elif user_choice == 5:

        exit(1)