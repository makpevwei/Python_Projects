import time

# Get the current date and time in a readable format
now = time.strftime("%b %d, %Y %H:%M:%S")

# Default file path for storing todos
FILEPATH = "todos.txt"


def read_from_todos(file_path=FILEPATH):
    """
    Reads the current list of todos from the specified file.

    Parameters:
    file_path (str): The path to the file storing todos. Defaults to "todos.txt".

    Returns:
    list: A list of todo items read from the file.
    """
    # Open the file in read mode to get the current list of todos
    with open(file_path, "r") as file:
        words = file.readlines()  # Read all lines (todos) into a list
    return words


def write_to_todos(todos_list, file_path=FILEPATH):
    """
    Writes the provided list of todos to the specified file.

    Parameters:
    todos_list (list): The list of todos to write to the file.
    file_path (str): The path to the file storing todos. Defaults to "todos.txt".
    """
    # Open the file in write mode and save the updated todo list back to the file
    with open(file_path, "w") as file:
        file.writelines(todos_list)  # Write the updated list to the file


def add_todos():
    """
    Adds a new todo item to the list.
    
    Prompts the user to enter a new todo item, appends it to the list,
    and writes the updated list to the file.
    """
    todo = input("Enter a todo: ").strip().capitalize() + "\n"
    
    # Read the current list of todos
    todos = read_from_todos()
    
    # Append the new todo to the list of todos
    todos.append(todo)
    
    # Write the updated todos list to the file
    write_to_todos(todos)


def view_todos():
    """
    Displays the current list of todo items.
    
    Reads the todos from the file, removes newline characters for display,
    and prints each todo item with its index.
    """
    # Read the current list of todos
    todos = read_from_todos()

    # Remove newline characters from each item for a cleaner display
    new_todos = [item.strip("\n") for item in todos]
    
    # Loop through todos with an index starting from 1 and display each
    for index, item in enumerate(new_todos, 1):
        print(f"{index}: {item}")


def edit_todos():
    """
    Edits an existing todo item.
    
    Prompts the user for the number of the todo to edit, and for the new todo text,
    then updates the specified todo item and writes the changes back to the file.
    """
    try:
        # Get the todo number to edit
        number = int(input("Enter the number of the todo to edit: "))
        new_todo = input("Enter new todo: ").strip().capitalize() + "\n"
        
        # Read the current list of todos
        todos = read_from_todos()
        
        # Update the specified todo with the new text
        todos[number - 1] = new_todo  # Adjust by -1 for zero-based index
        
        # Write the updated todos back to the file
        write_to_todos(todos)
        
        print("Todo updated successfully.")
    except Exception as error:
        # Handle invalid input or out-of-range index
        print("Error:", error, "\nPlease enter a valid todo number.")


def delete_todos():
    """
    Removes a completed todo item from the list.
    
    Prompts the user for the number of the todo to delete, removes the specified todo,
    and writes the updated list back to the file.
    """
    try:
        # Get the todo number to delete
        number = int(input("Number of the todo completed to remove: "))
        
        # Read the current list of todos
        todos = read_from_todos()
        
        # Remove the specified todo from the list
        removed_todo = todos.pop(number - 1)  # Adjust by -1 for zero-based index
        
        # Write the updated todos back to the file
        write_to_todos(todos)
        
        print(f"Todo '{removed_todo.strip()}' removed successfully.")
    except Exception as error:
        # Handle invalid input or out-of-range index
        print("Error:", error, "\nPlease enter a valid todo number.")


def exit_app():
    """
    Exits the Todos application with a farewell message.
    """
    print("Exiting Todos App... Goodbye!")


def run_app():
    """
    Runs the main loop of the Todos application.
    
    Provides a menu for the user to choose from various actions,
    and continuously prompts the user for choices until they exit.
    """
    print("It is", now)
    print()
    print("Welcome to Todos App")
    print("-" * 20)
    print("Enter 1 to add todos")
    print("Enter 2 to show todos")
    print("Enter 3 to edit todos")
    print("Enter 4 to remove completed todos")
    print("Enter 5 to exit the application")
    
    # Loop until the user decides to exit
    while True:
        try:
            # Ask the user for an action
            choice = int(input("\nEnter your choice: "))
            
            # Match the user's action to different cases
            match choice:
                case 1:
                    # Add a new todo item
                    add_todos()
                case 2:
                    # Display all todo items
                    view_todos()
                case 3:
                    # Edit an existing todo item
                    edit_todos()
                case 4:
                    # Mark a todo as complete (removing it from the list)
                    delete_todos()
                case 5:
                    # Exit the program
                    exit_app()
                    break  # Exit the loop to end the program
                case _:
                    # Handle any unrecognized actions
                    print("Invalid choice: Please enter a number from 1 to 5.")
                    
        except Exception as error:
            print("Error:", error, "\nPlease enter a valid numeric choice.")


# Run the app if this module is the main entry point
if __name__ == "__main__":
    run_app()
