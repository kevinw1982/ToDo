todos = []

while True:
    user_action = input("Type Add, Show, Edit or Exit: ")
    user_action = user_action.strip()
    user_action = user_action.capitalize()
    match user_action:
        case 'Add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'Edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1
            todos[number]
            new_todo = input("Enter new todo")
            todos[number] = new_todo
        case 'Show':
            for item in todos:
                print(item)
        case 'Exit':
            break

print("Bye")
