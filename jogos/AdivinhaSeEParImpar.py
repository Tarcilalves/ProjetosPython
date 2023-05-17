print("*********************************")
print("Crie um programa que solicite o valor de um número ao usuário e imprima se o mesmo é par ou ímpar")
print("*********************************")


numero_str = input("Digite um número: ")

print("Você digitou:  ", numero_str)
numero = int(numero_str)

numeroDigitado = numero % 2
if(numeroDigitado == 0 ):

    print("*** O número que você digitou é PAR" "***")
else:
    print("*** O número digitou é IMPAR ***")
