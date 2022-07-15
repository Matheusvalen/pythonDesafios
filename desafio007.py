n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
#Exemplo de erro que você pode cometer a baixo
média = (n1 + n2) / 2
print ('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))