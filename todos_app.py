def read_from_todos():
    # Open the file in read mode to get the current list of todos
    with open("todos.txt", "r") as file:
        words = file.readlines()  # Read all lines (todos) into a list
    return words

        
def write_to_todos(todos):
    # Open the file in write mode and save the updated todo list back to the file
    with open("todos.txt", "w") as file:
        words = file.writelines(todos)  # Write the updated list to the file
        return  words
    
    
def add_todos():
    # Prompt the user to enter a new todo, capitalize it, and add a newline
    todo = input("Enter a todo: ").strip().capitalize() + "\n"
    
    todos = read_from_todos() # Call the open todos function and store in a variable todos
        
    # Append the new todo to the list of todos
    todos.append(todo)
    
    todos = write_to_todos(todos) # Pass the updated todos list as argument in the write_todos function
 
        
def view_todos():
    todos = read_from_todos() # Call the open todos function and store in a variable todos

    # Remove newline characters from each item for a cleaner display
    new_todos = [item.strip("\n") for item in todos]
    
    # Loop through todos with an index starting from 1 and display each
    for index, item in enumerate(new_todos, 1):
        print(f"{index}: {item}")
   
        
def edit_todos():
    try:
        # Ask the user for the number of the todo to edit and convert to an integer
        number = int(input("Enter the number of the todo to edit: "))
        
        # Prompt the user for the new todo text
        new_todo = input("Enter new todo: ").strip().capitalize() + "\n"
        
        todos = read_from_todos() # Call the open todos function and store in a variable todos
        # Update the specified todo with the new text
        
        todos[number - 1] = new_todo  # Adjust by -1 for zero-based index
        # Open the file in write mode and save the updated todo list
        
        todos = write_to_todos(todos) # Pass the updated todos list as argument in the write_todos function

        print("Todo updated successfully.")
    except Exception as error:
        # Catch errors if the input number is invalid or out of range
        print("Error:",error,"\nPlease, enter a valid todo number.")
 
        
def delete_todos():
    try:
        # Ask the user for the number of the todo to mark as complete
        number = int(input("Number of the todo to complete: "))
        
        todos = read_from_todos() # Call the open todos function and store in a variable todos
        
        # Remove the specified todo from the list
        removed_todo = todos.pop(number - 1)  # Adjust by -1 for zero-based index
        
        todos = write_to_todos(todos) # Pass the updated todos list as argument in the write_todos function

        print(f"Todo {removed_todo.strip("\n")} removed successfully.")
    except Exception as error:
        # Catch errors if the input number is invalid or out of range
        print("Error:",error,"\nPlease, enter a valid todo number.")
 
        
def exit_app():
    print("Exiting...Goodbye!")
    

def run_app():
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
            choice = int(input("\nEnter your choice: ")) # Ask the user for an action 
            
            # Match the user's action to different cases
            match choice:
                case 1:
                    # Case for adding a new todo item
                    add_todos()
                    
                case 2:
                    # Case for displaying all todo items
                    view_todos()
                            
                case 3:
                    # Case for editing an existing todo item
                    edit_todos()
                        
                case 4:
                    # Case for marking a todo as complete (removing it from the list)
                    delete_todos()    
                        
                case 5:
                    # Case for exiting the program
                    exit_app()
                    break # Exit the loop to end the program
                
                case _:
                    # Handle any unrecognized actions
                    print("Invalid choice: Please enter number from 1 to 5.")
                    
                    
        except Exception as error:
            print("Error:",error,"\nPlease, enter a valid numeric choice.")
            
            
if __name__ == "__main__":
    run_app()
    
    