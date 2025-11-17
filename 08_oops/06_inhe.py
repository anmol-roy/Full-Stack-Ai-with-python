class BaseChai:
    def __init__(self, type_):
        self.type = type_


    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding Cardamon, Ginger, Cloves")

class chaishop:
    chai_cls = BaseChai