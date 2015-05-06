import re
import abc

from tornado.web import RequestHandler

from breeze.filter import FilterOptions


class _ResourceMeta(abc.ABCMeta):
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        if bases == (RequestHandler, ):
            return

        options = getattr(cls, 'Meta', object())

        cls.name = getattr(options, 'name', cls.__name__.lower() + 's')
        cls.url_regex = r'/{}(?:/(?P<pk>[^/]+))?/?$'.format(re.escape(cls.name))


class Resource(RequestHandler, metaclass=_ResourceMeta):
    # def __init__(self, model, name=None):
    #     self._model = model
    #     self._name = name or model.default_resource_name()

    # @abc.abstractclassmethod
    def load(self, pk):
        pass

    # @abc.abstractclassmethod
    def list(self, filter_options):
        pass

    # @abc.abstractclassmethod
    def delete(self, instance):
        pass

    # @abc.abstractclassmethod
    def update(self, instance, **data):
        pass

    # @abc.abstractclassmethod
    def create(self, **data):
        pass

    def get(self, pk=None):
        if pk is not None:
            self.write(self.load(pk).to_json())
            return

        self.write({
            'data': [
                x.to_json() for x in
                self.list(self._parse_filter_options())
            ]
        })

    def post(self, pk=None):
        assert pk is None

    def _parse_filter_options(self):
        return FilterOptions()
