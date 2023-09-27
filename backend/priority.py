#strategy class

class Priority:
    def __init__(self, priotype):
        self.__priotype = priotype

    def set_priority(self):
        pri = self.__priotype.prioset()
        return pri