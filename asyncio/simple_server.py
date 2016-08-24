import asyncio
from aiohttp import web
app = web.Application()

static_dir = "../client"

# temp
@asyncio.coroutine
def h(r):
    return web.Response(body='hello world'.encode())

app.router.add_route('GET', '/', h)

app.router.add_static('/static/', static_dir, name='static')
app.router.add_static('/', static_dir + "/html/")
route = web.StaticRoute(None, '/static/', static_dir)
route._method = 'HEAD'
app.router.register_route(route)

loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, '0.0.0.0', 8090)
srv = loop.run_until_complete(f)

print('serving on', srv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.run_until_complete(app.finish())
loop.close()