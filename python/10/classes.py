class ToDoList:

    def __init__(self):

        self.list_of_tasks = {}

    
    def list_tasks(self):


        for task_number, task in self.list_of_tasks.items():

            print(f"{task_number} - {task['task']}\nDescrição: {task['description']}\nStatus: {task['status']}")


    def add_task(self, task, description, task_status="pendente"):

        task_number = len(self.list_of_tasks)

        self.list_of_tasks[f"{task_number}"] = {"task": task, "description": description, "status": task_status}

