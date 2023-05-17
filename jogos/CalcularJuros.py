valorOriginal = 200
quantidadeParcela = 4
juros = 0

if(quantidadeParcela == 0 or quantidadeParcela == 1):
    juros = 0
else:
    if(quantidadeParcela == 2 or quantidadeParcela == 3):
        juros = 10
    elif(quantidadeParcela > 4):
        juros = 20

valorAtualizado = valorOriginal + (valorOriginal*juros/100)
prestacaoMensal = valorAtualizado/quantidadeParcela

print(valorAtualizado)
print(prestacaoMensal)