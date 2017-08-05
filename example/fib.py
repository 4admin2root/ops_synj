#!/usr/bin/env python
# http://python.jobbole.com/86069/
import random
import time
import asyncio

def old_fib(n):
    res = [0] * n
    index = 0
    a = 0
    b = 1
    while index < n:
        res[index] = b
        a, b = b, a + b
        index += 1
    return res


# print('-' * 10 + 'test old fib' + '-' * 10)
# for fib_res in old_fib(20):
#     print(fib_res)



def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1


# print('-' * 10 + 'test yield fib' + '-' * 10)
# for fib_res in fib(20):
#     print(fib_res)

def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_cnt = yield b
		print('let me think {0} secs'.format(sleep_cnt))
		time.sleep(sleep_cnt)
		a, b = b, a + b
		index += 1
# print('-'*10 + 'test yield send' + '-'*10)
# N = 20
# sfib = stupid_fib(N)
# fib_res = next(sfib)
# while True:
# 	print(fib_res)
# 	try:
# 		fib_res = sfib.send(random.uniform(0, 0.5))
# 	except StopIteration:
# 		break

def copy_fib(n):
	print('I am copy from fib')
	yield from fib(n)
	print('Copy end')
# print('-'*10 + 'test yield from' + '-'*10)
# for fib_res in copy_fib(20):
# 	print(fib_res)



def copy_stupid_fib(n):
	print('I am copy from stupid fib')
	yield from stupid_fib(n)
	print('Copy end')
# print('-'*10 + 'test yield from and send' + '-'*10)
# N = 20
# csfib = copy_stupid_fib(N)
# fib_res = next(csfib)
# while True:
# 	print(fib_res)
# 	try:
# 		fib_res = csfib.send(random.uniform(0, 0.5))
# 	except StopIteration:
# 		break

@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs)
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs)
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [
#         asyncio.async(smart_fib(10)),
#         asyncio.async(stupid_fib(10)),
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print('All fib finished.')
#     loop.close()

async def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        await asyncio.sleep(sleep_secs)
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


async def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        await asyncio.sleep(sleep_secs)
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(smart_fib(10)),
        asyncio.ensure_future(stupid_fib(10)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
