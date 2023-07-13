def outer_fun():
    print("HEllo")
    def inner_fun():
        print("World")
    inner_fun()

outer_fun()


def increment(n):
    def inner_increment():
        return n+1
    return inner_increment()*2

print(increment(10+1))

def fun1():
    p="Hello dears"
    def fun2():
        print(p)
    fun2()
fun1()

