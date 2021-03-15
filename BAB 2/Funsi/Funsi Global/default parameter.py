def tulis(s, gantibaris=True):
    if not gantibaris:
        print(s, end=' ')
    else:
        print(s)


tulis('Python')

tulis('Python',False);tulis('dan Java')


tulis('Python');tulis('Java')