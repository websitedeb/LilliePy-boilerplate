import os


class Store:

  def __init__(self):
    self.local = os.path.join(os.path.dirname(__file__), "../storage/")

  def createStore(self, name):
    open(f"{self.local}{name}.json", "w").write("{}")

  def getStore(self, name):
    return open(f"{self.local}{name}.json", "r").read()

  def writeStore(self, name, data):
    open(f"{self.local}{name}.json", "w").write(data)

  def deleteStore(self, name):
    os.remove(f"{self.local}{name}.json")


def use_store():
  return Store()
