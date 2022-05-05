import toml
from serializers.serializer_universal import Serializer
from serializers import general_serializer


class TOMLSerializer(Serializer):

    def dumps(self, obj):
        """Overriding dumps method to be used in TOML"""
        return toml.dumps(general_serializer.serialize(obj))

    def loads(self, path):
        """Overriding loads method to be used in TOML"""
        return general_serializer.deserialize(toml.loads(path))
