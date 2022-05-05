import math
import os

from entities import serializable_object
from entities import serializable_functions
from serializers import toml_serializer

"""Testing toml"""


def test_dump_load_object():
    serialz = toml_serializer.TOMLSerializer()
    file = open("example.toml", "w")
    serialz.dump(serializable_object.boozer_object, file.name)
    obj = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.name == 'Ivan'


def test_dump_load_object2():
    serialz = toml_serializer.TOMLSerializer()
    file = open("example.toml", "w")
    serialz.dump(serializable_object.boozer_object, file.name)
    obj = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.liters == 99


def test_dump_load_function():
    serialz = toml_serializer.TOMLSerializer()
    file = open("example.toml", "w")
    serialz.dump(serializable_functions.sum_of_two, file.name)
    func = serialz.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 2 + 3 == func(2, 3)
