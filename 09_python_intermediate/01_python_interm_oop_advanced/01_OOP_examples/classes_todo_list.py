class Task:
    def __init__(self, description, deadline=None):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        deadline = f" (Deadline: {self.deadline})" if self.deadline else ""
        return f"{self.description}{deadline} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = list()

    def add_task(self, description, deadline=None):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index]}")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task}")
        else:
            print("No tasks in the to-do list.")

todo_list = ToDoList()

todo_list.add_task("Buy groceries", "2024-09-01")
todo_list.add_task("Finish Python project")
todo_list.list_tasks()
todo_list.mark_task_completed(0)
todo_list.remove_task(1)
todo_list.list_tasks()
