import time

def d_time(foo):
    def inner(*args):
        start_time = time.time()
        func = foo(*args)
        print "execution time: ", time.time() - start_time
        return func
    return inner

def args(foo):
    def inner(*arg):
        print "%s%s" % (foo.func_name, arg)
        return foo(*arg)
    return inner

@d_time
@args
def mult(x, y):
    time.sleep(3)
    return x*y

@d_time
@args
def factorial( x ):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print factorial(10)
print mult(4, 5)
