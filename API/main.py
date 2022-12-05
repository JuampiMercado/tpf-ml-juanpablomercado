from fastapi import FastAPI
from dataAccessLayer import DAL
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
DAL = DAL()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return { "status" : "ok"}

@app.get("/places")
async def getPlaces():
    return DAL.getPlaces()

@app.get("/places/{placeid}")
async def getPlaceById(placeid):
    return DAL.getPlaceById(placeid)

@app.get("/places/getplacebyname/{placename}")
async def getPlacesByName(placename):
    return DAL.getPlacesByName(placename)
    

@app.get("/ratings")
async def getRatings():
    return DAL.getRatings()

@app.get("/ratings/user/{userid}")
async def getRatingsByUser(userid):
    return DAL.getRatingsByUser(userid)

@app.get("/ratings/place/{placeid}")
async def getRatingsByPlace(placeid):
    return DAL.getRatingsByPlace(placeid)

@app.get("/recommendations")
async def getRecommendations():
    return DAL.getRecommendations()

@app.get("/recommendations/{placeName}")
async def getRecommendationByPlaceName(placeName):
    return  DAL.getRecommendationByPlaceName(placeName)
