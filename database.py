#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Video(Base):
    __tablename__ = 'mpg'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    path = Column(String(256), nullable=False)
    key = Column(String(32), nullable=False)
    kid = Column(String(32), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'path': self.path,
            'key': self.key,
            'kid': self.kid,
        }
        # Return object data in easily serializeable format


engine = create_engine('sqlite:///videos.db')

Base.metadata.create_all(engine)
