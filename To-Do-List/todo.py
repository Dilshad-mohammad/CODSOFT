class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add(self, task):
        self.tasks.append({"task": task,"completed": False})

    def view(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} - {status}")

    def Done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
        else:
            print("Invalid task index.")

    def delete(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task index.")

def main():
    todo = TodoList()
    while True:
        Do = int(input('''
        Press 1. Add Task
        Press 2. View Tasks
        Press 3. Mark Task as Complete
        Press 4. Delete Task
        Press 5. Exit
        '''))

        if Do == 1:
            task = input("Enter task: ")
            todo.add(task)
        elif Do == 2:
            todo.view()
        elif Do == 3:
            index = int(input("Enter task index to mark as Done: "))
            todo.Done(index)
        elif Do == 4:
            index = int(input("Enter task index to delete the task: "))
            todo.delete(index)
        elif Do == 5:
            break
        else:
            print("Enter Valid Number. ")
if __name__ == "__main__":
    main()
