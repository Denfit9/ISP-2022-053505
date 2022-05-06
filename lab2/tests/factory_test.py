from serializers.serializers_factory import *
"""Testing Factory file"""


def get_serializer(creator: SerializerCreator()):
    return creator.create_serializer()


def test_json_creator():
    """Testing json from fabric"""
    serialz = get_serializer(JSONSerializerCreator())
    assert isinstance(serialz, json_serializer.JSONSerializer)


def test_yaml_creator():
    """Testing yaml from fabric"""
    serialz = get_serializer(YAMLSerializerCreator())
    assert isinstance(serialz, yaml_serializer.YAMLSerializer)


def test_toml_creator():
    """Testing toml from fabric"""
    serialz = get_serializer(TOMLSerializerCreator())
    assert isinstance(serialz, toml_serializer.TOMLSerializer)
