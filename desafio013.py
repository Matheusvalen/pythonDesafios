#Faça um algoritmo que leia um salário de um funcionário e mostre seu
# novo salário, com aumento de 15%
salário = float(input('Qual o salário do Funcionário? R$'))
aumento = salário+(salário * 15 / 100)
print('Um Funcionário recebia {:.2f}, com o aumento de 15%, ele agora passa a receber {:.2f}'.format(salário, aumento))
