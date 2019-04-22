from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS
from dbConfig import api, app, mysql
from tutorial import Tutorial

@app.route("/")
def index():
    name = "this is the route."
    return name

api.add_resource(Tutorial, '/Tutorial')

if __name__ == '__main__':
    app.run(debug=True)
