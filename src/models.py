import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorite'
    fav_Id = Column (Integer, primary_key=True)
    char_Id = Column (Integer, ForeignKey('Character.char_Id'),nullable=True)
    planet_Id = Column (Integer, ForeignKey('Planet.planet_id'), nullable=True)
    user_Id = Column (Integer, ForeignKey('User.id'))

class Characters (Base):
    __tablename__ = 'Character'
    char_Id = Column (Integer, primary_key=True)
    char_name = Column (String (250), nullable=False)
    char_age = Column(Integer, nullable=False)
    char_height = Column(Integer, nullable=False)


class Planets(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_mass = Column(String(250))
    planet_environment = Column(String(250), nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
