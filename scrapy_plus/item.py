class item(object):
    def __init__(self, data):
        self.data = data
    @property
    def data(self):
        return self.__data