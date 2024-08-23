import asyncio
import os


class Store:

  def __init__(self):
    self.local = os.path.join(os.path.dirname(__file__), "../storage/")

  def createStore(self, name):
    if not os.path.exists(f"{self.local}{name}.json"):
      open(f"{self.local}{name}.json", "w").write("{}")
    else:
      return FileExistsError()

  def getStore(self, name):
    if os.path.exists(f"{self.local}{name}.json"):
      return open(f"{self.local}{name}.json", "r").read()
    else:
      return FileNotFoundError()

  def writeStore(self, name, data):
    if os.path.exists(f"{self.local}{name}.json"):
      open(f"{self.local}{name}.json", "a").write(data)
    else:
      return FileNotFoundError()

  def deleteStore(self, name):
    os.remove(f"{self.local}{name}.json")

  async def cacheStore(self, name, data, time, canDelete):
    self.writeStore(name, data)
    await asyncio.sleep(time)
    if canDelete:
      os.remove(f"{self.local}{name}.json")
    else:
      open(f"{self.local}{name}.json", "w").write("{}")


def use_store():
  return Store()
