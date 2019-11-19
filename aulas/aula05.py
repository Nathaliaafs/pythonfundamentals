# MANIPULAÇÃO DE DADOS 

 #arq1 = '../arquivos/sherlock.txt' #esta aberto e dentro de uma instancia 

# print(arq1.read()) #mostra conteúdo do arquivo 
# #print(arq1.tell()) #mostra a quantidade de caracteres lembrando que o read tem que rodar primeiro 
# #print(arq1.seek(3,2))
# print (arq1.read(500))
# arq1.close()

# with open ('arquivo01.txt','x') as f:
#     f.write('Abrindo arquivos em python')


# with open(arq1,'r+') as f:
#     print(f.readlines())

# def soma (x,y):
#     return x + y

# print (soma(10,13))    
  

# produtos = []

# def cadastraProduto (produtos):
#     #global produto 
#     produtos.append (produto)

# def listarProduto ():
#     #global produtos
#     for p in produtos:
#         print (p) 

# produto = ""

# while produto != "sair":
#     produto = input('Digite o produto que deseja:')
#     cadastraProduto(produto)
#     print('produtos cadastrados:')
#     listarProduto ()

 


# def primo (num):
#     for n in range (2, num):
#         if num % n == 0:
#             print('Não é primo')
#             break
#         else:
#                 print('é primo')

# primo(3)           


# def alternaServidor (atual, novo):
#     print('O IP atual é :', atual)
#     print('o nomo ip é:', nome)

#  alternaServidor('192.168.1.1', '192.168.1.254')



# def conexao():
#     r = requests.get ('https://google.com')
#     print(r.status_code)

# conexao()


# def media(x,y):
#     return(x+y) / 2
# print (media(10,2))    


#ark tupla

# def printa(*valores):
#     print (valores[0])
#     print (valores[1])

# printa ('nome','sobrenome')

#kar.. dicionario 


# def printa2(**valores):
#     print (valores)


# printa2(var1='valor', var2='valo2' , var3= 'valor3')



# texto = 'Olá sou apenas um teste para esse exercicio.'

# def split_texto(text):
#     return text.split('')

# split_texto(texto)    


