import functools
from flask import Flask, json,jsonify,request,g
from config.Settings import Settings

import jwt
import re


def login_required(func):
    @functools.wraps(func)
    def secure_login(*args, **kwargs):
        auth=True

        auth_header = request.headers.get('Authorization') #retrieve authorization bearer token
        if auth_header: 
            auth_token = auth_header.split(" ")[1]#retrieve the JWT value without the Bearer 
        else:
            auth_token = ''
            auth=False #Failed check
        if auth_token:
            try:
                payload = jwt.decode(auth_token,Settings.secretKey,algorithms=['HS256'])
                #print(payload)
                g.userid=payload['userid']#update info in flask application context's g which lasts for one req/res cyycle
                g.role=payload['role']

            except jwt.exceptions.InvalidSignatureError as err:
                print(err)
                auth=False #Failed check

        if auth==False:
            return jsonify({"Message":"Not Authorized!"}),403 #return response

        return func(*args, **kwargs)

    return secure_login


def validateRegister(func):
    @functools.wraps(func)
    def validate(*args, **kwargs):
        return func(*args,**kwargs)
       
    return validate



# def validateNumber(num):

    # [1-9][0-9] is 1 to 9 AND 0 to 9
    # \.
    #[0-9] is 0 to 9
    # patternNum=re.compile('^(([1-9][0-9]*)|0)(\.[0-9]{2})?$')
    
    

    #username=request.json['username']
    #email=request.json['email']
    #role=request.json['role']
    #password=request.json['password']


def validateNumber(func):

    @functools.wraps(func)
    def validateUserID(*args, **kwargs):
        # Do something before
        # value = func(*args, **kwargs)
        
        # user input
        userid = request.json["userid"]
    
        # create regex with a pattern
        patternNum=re.compile([0-9])

        # match will return None if there is no match
        if(patternNum.match(userid)):
            
            print("Correct userid")
            value = func(*args, **kwargs)
            return value
    
    
        else:
            return jsonify({"Message":"Validation Failed!"}),403 #return response
    
    # return validateNumber.match(num)

    return validateUserID
"""

def validateNum(num):
    patternNum = re.compile('^(([1-9][0-9]*)|0)(\.[0-9]{2})?$')
    return patternNum.match(num)

"""