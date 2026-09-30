#!/data/cond/envs/a/bin/python
from aiohttp.web import RouteTableDef, Application, AppRunner, TCPSite, WebSocketResponse
from asyncio import get_event_loop
from functools import partial

l = get_event_loop()
def go(f):
    l.create_task(f())


R = []
t = RouteTableDef()
@t.get('/')
async def _(t):
    r = WebSocketResponse()
    await r.prepare(t)
    R.append(r)
    async for t in r:
        print(t.data)
    R.remove(r)
r = Application()
r.add_routes(t)
r = AppRunner(r)
@go
async def _():
    await r.setup()
    await TCPSite(r, '0.0.0.0', 2222).start()

@partial(l.add_reader, 0)
def _():
    @go
    async def _():
        for r in R:
            await r.send_str(input())

l.run_forever()