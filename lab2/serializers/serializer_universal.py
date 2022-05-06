class Serializer:
    """Methods that will be used in each of serializer to serialize what we need"""

    def dump(self, item: any, filename: str):
        """Serializing Python object into file"""
        file = open(filename, 'w')
        file.write(self.dumps(item))

    def dumps(self, item: any) -> str:
        """Serializing Python object to string"""

    def load(self, filename: str):
        """Deserializing Python object from file"""
        file = open(filename, 'r')
        return self.loads(file.read())

    def loads(self, string: str) -> any:
        """Deserializing Python object from string"""
