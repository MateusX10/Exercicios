from classes import ToDoList
from funcs import *
from sys import exit


ToDoList1 = ToDoList()


#list of valid option of the menu
menu_valid_options = [1, 2, 3, 4, 5]

# list of titles
list_of_titles = ["Add task", "Change task status", "list tasks", "Remove task", "quit"]


while True:

    # show menu
    menu()

    # user choice
    while True:

        user_choice = leiaInt("Enter your choice: ")

        if user_choice in menu_valid_options:

            break

        print("\033[1;31mInvalid option.Please, enter a valid number that exits in the menu options!.\033[m")

    # show the title according to user choice
    title(list_of_titles[user_choice - 1])

    # add task
    if user_choice == 1:

        while True:
            
            # data input of task name
            task_name = str(input("Task name: ")).strip().capitalize()

            # check if the length of the name is equal or bigger than 3 caracters.It must have at least 3 characters to be a valid task name
            if len(task_name) >= 3:

                break

            print("\033[1;31mThe task need to have at least 3 characters.\033[m")

        while True:
            
            # data input of task description
            task_description = str(input("Task description: ")).strip()

            if len(task_description) >= 5:

                break
            print("\033[1;31mThe task description need to have at least 5 characters.\033[m")

        while True:

            #data input of task status
            
            print("Task possible status:\n[ 1 ] - Pending\n[ 2 ] - Completed\n")

            task_status = leiaInt("Which is the status of the task? ")

            # task status must be equal to 1 (pending) or 2 (completed)
            if task_status in [1, 2]:
                
                # task status is equal to "pending"
                if task_status == 1:

                    task_status = "pending"

                # task status is equal to "completed"
                else:

                    task_status = "completed"

                break

            print('Invalid option.Please, enter just "1" or "2".\033[m')


        # calls the function that add the task to the to do list
        ToDoList1.add_task(task_name, task_description, task_status)

    # mark task as completed
    elif user_choice == 2:

        ToDoList1.list_tasks()

        # calls tre function that get the task position
        task_position = ToDoList1.get_task_position()

        # calls the function that change the task status
        ToDoList1.change_task_status(task_position)

    # list tasks
    elif user_choice == 3:

        #calls the function that show the task list of to do list
        ToDoList1.list_tasks()

    # remove tasks
    elif user_choice == 4:

        # calls the function that show the list of tasks
        ToDoList1.list_tasks()

        # calls the function that get the position of the task
        task_position = ToDoList1.get_task_position()

        # calls the funtion that removes the task according to its position
        ToDoList1.remove_task(task_position)
    
    # quit the program
    elif user_choice == 5:

        exit(1)