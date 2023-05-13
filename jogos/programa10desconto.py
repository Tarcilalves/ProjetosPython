print("*********************************")
print("Aplicação de desconto")
print("*********************************")


totalCompra_str = input("Digite o valor total da compra: R$ ")

print("Você digitou: R$ ", totalCompra_str)
total = int(totalCompra_str)


if(total >= 300):
    desconto = total * 0.1
    valorComDesconto = total - desconto
    print("*** O valor final com desconto é: R$", valorComDesconto, "***")
else:
    print("*** Este valor de compra não tem desconto ***")
    print("*** O valor da sua compra deu: R$", total, "***")

