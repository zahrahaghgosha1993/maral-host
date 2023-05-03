## Run Project

In the project directory, you can run:

### `docker compose up --build `

Open [http://localhost:8008](http://localhost:8008) to view it in the browser.

## Panel

Panel Login url  : [http://localhost:8008/user/panel/login](http://localhost:8008/user/panel/login])


## Api

Api Login spec : 
###
```
POST /user/api/token/ HTTP/1.1
Host: 127.0.0.1:8008
Content-Type: application/json

{
    "email":"zahra@email.com",
    "password":"123"
}
```