# Poke Info API

> Using this you can get pokemons info. It is built using [PokeAPI v2](https://pokeapi.co/docs/v2) and is for educational purpose only.

## Aiohttp Server
* Go inside `Aiohttp` folder.
* Create a virtual env and activate it.
```shell
$ python -m venv venv
$ source venv/Scripts/activate
```
* Install required packages.
```shell
(venv) $ pip install -r requirements.txt
```
* Start the server at port `8080`.
```shell
(venv) $ python main.py
```

## FastAPI Server
* Go inside `FastApi` folder.
* Repeat same steps mentioned above.

## Interaction with Server
* You can interact with the server using `Swagger/ReDoc/RapiDoc` UIs. Use below links,
```
Swagger : http://localhost:8080/swagger
ReDoc : http://localhost:8080/redoc
RapiDoc : http://localhost:8080/rapidoc
```

## Reference
* [PokeAPI v2](https://pokeapi.co/docs/v2)
* [aiohttp-swagger3](https://aiohttp-swagger3.readthedocs.io/en/latest/)
* [Aiohttp Client](https://docs.aiohttp.org/en/stable/client.html)
* [Aiohttp Server](https://docs.aiohttp.org/en/stable/web.html)
* [FastAPI](https://fastapi.tiangolo.com/)
* [RapiDoc](https://rapidocweb.com/)