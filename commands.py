from errors import input_error
from file_pickle import save_decorator
from helper_errors_classes import ArgsNotEnought, CustomKeyError,  CustomAlreadyExistsError
from task1_hw_07 import Birthday, Name, Phone, Record, AddressBook

my_address_book = AddressBook()


def normalize_input(user_input):
    return user_input.strip().lower()


@input_error
def parse_input(user_input):
    if not user_input:
        return None, None
    if " " not in user_input:
        return normalize_input(user_input), None
    cmd, *args = user_input.split()
    cmd = normalize_input(cmd)
    return cmd, *args

# use after all work done


def formatted_input(message="Pls follow the hint: "):
    inp = input(message).strip().lower()
    return inp


@input_error
def add_record() -> None:
    name = input("Enter a name: ")
    phone = input("Enter a phone number: ")
    birthday = input("Enter a birthday in format DD.MM.YYYY: ")
    record = Record(name, phone, birthday)
    my_address_book.add_record(record)


def all_contacts():
    print(my_address_book)


@input_error
def change_record_phone():
    name_of_contact = input("Enter a name of contact: ")
    new_phone = input("Enter a new phone number: ")
    my_address_book.change_record_phone(name_of_contact, new_phone)


@input_error
def add_phone():
    name_of_contact = input("Enter a name of contact: ")
    phone = input("Enter a phone number: ")
    changed_record = my_address_book.add_phone(name_of_contact, phone)

    print(changed_record)


def change_alias():
    name_of_contact = input("Enter a name of contact: ")
    alias = input("Enter a new alias: ")
    changed_record = my_address_book.change_alias(name_of_contact, alias)
    print(changed_record)


def change_record_name():
    name_of_contact = input("Enter a name of contact: ")
    new_name = input("Enter a new name: ")
    changed_record = my_address_book.change_record_name(
        name_of_contact, new_name)
    print(changed_record)


def phone():
    name_of_contact = input("Enter a name of contact: ")
    result = my_address_book.find_record(name_of_contact)
    print(result)


def show_record_phones():
    name_of_contact = input("Enter a name of contact: ")
    my_address_book.show_record_phones(name_of_contact)


def add_birthday():
    print("Enter a birthday in format DD.MM.YYYY")
    name_of_contact = input("Enter a name of contact: ")
    birthday = input("Enter a birthday: ")
    changed_record = my_address_book.add_birthday(name_of_contact, birthday)
    print(changed_record)


def show_birthday():
    name_of_contact = input("Enter a name of contact: ")
    birthday = my_address_book.show_birthday(name_of_contact)
    print(birthday)


def birthdays():
    birthdays = my_address_book.show_birthdays()
    print(birthdays)


def delete_record():
    name_of_contact = input("Enter a name of contact: ")
    my_address_book.delete_record(name_of_contact)
    print(f"Record {name_of_contact} was deleted")


def find_record():
    user_input = input(
        "if you want to find a record by name press 'n', if by phone press 'p', if you want to skip press Enter: ")
    if user_input == 'n':
        name = input("Enter a name of contact: ")
        result = my_address_book.find_record(name)
        print(result)
    elif user_input == 'p':
        phone = input("Enter a phone number: ")
        result = my_address_book.find_record_by_phone(phone)
        print(result)
    else:
        print("You skipped the search")
        return

    result = my_address_book.find_record(name)

    if result:
        print(f"Record {name} was found", result)


def execute_command(command):
    if command in ["close", "exit"]:
        print("Good bye!")
        return
    elif command == "hello":
        print("How can I help you?")
    elif command == "add":
        add_record()
    elif command == "all":
        all_contacts()
    elif command == 'all-phones':
        show_record_phones()
    elif command == "change":
        user_input = normalize_input(
            input("what do you want to change? name/phone/alias for phone(n/p/a):  "))
        if user_input == "n":
            change_record_name()
        elif user_input == "p":
            change_record_phone()
        elif user_input == "a":
            change_alias()
    elif command == "phone":
        phone()
    elif command == "find":
        name = input("Enter a name of contact: ")
        find_record(name)
    elif command == "show-birthday":
        show_birthday()
    elif command == "birthdays":
        birthdays()
    elif command == "add-b":
        add_birthday()
    elif command == 'add-p':
        add_phone()
    elif command == "del" or command == "delete":
        delete_record()

    elif command == "help":
        print("Commands: hello, add, all, change, phone, close, exit, help, add-b, show-birthday, birthdays",
              "del", "delete", "all-phones", "add-p", "add-b"),
