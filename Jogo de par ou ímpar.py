n = int(input('\033[1;36m''Me diga um número qualquer:''\033[0;0m'))
if n%2 == 0:
    print('\033[1;36m''O número ''\033[0;0m''\033[1;31m''{}''\033[0;0m''\033[1;36m'' é par!''\033[0;0m'.format(n))
else:
    print('\033[1;36m''O número ''\033[0;0m''\033[1;31m''{}''\033[0;0m''\033[1;36m'' é ímpar!''\033[0;0m'.format(n))
