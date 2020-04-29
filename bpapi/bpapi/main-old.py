__Author__ = "Waldir Borba Junior"
__Version__ = "0.0.1"
__Email__ = "wborbajr@gmail.com"
__Website__ = ""

try:
    # import uvicorn
    from fastapi import FastAPI

    # from redis import Redis
    import os
except Exception as e:
    print("Some modules are missing {}".format(e))

# used environment variabls from docker-composer
# if os.environ.get('HOST_REDIS'):
#     host_redis = os.environ.get('HOST_REDIS')
# else:
#     host_redis = 'redis'

# if os.environ.get('PORT_REDIS'):
#     host_port = os.environ.get('PORT_REDIS')
# else:
#     host_port = 9090


# init app
app = FastAPI()
# redis = Redis(host=host_redis, port=host_port)


# routes
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    /items/{item_id}, returns selected item {"item_id": item_id, "q": q}
    """
    return {"item_id": item_id, "q": q}


# if __name__ == '__main__' :
#     uvicorn.run(app, host="127.0.0.1", port=9090)
