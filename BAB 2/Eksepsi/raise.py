#membangkitkan eksepsi
def intdiv(a,b):
    if not isinstance(a,int) or \
        not isinstance(b,int):
            raise TypeError('ERROR: a dan b harus betipe bilangan bulat')
    if b == 0:
            raise ZeroDivisionError('ERROR: b tidak boleh 0')
    c = a//b
    return c


intdiv(5,3.6)
