from flask import Flask                                   
from flask_restful import Resource, Api, reqparse         
from flaskext.mysql import MySQL                          
from flask_cors import CORS                               
                                                          
mysql = MySQL()                                           
app = Flask(__name__)                                     
CORS(app)                                                 
                                                          
#Here we add our Database Connection Details              
app.config['MYSQL_DATABASE_USER'] = 'Username'          
app.config['MYSQL_DATABASE_PASSWORD'] = 'Password'        
app.config['MYSQL_DATABASE_DB'] = 'DatabaseName'          
app.config['MYSQL_DATABASE_HOST'] = 'HostName/ServerName' 
                                                          
mysql.init_app(app)                                      
api = Api(app)