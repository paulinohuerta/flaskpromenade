# flaskpromenade

## flask microframework introduction

# Scripts
-----

## Returning JSON format data

### hello.py
-----
_**Description**_: Adds a route to return JSON format data.    
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*URL 3*: http://localhost:5003/person/robert/age/36              
*URL 4*: curl -H 'Accept: application/json' -X GET http://localhost:5003/advices    
*improvement*: Moving the presentation logic into templates.    
