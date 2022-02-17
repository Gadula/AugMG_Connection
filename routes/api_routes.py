from flask import Blueprint, render_template, request, redirect, url_for

api_data = Blueprint("api", __name__)


@api_data.route("/getCodeInfo")
def getHome():
    return '{"Data": "Welcome to the homepage"}'
