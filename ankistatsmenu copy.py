import json
import urllib.request


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


def curanki():
    Japanese = len(invoke("findCards", query='"deck:2 日本語" is:due'))
    Deutsch = len(invoke("findCards", query='"deck:0 Deutsch" is:due'))
    Programming = len(invoke("findCards", query='"deck:0 Programming::0 CP Past Problem Tricks" is:due'))
    Español = len(invoke("findCards", query='"deck:3 Español (Audible)" is:due'))
    医学 = len(invoke("findCards", query='"deck:1 医学::MTW deck" is:due'))
    return (Japanese, Deutsch, Programming, Español, 医学)


import rumps

collection = []


class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        """temp = curanki()
        a = "Japanese: {} Deutsch: {} Programming: {} Español: {} 医学: {}".format(
            temp[0], temp[1], temp[2], temp[3], temp[4]
        )"""
        """ self.icon= """
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
        window = rumps.Window(f"Current:", "Add another deck to menu bar display")
        """ window.icon = self.icon """
        response = window.run()
        """ temp = curanki() """
        """ finding = len(invoke("findCards", query='"deck:{}" is:due'.format(response.text))) """
        """ a = "Japanese: {} Deutsch: {} Programming: {} Español: {} 医学: {}".format(
            temp[0], temp[1], temp[2], temp[3], temp[4]
        ) """
        if response.text != "":
            collection.append(response.text)
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
        window = rumps.Window(f"Current:", "Remove a deck from the menu bar display")
        """ window.icon = self.icon """
        response = window.run()
        collection.remove(response.text)
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
