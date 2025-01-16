todos = []

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
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
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'Complete':
            number = int(input("number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case 'Exit':
            break

print("Bye")
