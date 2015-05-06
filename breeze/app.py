import logging
import logging.config

import tornado.web
import tornado.ioloop

from breeze import settings

logger = logging.getLogger(__name__)
logging.config.dictConfig(settings.DEFAULT_LOGGING_CONFIG)


class App:
    def __init__(self, *resources, port=8080, prefix='/', **kwargs):
        self._port = port
        self._prefix = prefix

        self.tornado_app = tornado.web.Application([
            self.resource_to_url(resource)
            for resource in resources
        ], **kwargs)

    def resource_to_url(self, resource):
        return tornado.web.url(
            self._prefix + resource.url_regex.lstrip('/'),
            resource,
            name=resource.name
        )

    def serve(self):
        logging.info('Listening on port {}'.format(self._port))
        self.tornado_app.listen(self._port)
        tornado.ioloop.IOLoop.instance().start()
