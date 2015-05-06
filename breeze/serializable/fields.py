import abc


class BaseSerializableField(abc.ABC):
    default_value = None

    def __init__(self, default=None):
        self._value = default or self.__class__.default_value

    @property
    def value(self):
        return self._value

    def getter(self, model):
        return self.value

    def setter(self, model, value):
        self._value = value

    def to_dict(self):
        return self.value

    def to_json(self):
        return self.value


class StringField(BaseSerializableField):
    pass


class IntegerField(BaseSerializableField):
    def setter(self, model, value):
        self._value = int(value)


class DateTimeField(BaseSerializableField):

    def to_json(self):
        return self.value.isoformat()
