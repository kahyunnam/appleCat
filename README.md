# This is the Django API for appleCat

# API endpoints documentation:
## create applicant account
POST request to "/CreateCat" with the following JSON data body: 
```
{
  "userName":{string}, 
  "userPassword:{string}
}
```
if password and username are valid, API will return the response:
```
{
    "userName": {string},
    "userPassword": {string},
    "accessKey": {string}
}
```
if NOT valid, API will return the response:
```
{
        "userName": "notvalid",
        "userPassword": "notvalid",
        "accessKey": "notvalid"
}
```

## log in 
POST request to "/Login" with the following JSON data body:
```
{
  "userName":{string}, 
  "userPassword:{string}
}
```
if password and username are correct, API will return the response:
```
{
    "login": true,
    "accessKey": {string},
}
```
if incorrect:
```
{
    "login": false,
    "accessKey": "",
}
```

## create application
POST request to "/NewApple" with the following JSON data body: 
```
{
    "cat":{string, existing Cat object's accessKey},
    "company":{string},
    "jobTitle":{string},
    "location":{string},
    "submittedDate":{string},
    "pending": {bool, optional},
    "rejected": {bool, optional},
    "accepted": {bool, optional},
    "description": {str, optional},
    "notes": {str, optional}
    
}
```
if successful, return:

```
{
    "id": {int},
    "cat": {string},
    "company": {string},
    "jobTitle": {string},
    "location": {string},
    "submittedDate": {string},
    "pending": {bool},
    "rejected": {bool},
    "accepted": {bool},
    "description": {string} or null,
    "notes": {string} or null
}
```

if not successful, return: 
```
{
  "cat": "fieldsnotvalid"
}
```

## update application
PUT request to "UpdateApple/{str: accessKey}/{int: Apple.id}" with the same data JSON body as above. If successful, return same JSON body as above. 

if accessKey account does not exist, will return: 
```
{
  "cat": "catdoesnotexist"
}
```
if apple with Apple.id does not exist, will return:
```
{
  "cat": "appledoesnotexist"
}
```
if data JSON body is not valid: 
```
{
  "cat": "fieldsnotvalid"
}
```
