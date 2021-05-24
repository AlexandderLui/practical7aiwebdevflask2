import os
class Settings:
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Production
    #Staging on heroku
    
     
    host = os.environ['HOST']
    database = os.environ['DATABASE']
    user = os.environ['USERNAME']
    password = os.environ['PASSWORD']

"""
    #Dev
    host='localhost'
    database='furniture2'
    user='root'
    password='A!ex1333'
"""
    