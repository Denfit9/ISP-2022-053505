from serializers import general_serializer
from serializers.serializer_universal import Serializer


class JSONSerializer(Serializer):

    def dumps(self, obj):
        """Overriding dumps method to be used in JSON"""
        return self.create_json_str(general_serializer.serialize(obj))

    def loads(self, path):
        """Overriding loads method to be used in JSON"""
        null = None
        return general_serializer.deserialize(eval(path))

    def create_json_str(self, obj):
        """Creating a string according to JSON"""
        if isinstance(obj, dict):
            strings = list()
            for key, value in obj.items():
                strings.append(f'{self.create_json_str(key)}:{self.create_json_str(value)},')
            return f"{{{''.join(strings)[:-1]}}}"
        elif isinstance(obj, str):
            strng = obj.translate(str.maketrans({
                "\"": r"\"",
                "\\": r"\\",
            }))
            return f"\"{strng}\""
        elif obj is None:
            return 'null'
        else:
            return str(obj)
