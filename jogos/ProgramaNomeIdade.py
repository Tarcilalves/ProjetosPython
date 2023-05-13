
print("*********************************")
print("Formulário simples")
print("*********************************")

nome = input("Digita o seu nome: ")
print("Você digitou:", nome)

idade_str = input("Digita a sua idade: ")
print("Você digitou:", idade_str)

idade = int(idade_str)

if(idade >= 18):
    print( "Olá!", nome, "Seja bem vindo!")
else:
    print("*** Você não pode entrar. ***")





