class A:
    def __init__(self):
        super().__init__
        self.propl="propl"

class B:
    def __init__(self):
        super().__init__()
        self.prop2="prop2"

class C(A, B):
    def __init__(self):
        super().__init__()