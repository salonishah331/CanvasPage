import pymongo
from pymongo import MongoClient
from .models import Canvas



client = MongoClient('mongo-dev-1.stackfolio.com', port=27017)
client.stackfolio_v1.authenticate('stackfolio-dev', 'HRSLjgyMrrJ4tHXq7d4GkQse', mechanism='SCRAM-SHA-1')
db = client['stackfolio_v1']


def getdrawing():
    # projection = {"_id" : -1, "xcoord" : 1, "ycoord" : 1, "color" : 1}
    x = db.drawingcollection.find({})
    return list(x)



def createdrawing(xcoord, ycoord, color):
    y = db.drawingcollection.insert_one({"color" : color, "xcoord" : xcoord, "ycoord" : ycoord})


# def getxcoord():
#     xcoords = db.drawingcollection.find({}).distinct("_xcoord")
#     xcoords = [str(coord) for coord in xcoords]
#     return xcoords

# def getycoord():
#     ycoords = db.drawingcollection.find({}).distinct("_ycoord")
#     ycoords = [str(coord) for coord in ycoords]
#     return ycoords




# def getpost(roomID):
#     x = db.postcollection.find({"RoomID" : roomID})
#     return x

# def createpost(text, roomID):
#     y = db.postcollection.insert_one({"post" : text, "RoomID" : roomID})


# def getroomids():
#     roomIDs = db.roomcollection.find({}).distinct("_id")
#     roomIDs = [ str(room) for room in roomIDs]
#     if len(roomIDs) == 0:
#         return createroom()
#     return roomIDs


# def createroom():
#     x = db.roomcollection.insert_one({})
#     return getroomids()