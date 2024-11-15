import todos_cli
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=todos_cli.read_from_todos(),
                      key="items", 
                      enable_events=True,
                      size=[45, 10])

edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True: 
    event, values = window.read()
    print(event, values)
    
    match event:
        case "Add":
            todos = todos_cli.read_from_todos()
            new_todo = values["todo"]  + "\n"
            todos.append(new_todo)
            todos_cli.write_to_todos(todos)
            
        case "Edit":
            todo_to_edit = values["items"][0]
            new_todo = values["todo"]
            
            todos = todos_cli.read_from_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todos_cli.write_to_todos(todos)
            window["items"].update(values=todos)
            
        case "todos":
            window["todo"].update(value=values["todos"][0])
            
        case sg.WIN_CLOSED:
             break
    
window.close()
