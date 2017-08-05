#!/usr/bin/env python
# http://blog.csdn.net/gvfdbdf/article/details/52116661
import asyncio

def consumer():
    r = ''
    while True:
        n = yield r # 返回
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 调用
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)





async def hello():
        print("Hello World")
        r = await asyncio.sleep(2)
        print("Again")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
