import inter3
while True:
    linea=input('cal> ')
    resultado,error=inter3.run('prueba',linea)
    if error: print(error.as_string())
    elif resultado: print(repr(resultado)) 