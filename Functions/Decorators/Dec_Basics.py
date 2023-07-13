#f1=f1+f2

def make_pretty(func):
    def inner():
        print("I got decorated")
        #func()
    return inner

#@make_pretty
def ordinary():
    print("I am ordinary")
#ordinary()
# Output: I am ordinary

dec_fun=make_pretty(ordinary())
(dec_fun())

def add(x,y):
    return x+y
def calculate(func,x,y):
    return func(x,y)
res=calculate(add,2,6)
print(res)
