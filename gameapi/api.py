import sqlalchemy

from sqlalchemy.orm import sessionmaker
from gameapi.classes.server import Server
from gameapi.tables import tablebase
from .views.viewgame import ViewGame


class API(Server):
    """Main class for the RestAPI which creates required server
    variables, prepares database and mounts all required routes
    from other files.
    """
    def __init__(self, host="localhost", port="8080", reloader=False):
        super().__init__(host, port, reloader)

        # Create initial connection to local db file.
        engine = sqlalchemy.create_engine("sqlite:///test_db.sqlite")

        # Create all tables if needed.
        tablebase.Base.metadata.create_all(engine)

        # Create DBSession
        DBSession = sessionmaker(bind=engine)

        # Create mount point of ViewGame class to be called when
        # /game is on the url.
        self._app.mount("/game", ViewGame(DBSession)._app)
