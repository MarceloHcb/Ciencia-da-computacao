
def clear(self):
    self.head_value = None
    self.__length = 0

def clear(self):
    while not self.is_empty():
        self.remove_first()