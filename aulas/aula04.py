# try:

#     x = int (input('Digite o primeiro numero:'))
#     y = int (input('Digite o primeiro numero:'))

#     print(x + y)

#     except ValueError as e: #tratamento de erro. 
#        print('Digite apenas números', e)
# while True:
# try:
#     user = input ('Digite o nome de usuario:')
#      if user == 'ANA':
#          raise NameError('usuario bloqueado!!') #para criar um erro ou bloquear um parametro
#      else:
#          print(f'bem vindo')

#     print(x + y)

#     except ValueError as e:
#        print('Digite apenas números', e)

try:
    login = input('Digite seu login: ')
    if login == 'caio':
        raise NameError ('Usuario banido!')
    else:
        print(f'Bem vindo(a){login}!')   
except NameError as n:
    print(n)             
finally :print ('finally:')    

