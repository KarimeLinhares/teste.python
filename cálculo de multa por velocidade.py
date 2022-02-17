v = int(input('\033[1;37m''Qual é a velocidade atual do carro?:''\033[0;0m'' '))
if v > 80:
    print('\033[1;31m''MULTADO!''\033[0;0m''\033[1;37m''Você excedeu o limite permitido que é de 80Km/h''\033[0;0m')
    print('\033[1;37m''Você deve pagar uma multa de''\033[0;0m''\033[1;31m'' R${:.2f}!''\033[0;0m'.format((v-80)*7))
print('\033[1;92m''Tenha um bom dia! Dirija com segurança!''\033[0;0m')