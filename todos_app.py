# Loop until the user decides to exit
while True:
    # Ask the user for an action and standardize input by stripping whitespace and converting to lowercase
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    
    # Match the user's action to different cases
    match user_action:
        case "add":
            # Case for adding a new todo item
            # Prompt the user to enter a new todo, capitalize it, and add a newline
            todo = input("Enter a todo: ").strip().capitalize() + "\n"
            
            # Open the file in read mode to get the current list of todos
            with open("todos.txt", "r") as file:
                todos = file.readlines()  # Read all lines (todos) into a list
                
            # Append the new todo to the list of todos
            todos.append(todo)
            
            # Open the file in write mode and save the updated todo list back to the file
            with open("todos.txt", "w") as file:
                file.writelines(todos)  # Write the updated list to the file
    
        case "show":
            # Case for displaying all todo items
            # Open the file in read mode to fetch the current list of todos
            with open("todos.txt", "r") as file:
                todos = file.readlines()  # Read all lines (todos) into a list

            # Remove newline characters from each item for a cleaner display
            new_todos = [item.strip("\n") for item in todos]
            
            # Loop through todos with an index starting from 1 and display each
            for index, item in enumerate(new_todos, 1):
                print(f"{index}: {item}")
                
        case "edit":
            # Case for editing an existing todo item
            try:
                # Ask the user for the number of the todo to edit and convert to an integer
                number = int(input("Enter the number of the todo to edit: "))
                
                # Prompt the user for the new todo text
                new_todo = input("Enter new todo: ").strip().capitalize() + "\n"
                
                # Open the file in read mode to get the current list of todos
                with open("todos.txt", "r") as file:
                    todos = file.readlines()  # Read all lines (todos) into a list
                
                # Update the specified todo with the new text
                todos[number - 1] = new_todo  # Adjust by -1 for zero-based index
                
                # Open the file in write mode and save the updated todo list
                with open("todos.txt", "w") as file:
                    file.writelines(todos)  # Write the updated list to the file

                print("Todo updated successfully.")
            except (IndexError, ValueError):
                # Catch errors if the input number is invalid or out of range
                print("Invalid input: Please enter a valid todo number.")
                
        case "complete":
            # Case for marking a todo as complete (removing it from the list)
            try:
                # Ask the user for the number of the todo to mark as complete
                number = int(input("Number of the todo to complete: "))
                
                # Open the file in read mode to get the current list of todos
                with open("todos.txt", "r") as file:
                    todos = file.readlines()  # Read all lines (todos) into a list
                
                # Remove the specified todo from the list
                todos.pop(number - 1)  # Adjust by -1 for zero-based index
                
                # Open the file in write mode and save the updated todo list
                with open("todos.txt", "w") as file:
                    file.writelines(todos)  # Write the updated list to the file

                print("Todo completed and removed successfully.")
            except (IndexError, ValueError):
                # Catch errors if the input number is invalid or out of range
                print("Invalid input: Please enter a valid todo number.")
                
        case "exit":
            # Case for exiting the program
            print("Exiting...")
            print("Goodbye!")
            break  # Exit the loop to end the program
        
        case _:
            # Handle any unrecognized actions
            print("Invalid action: Please choose from add, show, edit, complete, or exit.")
