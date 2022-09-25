from time import sleep

print('='*30)
print('{:^30}'.format(' CAIXA ELETRÔNICO '))
print('='*30)

#variavais para receber informações da operação no caixa eletronico e inforações das cédulas/notas em Reais
banco = float(input('Saldo em banco: R$'))
valor = int(input('Que valor deseja retirar: R$'))
total = valor
cedula = 50 
totalCedula = 0 

#codigo que fara as seguintes funções:
while True:
    # solicitado valor no banco usuario nao pode tirar mais do que existe dispoviel para saque
    while valor > banco:
        valor = int(input('Digite um valor dentro do seu saldo: '))
        total = valor
    # após verificado valor de saque <= a saldo no banco, o sistema gerencia as notas para saque
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
    # finalizando a operação, o sistema analisa as notas disponiveis e distribui as notas mediante o valor solicitado saque
        if totalCedula > 0:
            print(f'Total de {totalCedula} céculas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        totalCedula = 0
        if total == 0:
            break
print('=-'*25)
# var responsavel por fazer calculo de saldo - valor solicitado de saque para mostrar valor atualizado no sistema
novosaldo = valor - banco 
# finalizando a parte lógica dos calculos e entregando o saque, programa pergunta se o usuário quer ver o extrato do banco
extrato = str(input('Deseja ver o extrato: [S/N]')).strip().upper()[0]
# SE solicitado Sim para ver extrato sistema "carrega" com TIME o processamento dos dados, mostando o antigo e novo valor em conta, se não.
# programa finalizado com mensagem de agradecimento 
if extrato == 'S':
    print('processando...')
    sleep(0.5)
    print('=-'*25)
    sleep(0.5)
    print(f'Seu saldo era de R${banco} e passou a ser R${novosaldo*-1}')
    print('=-'*25)
else:
    print('=-'*33)
print('Operação finalizada! BANCO DA CIDADE Agradece a preferência :) ')
