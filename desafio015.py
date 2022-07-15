#Escreva um programa que pergunte a quantidade de km percorrídos por um carro alugado
#e a quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$60 por dia e R$0.15 por km rodado.
dias = int(input('Quantos dias? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))
