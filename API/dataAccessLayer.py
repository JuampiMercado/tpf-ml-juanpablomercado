from dbManager import DBManager as db

class DAL:
    def getPlaces(self):
        df = db.query("SELECT p.placeid, p.name FROM places p order by p.placeid")
        return  df.to_dict(orient="records")
    def getPlaceById(self,placeid):
        df = db.query(f"SELECT p.placeid, p.name FROM places p where p.placeid = {placeid} order by p.placeid")
        return  df.to_dict(orient="records")
    def getPlacesByName(self,placename):
        df = db.query(f"SELECT p.placeid, p.name FROM places p where upper(p.name) = upper('{placename}') order by p.placeid")
        return  df.to_dict(orient="records")

    def getRatings(self):
        df = db.query("SELECT r.placeid, p.name, r.userid, r.rating FROM ratings r join places p on r.placeid = p.placeid order by r.placeid, r.rating")
        return  df.to_dict(orient="records")
    
    def getRatingsByUser(self,userid):
        df = db.query(f"SELECT r.placeid, p.name, r.userid, r.rating FROM ratings r join places p on r.placeid = p.placeid where r.userid = '{userid}' order by r.placeid, r.rating")
        return  df.to_dict(orient="records")

    def getRatingsByPlace(self,placeid):
        df = db.query(f"SELECT r.placeid, p.name, r.userid, r.rating FROM ratings r join places p on r.placeid = p.placeid where p.placeid = {placeid} order by r.placeid, r.rating")
        return  df.to_dict(orient="records")

    def getRecommendations(self):
        df = db.query("SELECT r.*,p.name FROM recommendations r join places p on r.placeid = p.placeid")
        return  df.to_dict(orient="records")
    
    def getRecommendationByPlaceName(self,placeName):
        s = f"select p2.placeid, p2.name from places p join recommendations r on p.placeid = r.placeid join places p2 on r.recommended_placeid = p2.placeid where upper(p.name) = upper('{placeName}')"
        print(s)
        df = db.query(s)

        return  df.to_dict(orient="records")