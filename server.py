import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
	return web.HTTPFound('/index.html')


@routes.get('/data')
async def data(request):
	return web.Response(text="Some data")


routes.static('/', './static')
app = web.Application()
app.add_routes(routes)



web.run_app(app)




