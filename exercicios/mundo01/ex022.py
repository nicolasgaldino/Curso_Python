'''Crie um programa que leia o nome completo
de uma pessoa e mostre:
O nome com todas as letras maiúculas
o nome com todas letras minúsculas
Quantas letras tem sem condsiderar espaços
Quantas letras tem o primeiro nome'''

nome = input('Qual seu nome? ')
mai = nome.upper()
min = nome.lower()
spc = nome.replace(' ', '')
qua = len(spc)
a1 = nome.split()
a2 = a1[0]
a3 = len(a2)
print('''
Olá, {}! 
Seu nome com todas as letras maiúculas fica: {};
Seu nome com todas a letras minúsculas fica: {};
Seu nome tem {} letras;
Seu primeiro nome tem {} letras;
'''.format(nome, mai, min, qua, a3))