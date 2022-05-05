import yaml
from serializers.serializer_universal import Serializer
from serializers import general_serializer


class YAMLSerializer(Serializer):

    def dumps(self, obj):
        """Overriding dumps method to be used in YAML"""
        return yaml.dump(general_serializer.serialize(obj))

    def loads(self, path):
        """Overriding loads method to be used in YAML"""
        return general_serializer.deserialize(yaml.safe_load(path))
