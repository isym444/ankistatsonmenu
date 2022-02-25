import json
import urllib.request
import pickle
import easygui


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


""" 
a = ["one", "two", "test"]
save_object(MyClass(a))
obj = load_object("data.pickle")

print(obj.param)
 """


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(urllib.request.urlopen(urllib.request.Request("http://localhost:8765", requestJson)))
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


""" invoke("createDeck", deck="test1") """


""" def curanki():
    Japanese = len(invoke("findCards", query='"deck:2 日本語" is:due'))
    Deutsch = len(invoke("findCards", query='"deck:0 Deutsch" is:due'))
    Programming = len(invoke("findCards", query='"deck:0 Programming::0 CP Past Problem Tricks" is:due'))
    Español = len(invoke("findCards", query='"deck:3 Español (Audible)" is:due'))
    医学 = len(invoke("findCards", query='"deck:1 医学::MTW deck" is:due'))
    return (Japanese, Deutsch, Programming, Español, 医学)
 """
""" import sys

sys.path.insert(0, "/Users/isym444/rumps")
from rumps import rumps """

import rumps

collection = []
""" save_object(MyClass(collection)) """


class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        """temp = curanki()
        a = "Japanese: {} Deutsch: {} Programming: {} Español: {} 医学: {}".format(
            temp[0], temp[1], temp[2], temp[3], temp[4]
        )"""
        """ self.icon= """
        collection = load_object("data.pickle").param
        if len(collection) > 0:
            finaltitle = ""
            for x in collection:
                finaltitle += x
                finaltitle += ": "
                finaltitle += str(len(invoke("findCards", query='"deck:{}" is:due'.format(x))))
                finaltitle += " "
            super(AwesomeStatusBarApp, self).__init__(finaltitle)
        else:
            super(AwesomeStatusBarApp, self).__init__("Start by adding your first deck!")

    """ @rumps.clicked("Update")
    def test(self, _):
        temp = curanki()
        a = "Japanese: {} Deutsch: {} Programming: {} Español: {} 医学: {}".format(
            temp[0], temp[1], temp[2], temp[3], temp[4]
        )
        self.title = a """

    @rumps.clicked("Add decks")
    def test2(self, sender):
        collection = load_object("data.pickle").param
        window = rumps.Window(
            "If you want to add multiple items, separate these using a semicolon i.e. ;",
            "Add another deck to menu bar display.",
        )
        """ window.default_text = "testing!" """
        """ window.icon = self.icon """
        response = window.run()
        """ temp = curanki() """
        """ finding = len(invoke("findCards", query='"deck:{}" is:due'.format(response.text))) """
        """ a = "Japanese: {} Deutsch: {} Programming: {} Español: {} 医学: {}".format(
            temp[0], temp[1], temp[2], temp[3], temp[4]
        ) """
        if response.text != "":
            y = response.text.split(";")
            for z in y:
                collection.append(z)
            save_object(MyClass(collection))
        finaltitle = ""
        for x in collection:
            finaltitle += x
            finaltitle += ": "
            finaltitle += str(len(invoke("findCards", query='"deck:{}" is:due'.format(x))))
            finaltitle += " "
        """ print(finaltitle) """
        """ self.title = "{}: {}".format(response.text, finding) """
        self.title = finaltitle

    @rumps.clicked("Remove decks")
    def test3(self, sender):
        collection = load_object("data.pickle").param
        window = rumps.Window(
            "If you want to add multiple items, separate these using a semicolon i.e. ;",
            "Remove a deck from the menu bar display.",
        )
        """ window.icon = self.icon """
        response = window.run()
        y = response.text.split(";")
        for z in y:
            collection.remove(z)
        save_object(MyClass(collection))
        finaltitle = ""
        for x in collection:
            finaltitle += x
            finaltitle += ": "
            finaltitle += str(len(invoke("findCards", query='"deck:{}" is:due'.format(x))))
            finaltitle += " "
        """ print(finaltitle) """
        """ self.title = "{}: {}".format(response.text, finding) """
        self.title = finaltitle

    @rumps.clicked("Remove all")
    def test4(self, sender):
        """collection = load_object("data.pickle").param"""
        """ window.icon = self.icon """
        window = rumps.Window("Type yes if you are sure you want to delete all decks")
        """ window.icon = self.icon """
        response = window.run()
        y = response.text
        if y == "yes":
            collection = []
            save_object(MyClass(collection))
            finaltitle = ""
            """ print(finaltitle) """
            """ self.title = "{}: {}".format(response.text, finding) """
            super(AwesomeStatusBarApp, self).__init__("Start by adding your first deck!")

    @rumps.timer(30)
    def prefs(self, _):
        collection = load_object("data.pickle").param
        finaltitle = ""
        for x in collection:
            finaltitle += x
            finaltitle += ": "
            finaltitle += str(len(invoke("findCards", query='"deck:{}" is:due'.format(x))))
            finaltitle += " "
        """ print(finaltitle) """
        """ self.title = "{}: {}".format(response.text, finding) """
        self.title = finaltitle


if __name__ == "__main__":
    AwesomeStatusBarApp().run()

""" rm -rf build dist """
""" python3 setup.py py2app  """
"2 日本語;0 Deutsch;0 Programming::0 CP Past Problem Tricks;3 Español (Audible);1 医学::MTW deck"
