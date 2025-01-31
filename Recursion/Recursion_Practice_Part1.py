'''def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
    print(n)

fun(3)'''


def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
    fun(n-1)
fun(3)
