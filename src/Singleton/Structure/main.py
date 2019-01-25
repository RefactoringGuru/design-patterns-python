class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise ReferenceError("Cannot instantiate a singleton class.")
        else:
            Singleton._instance = self


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
