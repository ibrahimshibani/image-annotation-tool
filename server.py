from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from configs.app_config import db_name, collection_name, mongodb_url
from utils.image import ImageData
from typing import List


client = MongoClient(mongodb_url)
db = client[db_name]

app = FastAPI()


@app.post("/upload/")
def upload_image(image: ImageData):
    collection = db[collection_name]
    result = collection.insert_one(image.dict())
    return {"_id": str(result.inserted_id)}


@app.get("/images/{image_ids}", response_model=List[ImageData])
def get_images(image_ids: str):
    collection = db[collection_name]
    image_ids = image_ids.split(',')
    object_ids = [ObjectId(id) for id in image_ids]
    images = list(collection.find({"_id": {"$in": object_ids}}))
    return images
