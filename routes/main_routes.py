from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from scripts.database import Database
import json

data = Blueprint("main_api", __name__)


@data.route("/getCodeInfo")
def getHome():
    db = Database().getData()
    
    cardInfos =[]
    for row in db:
        cardInfo={"cardType":row[0], "product_id":row[1], "text":row[2], "url": row[3]}
        cardInfos.append(cardInfo)
    
    cardInfoJSON = json.dumps(cardInfos)
    return {"json" : cardInfoJSON}

