import math
import os

from entities import serializable_object
from entities import serializable_functions
from serializers import yaml_serializer
"""Testing yaml"""


def test_dump_load():
    serialz = yaml_serializer.YAMLSerializer()
    file = open("example.yaml", "w")
    serialz.dump(serializable_functions.f, file.name)
    func = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert math.sin(42 * 123 * 1) == func(1)


def test_dump_load2():
    serialz = yaml_serializer.YAMLSerializer()
    file = open("example.yaml", "w")
    serialz.dump(serializable_functions.sum_of_two, file.name)
    func = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 2 + 3 == func(2, 3)


def test_dump_load_object():
    serialz = yaml_serializer.YAMLSerializer()
    file = open("example.yaml", "w")
    serialz.dump(serializable_object.boozer_object, file.name)
    obj = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.name == 'Ivan'
