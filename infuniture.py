from asyncio import create_task, wait, Future, sleep
class _(list):
    def __call__(s, a):
        def _(f):
            s.__iadd__(create_task(f(a))for a in a)
        return _
    async def ing(s):
        await wait(s)
        s.clear()
go = _()

from time import time
# async def infuniture(a, b, n):
#     s = [Future() for _ in range(a)]
#     a = [Future() for _ in range(a)]
#     b = [Future() for _ in range(b)]
#     @go(range(len(a)))
#     async def _(i):
#         s[i].set_result(None)
#         for _ in range(n):
#             await wait(b)
#             await sleep(1)
#             a[i].set_result(None)
#             a[i] = Future()
#     await wait(s)
#     @go(range(len(b)))
#     async def _(i):
#         for _ in range(n):
#             await sleep(1)
#             b[i].set_result(None)
#             b[i] = Future()
#             await wait(a)
#     t = time()
#     await go.ing()
#     print(time() - t)
async def infuniture(a, b, n):
    t = time()
    for _ in range(n):
        await wait([sleep(1)for _ in range(a)])
        await wait([sleep(1)for _ in range(b)])
    print(time() - t)

from uvloop import install
from asyncio import run
install()
run(infuniture(65536*4, 65536*4, 10))