# This is the Django API for appleCat

## API endpoints documentation:
### create account 
POST request to "/CreateCat" with the following data body: 
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

### log in 
POST request to "/Login" with the following data body:
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
