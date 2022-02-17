n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {}'.format(m))
if m >= 7.0:
    print('Você está aprovado!')
else:
    print('Você está reprovado!')
