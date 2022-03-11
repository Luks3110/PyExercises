import hashlib

str = input("Digite o texto a ser encryptado: ")

menu = int(input(''' ###MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(str.encode('utf-8'))
    print(f"O hash da string {str} é: {resultado.hexdigest()}")
elif menu == 2:
    resultado = hashlib.sha1(str.encode('utf-8'))
    print(f"O hash da string {str} é: {resultado.hexdigest()}")
elif menu == 3:
    resultado = hashlib.sha256(str.encode('utf-8'))
    print(f"O hash da string {str} é: {resultado.hexdigest()}")
elif menu == 4:
    resultado = hashlib.sha512(str.encode('utf-8'))
    print(f"O hash da string {str} é: {resultado.hexdigest()}")
else:
    print('Preencha corretamente!')
