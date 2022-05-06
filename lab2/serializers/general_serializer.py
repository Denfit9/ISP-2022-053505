import builtins
import importlib
import sys
import types
from inspect import getmodule


def serialize(obj) -> any:
    """Creating serialized dictionary"""
    if isinstance(obj, int | str | types.NoneType):
        return obj
    elif isinstance(obj, tuple):
        return {"tuple": serialize_elements(obj)}
    elif isinstance(obj, list):
        return {"list": serialize_elements(obj)}
    elif isinstance(obj, dict):
        return {"dict": obj}
    elif isinstance(obj, bytes):
        return {"bytes": obj.hex()}
    elif isinstance(obj, types.MappingProxyType):
        return serialize_dict_obj(obj)
    elif isinstance(obj, types.CodeType):
        return {"code": serialize_attributes(obj)}
    elif isinstance(obj, types.FunctionType):
        return {"func": serialize(obj.__code__)}
    elif isinstance(obj, type):
        return serialize_type_obj(obj)
    if (getmodule(type(obj)).__name__ in sys.builtin_module_names or
            getmodule(type(obj)).__name__ == 'importlib._bootstrap'):
        return None
    else:
        obj_dict = serialize(obj.__dict__)
        obj_type = serialize(type(obj))
        return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}


def serialize_elements(obj) -> dict[str, any]:
    elements = dict()
    for i in range(len(obj)):
        elements[f"el{i}"] = serialize(obj[i])
    return elements


def serialize_dict_obj(obj):
    object_dict = dict(obj)
    for key in object_dict.keys():
        object_dict[key] = serialize(object_dict[key])
    return object_dict


def serialize_type_obj(obj):
    attributes_dict = dict(obj.__dict__)
    for key in attributes_dict.keys():
        attributes_dict[key] = serialize(attributes_dict[key])
    attributes_dict['__annotations__'] = None
    return {"type": {"name": obj.__name__, "attribs": attributes_dict}}


def serialize_attributes(obj) -> dict[str, any]:
    elements = dict()
    pub_attributes = list(
        filter(lambda item: not item.startswith('_'), dir(obj)))
    for attr in pub_attributes:
        elements[attr] = serialize(obj.__getattribute__(attr))
    return elements


def deserialize_code_type(value):
    return types.CodeType(
        deserialize(value["co_argcount"]),
        deserialize(value["co_posonlyargcount"]),
        deserialize(value["co_kwonlyargcount"]),
        deserialize(value["co_nlocals"]),
        deserialize(value["co_stacksize"]),
        deserialize(value["co_flags"]),
        deserialize(value["co_code"]),
        deserialize(value["co_consts"]),
        deserialize(value["co_names"]),
        deserialize(value["co_varnames"]),
        "deserialized",
        deserialize(value["co_name"]),
        deserialize(value["co_firstlineno"]),
        deserialize(value["co_lnotab"]),
        deserialize(value["co_freevars"]),
        deserialize(value["co_cellvars"])
    )


def deserialize_object_type(value):
    obj_type = deserialize(value['obj_type'])
    obj_dict = deserialize(value['obj_dict'])
    try:
        obj = object.__new__(obj_type)
        obj.__dict__ = obj_dict
        for (key, value) in obj_dict.items():
            setattr(obj, key, value)
    except TypeError:
        obj = None
    return obj


def deserialize_function_type(value):
    import __main__
    globals().update(__main__.__dict__)

    def func():
        pass

    func.__code__ = deserialize(value)
    for name in func.__code__.co_names:
        if builtins.__dict__.get(name, 42) == 42:
            try:
                builtins.__dict__[name] = importlib.import_module(name)
            except ModuleNotFoundError:
                builtins.__dict__[name] = 42
    return func


def deserialize_type_obj(value):
    import __main__
    globals().update(__main__.__dict__)

    obj_type = getattr(__main__, value['name'], None)
    serialize(obj_type)

    attributes = value['attribs']
    for key in attributes.keys():
        attributes[key] = deserialize(attributes[key])

    obj_type = type(
        value['name'],
        (object,),
        attributes
    )

    return obj_type


def deserialize_tuple_type(value):
    if value is None:
        return ()
    return tuple([deserialize(element) for element in value.values()])


def deserialize(obj: dict[str, any]):
    """Deserializing dictionary"""
    if not isinstance(obj, dict):
        return obj

    for (key, value) in obj.items():
        if key == 'tuple':
            return deserialize_tuple_type(value)
        elif key == 'list':
            return [deserialize(element) for element in value.values()]
        elif key == 'dict':
            return value
        elif key == 'bytes':
            return bytes.fromhex(value)
        elif isinstance(value, int | float | str):
            return value
        elif key == 'type':
            return deserialize_type_obj(value)
        elif key == 'func':
            return deserialize_function_type(value)
        elif key == 'code':
            return deserialize_code_type(value)
        elif key == 'object':
            return deserialize_object_type(value)
