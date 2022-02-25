import pickle


class MyClass:
    def __init__(self, param):
        self.param = param


def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


a = ["one", "two", "test"]
save_object(MyClass(a))
obj = load_object("data.pickle")

print(obj.param)
