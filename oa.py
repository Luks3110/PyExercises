import ctypes

atributo_ocultar = 0x02

retorno = ctypes.CDLL..SetFileAttributeW('ocultar.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('deu errado')