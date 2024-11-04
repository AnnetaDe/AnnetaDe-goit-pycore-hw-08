import pickle
from task1_hw_07 import AddressBook


def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_from_pickle(file):
    try:

        with open(file, 'rb') as f:
            return pickle.load(f)

    except FileNotFoundError:
        return AddressBook()


file = "my_pickle_file.pkl"


def save_decorator(func):
    def inner(*args, **kwargs):
        return save_to_pickle(args[0], file)
    return inner


def load_decorator(func):
    def inner(*args, **kwargs):
        return func(load_from_pickle(args[0]), file, **kwargs)
    return inner
