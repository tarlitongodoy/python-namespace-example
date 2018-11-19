

class SomeClass:
    def __init__(self, a=10):
        self.a = a

    def some_method(self, b=5):
        return self.a + b * 2


some_instance = SomeClass()
