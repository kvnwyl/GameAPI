from sqlalchemy import Column, Sequence, Integer, String, Date, DateTime

from .tablebase import Base
from gameapi.tables import tablebase


class Game(Base):
    """Table to store data about game.
    """
    __tablename__ = "games"

    id = Column(Integer, Sequence("game_id_seq"), primary_key=True)
    name = Column(String, unique=True, nullable=False)
    region = Column(String, nullable=False)

    release_date = Column(DateTime)
    console = Column(String, nullable=False)
    series = Column(String)
    genre = Column(String)
    tags = Column(String)
    rating = Column(Integer)

    developer = Column(String)
    publisher = Column(String)

    play_count = Column(Integer)
    last_played = Column(DateTime)
    play_duration = Column(Integer)

    def __repr__(self):
        """String representation of object.
        """
        return "<Game ({}({}))>".format(self.name, self.region)

    def to_json(self):
        """Convert object to dictionary representation where
        keys are variable names and values are variable content.
        """
        return {
            attr:
            str(getattr(self, attr))
            for attr in vars(self) if not attr.startswith("_")
            }