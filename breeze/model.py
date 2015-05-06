import abc


class ResourceModel(metaclass=abc.ABCMeta):

    @classmethod
    def default_resource_name(cls):
        return cls.name.lower() + 's'

    @abc.abstractclassmethod
    def load(cls, pk):
        pass

    @abc.abstractclassmethod
    def create(cls, **kwargs):
        pass

    @abc.abstractclassmethod
    def list(cls, filter_options):
        pass

    @abc.abstractmethod
    def save(cls, pk):
        pass

    @abc.abstractmethod
    def update(cls, pk):
        pass
