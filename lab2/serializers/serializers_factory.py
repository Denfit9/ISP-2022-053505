from serializers import serializer_universal, json_serializer, yaml_serializer, toml_serializer


class SerializerCreator:

    def create_serializer(self) -> serializer_universal.Serializer:
        """method that creates different types of serializers"""


class JSONSerializerCreator(SerializerCreator):
    """Creating JSONSerializer"""
    def create_serializer(self) -> serializer_universal.Serializer:
        return json_serializer.JSONSerializer()


class YAMLSerializerCreator(SerializerCreator):
    """Creating YAMLSerializer"""
    def create_serializer(self) -> serializer_universal.Serializer:
        return yaml_serializer.YAMLSerializer()


class TOMLSerializerCreator(SerializerCreator):
    """Creating TOMLSerializer"""
    def create_serializer(self) -> serializer_universal.Serializer:
        return toml_serializer.TOMLSerializer()
