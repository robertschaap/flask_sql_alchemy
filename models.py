from sqlalchemy import Column, Integer, String, Text, Date
from database import Base

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(50), unique=True)
  email = Column(String(120), unique=True)

  def __init__(self, name=None, email=None):
    self.name = name
    self.email = email

  def __repr__(self):
    return '<User %r>' % (self.name)

class Something(Base):
  __tablename__ = 'somethings'
  id = Column(Integer, primary_key=True)
  title = Column(Text)
  date1 = Column(Date)
  date2 = Column(Date)

  def __repr__(self):
    return '<Something (%r %r)>' % (self.title, self.date2)
