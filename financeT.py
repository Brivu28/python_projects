import time

timee = time.time
def logger(func):
    def wrapper(*args, **kwargs):
        print("The Finction is about to start")
        res = func(*args,**kwargs)
        print("The Function Has end")
        return res
    return wrapper
    
@logger
def add(a , b):
    print(a + b)
    
k = add(5,6)
print(k)

def greet(func):
    def wrapper(*args,**kwargs):
        print("hello")
        ft = timee()
        func()
        lt = timee()
        print(lt - ft)
    return wrapper

@greet
def hello():
    print("NAMASKAR")

hello()




















