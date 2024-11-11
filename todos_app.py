todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ").strip().capitalize()
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos, 1):
                print(f"{index}: {item}")
        case "edit":
            try:
                number = int(input("Enter the number of the todo to edit: "))
                new_todo = input("Enter new todo: ").strip().capitalize()
                todos[number-1] = new_todo
            except Exception as error:
                print("Invalid input")
                
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
            
        case "exit":
            print("Exiting...")
            print("Goodbye!")
            break
        
            

