from builtins import input

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numeroSecreto = 42

chute_str = input("Digita o seu número: ")

print("Você digitou:", chute_str)
chute = int(chute_str)

if(numeroSecreto == chute):
    print("*** Você acertou!!! ***")
else:
    print("*** Você errou!!! ***")

print("*********************************")
print("********** Fim do jogo  *********")
print("*********************************")
