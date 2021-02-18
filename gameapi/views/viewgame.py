from gameapi.classes.server import Server
from gameapi.tables.game import Game
from bottle import request
from sqlalchemy import func
from datetime import datetime


class ViewGame(Server):
    """Bottle view created to house all routes related to
    the /game url route.
    """

    def __init__(self, DBSession):
        super().__init__(runable=False)

        self.session = DBSession

        # Routes to retrieve data

        self._app.route(
            "/count",
            method="GET",
            callback=self.count_games
            )

        self._app.route(
            "/id/<id>",
            method="GET",
            callback=lambda id: self.query_data("id", id)
            )

        self._app.route(
            "/name/<name>",
            method="GET",
            callback=lambda name: self.query_data("name", name)
            )

        self._app.route(
            "/genre/<genre>",
            method="GET",
            callback=lambda genre: self.query_data("genre", genre)
            )

        self._app.route(
            "/series/<series>",
            method="GET",
            callback=lambda series: self.query_data("series", series)
            )

        self._app.route(
            "/console/<console>",
            method="GET",
            callback=lambda console: self.query_data("console", console)
            )

        self._app.route(
            "/rating/<rating>",
            method="GET",
            callback=lambda rating: self.query_data("rating", rating)
            )

        self._app.route(
            "/recent",
            method="GET",
            callback=lambda: self.get_top("last_played", order_amount=1)
            )

        self._app.route(
            "/recent/<order_amount>",
            method="GET",
            callback=lambda order_amount: self.get_top(
                "last_played", order_amount
                )
            )

        self._app.route(
            "/favourite",
            method="GET",
            callback=lambda: self.get_top("rating", order_amount=1)
            )

        self._app.route(
            "/favourite/<order_amount>",
            method="GET",
            callback=lambda order_amount: self.get_top("rating", order_amount)
        )

        # Routes to create data

        self._app.route(
            "/",
            method="POST",
            callback=self.create_data
            )

        # Routes to update data

        self._app.route(
            "/id/<id>",
            method="PATCH",
            callback=lambda id: self.update_data(id)
            )

        # Routes to delete data

        self._app.route(
            "/id/<id>",
            method="DELETE",
            callback=lambda id: self.delete_data(id)
            )

    def query_data(self, column, value):
        """Query game from the database where the specified
        column equals the value.

        args:
            column : str
                The column in the database / the attribute of the
                Game class to filter by.
            value : str
                The value needed to match.

        return:
            dict
                return dict where the key is the ID and the
                value is a dict representation of the object.

        Note:
            This is the equivalent to performing a sql SELECT
            with a WHERE clause.
        """

        session = self.session()
        response = {"status": "", "message": ""}

        try:
            query_games = session.query(Game).filter(
                getattr(Game, column) == value)
            response["status"] = "200"
            response["message"] = {
                game.id: game.to_json() for game in query_games
                }
        finally:
            session.close()

        # Return game in dictionary with ID as key and dict representation
        # of object as value.
        return response

    def create_data(self):
        """Create new row based on data passed in request.

        args:
            None

        return:
            dict
                dictionary detailing status of request and message.

        notes:
            Data is created based on the content of the request
            from the client.
        """

        session = self.session()
        creation_params = {}

        for key, value in request.json.items():
            if str(getattr(Game, key).type) == "DATETIME":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            creation_params[key] = value

        game = Game(**creation_params)
        response = {"status": "", "message": ""}

        # Bare exception used to catch any DB errors.
        try:
            session.add(game)
            session.commit()
            response["status"] = "200"
            response["message"] = "success"
        except Exception as e:
            session.rollback()
            response["status"] = "500"
            response["message"] = "An error occurred: {}".format(e)
        finally:
            session.close()

        return response

    def update_data(self, id):
        """Update ID passed in with the content of the JSON
        request.

        args:
            id : int
                The ID of the record to update.

        return:
            dict
                dictionary detailing status of request and message.
        """

        session = self.session()
        response = {"status": "", "message": ""}

        # Retrieve the single game where the ID matches.
        game = session.query(Game).filter(Game.id == id).one()

        for key, value in request.json.items():
            # Validation for DATETIME objects.
            # Note: The field type needs to be cast as a str
            # to ensure that the condition matches.
            if str(getattr(Game, key).type) == "DATETIME":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            setattr(game, key, value)

        # Bare exception used to catch any DB errors.
        try:
            session.commit()
            response["status"] = "200"
            response["message"] = "success"
        except Exception as e:
            session.rollback()
            response["status"] = "500"
            response["message"] = "An error occurred: {}".format(e)
        finally:
            session.close()

        return response

    def delete_data(self, id):
        """Delete the row which matches the ID supplied

        args:
            id : int
                The ID of the record to delete.

        return:
            dict
                dictionary detailing status of request and message.
        """

        session = self.session()
        response = {"status": "", "message": ""}

        # Select the record and delete.
        session.query(Game).filter(Game.id == id).delete()

        # Bare exception used to catch any DB errors.
        try:
            session.commit()
            response["status"] = "200"
            response["message"] = "success"
        except Exception as e:
            session.rollback()
            response["status"] = "500"
            response["message"] = "An error occurred: {}".format(e)
        finally:
            session.close()

        return response

    def count_games(self):
        """Get a count of all games in the db.

        return:
            dict
                return dict where key is constant string and
                value is the count.
        """

        session = self.session()
        response = {"status": "", "message": ""}

        try:
            game_count = session.query(func.count(Game.id)).scalar()
            response["status"] = "200"
            response["message"] = {"game_count": game_count}
        finally:
            session.close()

        return response

    def get_top(self, column, order_amount):
        """Retrieve results based on the column value and order_amount
        specified.

        args:
            column : str
                The column to order by.
            order_amount : int
                The amount of rows to return.

        returns:
            dict
                return dict where the key is the ID of the game and the
                value is a dict representation of the object.
        """

        session = self.session()
        response = {"status": "", "message": ""}

        try:
            query_games = session.query(Game).order_by(
                getattr(Game, column).desc()
                ).limit(order_amount)

            response["status"] = "200"
            response["message"] = {
                    game.id: game.to_json() for game in query_games
                }
        finally:
            session.close()

        return response
