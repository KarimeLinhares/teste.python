import random
import time
print('\033[1;34m''-=-''\033[0;0m'*17)
print('\033[1;33m''Vou pensar em um número entre 0 e 5. Tente Advinhar!''\033[0;0m')
print('\033[1;34m''-=-''\033[0;0m'*17)
nc = random.randint(0,5)
n = int(input('Em que número eu pensei? '))
print('\033[1;33m''PROCESSANDO ...''\033[0;0m')
time.sleep(2)
if nc == n:
    print('\033[1;32m''PARABÉNS! Eu também pensei no {}''\033[0;0m'.format(nc))
else:
    print('\033[1;31m''GANHEI! Eu pensei no número {} e não no número {}''\033[0;0m'.format(nc, n))


