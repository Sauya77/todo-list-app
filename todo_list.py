class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        print(f"Added task: {description}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Marked task {index} as complete: {self.tasks[index]['description']}")
        else:
            print(f"Task {index} does not exist.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "done" if task["completed"] else "not done"
                print(f"Task {i}: {task['description']} - {status}")

# Example usage:
def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Display tasks")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter the task number to complete: "))
            todo_list.complete_task(index)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
