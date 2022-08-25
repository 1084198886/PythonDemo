"""
协程
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'consume {n}')
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print(f'produce {n}')
        r = c.send(n)
        print(f'producer revc {r}')
    c.close()


c = consumer()
# producer(c)

import asyncio

import threading


@asyncio.coroutine
def hello():
    print(f'hello world!  {threading.currentThread().name}')
    r = yield from asyncio.sleep(2)
    print('hello again!')


@asyncio.coroutine
def hello2():
    print(f'hello2 world!  {threading.currentThread().name}')
    yield from asyncio.sleep(1)
    print('hello2 again!')


@asyncio.coroutine
def hello3():
    print(f'hello3 world!  {threading.currentThread().name}')
    yield from asyncio.sleep(1)
    print('hello3 again!')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([hello(), hello2(), hello3()]))
# loop.close()

print('------------asyncio的异步网络连接来获取sina、sohu和163的网站首页：-------------------')


@asyncio.coroutine
def wget(host):
    print(f'***************wget {host}...')
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print(f'{host} header > {line.decode("utf-8").rstrip()}')
    # Ignore the body, close the socket
    writer.close()


# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


async def eat():
    print(' start eat')
    await  asyncio.sleep(1)
    print(' finish eat')

#
# loop2 = asyncio.get_event_loop()
# loop2.run_until_complete(asyncio.wait([eat()]))
# loop2.close()

import asyncio
from aiohttp import web


async def index(request):
    await  asyncio.sleep(1)
    return web.Response(body=b'<h1>Index</h1>')


async def helloT(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop_):
    app = web.Application(loop=loop_)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/home/zhangsan', helloT)
    srv = await  loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
