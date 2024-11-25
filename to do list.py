# To-Do List Application

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to add a task
def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to your To-Do list.")

# Function to remove a task
def remove_task(todo_list):
    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from your To-Do list.")
    else:
        print(f"Task '{task}' not found in your To-Do list.")

# Function to view the to-do list
def view_tasks(todo_list):
    if todo_list:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty.")

# Main program
def main():
    todo_list = []

    while True:
        display_menu()

        # Get user input for menu option
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
