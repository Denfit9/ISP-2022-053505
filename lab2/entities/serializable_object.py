class Boozer:
    """serializing class"""

    def __init__(self, liters=99, name="Ivan", status="Boozer") -> None:
        self.liters = liters
        self.name = name
        self.status = status

    liters: int
    name: str
    status: str

    def booze(self):
        print("Noice! Feels good now")

    def return_liters(self):
        return self.liters

    def return_name(self):
        return self.name

    def return_status(self):
        return self.status


boozer_object = Boozer()
"""creating object of class"""
