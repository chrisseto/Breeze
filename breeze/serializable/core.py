import abc
import json

from breeze.serializable import utils
from breeze.serializable import fields


class _SerializableMeta(abc.ABCMeta):
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        if bases == ():
            return

        cls._fields = {}

        for name, field in nmspc.items():
            if not isinstance(field, fields.BaseSerializableField):
                continue
            cls._fields[name] = field
            setattr(cls, name, property(field.getter, field.setter))


class Serializable(metaclass=_SerializableMeta):
    String = fields.StringField
    Integer = fields.IntegerField
    DateTime = fields.DateTimeField

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if name not in self._fields:
                raise AttributeError('{} has no attribute "{}"'.format(self.__class__.__name__, name))
            setattr(self, name, value)

    def to_dict(self):
        return {
            name: value.to_dict()
            for name, value in
            self._fields.items()
        }

    def to_json(self):
        return {
            utils.snake_to_camel(name): value.to_json()
            for name, value in self._fields.items()
        }

    def to_xml(self):
        pass
