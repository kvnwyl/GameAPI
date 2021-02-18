from bottle import Bottle


class Server(object):
    """Base class to house common features for RestAPI.

    args:
        host : str : optional
            Host URI of the server.
        port : int : optional
            Port to host server on.
        reloader : bool
            Flag for Bottle to enable dynamic reloading of resources.
        runable : bool
            Flag to allow us to create a separate bottle instance for
            child classes whilst avoiding host / port conflicts.
    """

    def __init__(self, host="localhost", port=8080, reloader=False, runable=True):
        if runable:
            self._hostname = host
            self._port = port
            self._reloader = reloader

        self._app = Bottle()

    def mount(self, url_route, view_class):
        """method to bind class to a URL resource enabling
        separation of routes to individual files.

        args:
            url_route : str
                The URL base resource to access routes in the
                mounted class.
            view_class : str
                The class to search for routes when the url_route
                is called in a request.
        """
        self._app.route(url_route, view_class)

    def start(self):
        """Call the standard bottle framework to start
        the bottle server.
        """
        self._app.run(
            host=self._hostname,
            port=self._port,
            reloader=self._reloader)