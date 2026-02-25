# Asynchronous Server Gateway Interface(ASGI).
# Normally, before FastAPI we use WSGI which is synchronous.
# FastAPI is ASGI.
# ASGI= asyncio + webserver.
# ASGI has 3 parameters i.e. scope, request, response.

import uvicorn

async def app(scope,receive,send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
            ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })

async def apprwm(scope,receive,send):
    await send({
        'type':'http.response.start',
        'status':200,
        'headers':[
            [b'content-type', b'text/plain']
             ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, Venu!',
    })
# Now we are running the main module
# if this module app is from the same page then
# `asgi:app` takes the module app from `asgi` file
# run on port 5000.
if __name__ == "__main__":
    uvicorn.run("asgi:apprwm", port=5000, log_level="info")