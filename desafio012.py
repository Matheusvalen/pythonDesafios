#desafio012: Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.
#para esse exercício você precisará calcular regra de três. Fazendo 10 vezes 5 dividido por 100.
#Essa conta pode ser feita no Python Console
#R$10      100%
#    \    /
#     \  /
#      \/
#      /\
#     /  \
#    /    \
#   x      5%
preço = float(input('Qual é o preço do produto? R$'))
novo = preço-(preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
