import json
import urllib.request
import pickle
import easygui
from collections.abc import Mapping


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

import rumps


collection = []


class AwesomeStatusBarApp(rumps.App):
    def popup():
        myvar = easygui.enterbox("What deck do you want to add?")

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
        popup()
        if myvar != "":
            collection.append(myvar)
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
        """ window = rumps.Window(f"Current:", "Remove a deck from the menu bar display") """
        """ window.icon = self.icon """
        """ response = window.run() """
        myvar = easygui.enterbox("What, is your favorite color?")
        collection.remove(myvar)
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
