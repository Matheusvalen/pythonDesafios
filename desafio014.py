#Escreva um programa que converta uma temperatura digítada em gruas °C e
#converta em °F.
#dica: a formula para converter celcius para fahrenheit
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32 #nove vezes c, tudo isso dividido por 5 e tudo isso mais 32
#se você quiser você também pode tirar os parenteses porque a ordem de precedência da expressão é exatamente a mesma que os operadores aparecem
print('A temperatura de {}°C corresponde a {} °F!'.format(c, f))
