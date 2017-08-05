import time
t = time.time()
for i in xrange(10**8):
    continue
print time.time() - t
#➜  example git:(master) ✗ python time_test.py
#3.08078503609
#➜  example git:(master) ✗ pypy time_test.py
#0.100780010223
