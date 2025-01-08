todos = []

while True:
    user_action = input("Type Add, Show or Exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'Add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'Show':
            for item in todos:
                print(item)
        case 'Exit':
            break

print("Bye")
