class ToDoList:

    def __init__(self):

        # list of tasks of the current ToDoList object
        self.list_of_tasks = {}

    
    def list_tasks(self)->None:
        '''-> Show the list of tasks of the To-do list

            Parameters:

                return: no return
        '''

    
        for task_number, task in self.list_of_tasks.items():

            task_status = task['status']

            if task_status == "completed":

                print(f"\n\033[1m{task_number} - \033[1;32m{task['task']}\033[m\n\033[1;34mDescrição:\033[m {task['description']}\n\033[1;34,Status: \033[1;32m{task['status']}\033[m\n")

            else:

                print(f"\n\033[1m{task_number} - \033[1;32m{task['task']}\033[m\n\033[1;34mDescrição:\033[m {task['description']}\n\033[1;34,Status: \033[1;31m{task['status']}\033[m\n")





    def add_task(self, task, description, task_status="pending")-> None:
        '''-> Add a task to the list of tasks

            Parameters:

                task(str): name of the task
                description(str): description of the task
                task_status(str): status of the task (can be pending or completed - pending is default)
        '''

        task_number = len(self.list_of_tasks)

        self.list_of_tasks[f"{task_number + 1}"] = {"task": task, "description": description, "status": task_status}


    def get_task_position(self)-> int:
        '''-> Gets task position
            Parameters:

                return: returns the position of the task
        '''


        from funcs import leiaInt

        while True:

            user_choice = leiaInt("Which task? ")

            if 0 < user_choice <= len(self.list_of_tasks):

                break
            
            print("\033[1;31mInvalid option.Please, try again with a valid and choice.\033[m")

        task_position = user_choice 


        return task_position


    def change_task_status(self, task_position)-> None:
        '''-> Changes task position in the to do list

            Parameters:

            task_position(int): task position in the to do list
            return: no return
        '''

        task_status = self.list_of_tasks[f"{task_position}"]["status"] 

        if task_status == "pending":

            task_status = "completed"

        elif task_status == "completed":

            task_status = "pending"
            

        self.list_of_tasks[f"{task_position}"]["status"] = task_status


    def remove_task(self, task_position):
        '''-> Remove an task of the to do list

            Parameters:

                task_position(int): position of the task in the to do list
                return: no return
        '''


        self.list_of_tasks.pop(task_position)


        