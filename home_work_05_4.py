def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid arguments. Usage: add [name] [phone_number]"
        except IndexError:
             return "Not enough arguments provided."
    
    return inner

@input_error
def add_contact(args, contacts):
    """
    Додає контакт у словник.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Змінює номер телефону для вказаного імені.
    """
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного імені.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(args, contacts):
    """
    Показує всі контакти.
    """
    if contacts:
        return "\n".join([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
    else:
        return "No contacts found."

def parse_input(user_input):
    """
    Функція розбирає введений користувачем рядок на команду та її аргументи.
    """
    parts = user_input.split()
    command = parts[0].lower()  # перша частина рядка - команда
    args = parts[1:]  # решта частин рядка - аргументи
    return command, args

def main():
    """
    Основна функція, що управляє циклом обробки команд.
    """
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command == "exit" or command == "close":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
