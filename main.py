from classes import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please"
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_birthday(birthday)
    return 'Birthday added'


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone,new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    phone = args[0]
    record = book.find(phone)
    return '; '.join(str(phone) for phone in record.phones)

@input_error   
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return record.birthday

@input_error
def show_all(book: AddressBook):
    return book

def show_all_birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()




def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_all_birthdays(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book)) 



        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
