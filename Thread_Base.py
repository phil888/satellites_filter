from threading import Thread


class Thread_Base:
    def start(self):
        self.__thread.start()

    def join(self):
        self.__thread.join()

    def forceStop(self):
        self.__thread.join(5)

    def __init__(self, threadFunction):
        self.__thread = Thread(target=threadFunction)
