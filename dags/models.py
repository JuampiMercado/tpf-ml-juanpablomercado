"""Dummy data model definition."""
from sqlalchemy import Column, String, Float, Numeric,UniqueConstraint
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Place(Base):
    """Places data model."""

    __tablename__ = "places"
    placeid = Column(Numeric, primary_key=True)
    name = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    def __repr__(self):
        return f"<Place(placeid='{self.placeid}',name='{self.name}',city='{self.city}',state='{self.state}',country='{self.country}' )>"

    def __init__(self,placeid,name,city,state,country):
        self.placeid = placeid
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        super(Place, self).__init__()
    
    def __str__(self):
        return f"placeid='{self.placeid}',name='{self.name}',city='{self.city}',state='{self.state}',country='{self.country}'"

class Rating(Base):
    """Ratings data model."""

    __tablename__ = "ratings"
    userid = Column(String, primary_key=True)
    placeid = Column(Numeric, primary_key=True)
    rating = Column(Numeric)
    

    def __repr__(self):
        return f"<Rating(userid='{self.userid}',placeid='{self.placeid}',rating='{self.rating}' )>"

    def __init__(self,userid,placeid,rating):
        self.userid = userid
        self.placeid = placeid
        self.rating = rating        
        super(Rating, self).__init__()
    
    def __str__(self):
        return f"userid='{self.userid}',placeid='{self.placeid}',rating='{self.rating}''"


class Recommendation(Base):
    """Recommendation data model."""

    __tablename__ = "recommendations"
    recomendationid = Column(Numeric, primary_key=True, autoincrement=True)
    placeid = Column(Numeric)
    recommended_placeid = Column(Numeric)

    __table_args__ = (UniqueConstraint('placeid', 'recommended_placeid', name='recommendation_unique'),)

    def __repr__(self):
        return f"<Recommendation(placeid='{self.placeid}',recommended_placeid='{self.recommended_placeid}' )>"

    def __init__(self,placeid,recommended_placeid):
        self.placeid = placeid
        self.recommended_placeid = recommended_placeid
        super(Recommendation, self).__init__()
    
    def __str__(self):
        return f"placeid='{self.placeid}',recommended_placeid='{self.recommended_placeid}''"


