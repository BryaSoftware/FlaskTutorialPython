from dbConfig import mysql                               
from flask import Flask                                  
from flask_restful import Resource, Api, reqparse        
                                                          
class Tutorial(Resource):                                
     def get(self):                                       
         try:                                             
             parser = reqparse.RequestParser()            
             #here is where we add any parameters
             parser.add_argument('Keyword', type=str, help='')
             args = parser.parse_args()
             
             P_Keyword = args['Keyword']
             conn = mysql.connect()
             cursor = conn.cursor()
             cursor.callproc('spGetKeywords', (P_Keyword))
             data = cursor.fetchall()

             conn.commit()
             #return the data
             return data
         
         except Exception as e:
             return {'error': str(e)} 