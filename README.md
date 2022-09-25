# caixa_eletronico.py

## OBJETIVO 

- O objetivo do programa é realizar leitura do saldo em conta, valor do saque, contagem das notas e saldo final.

## COMO FUNCIONA:
- O programa tem por início, fazer a leitura do saldo bancario digitado pelo próprio usuário;
- Após a leitura o programa pergunta, qual valor o usuário quer ser retirá:
  - Se solicitado um valor acima do saldo em conta o programa nao permite o saque;
  - Enquanto não solicitado um valor igual ou menor que saldo em conta o programa ficará em um loop infinito;
- Quando solicitado um valor <= saldo, o programa calculará a quantidade baseado nas cédulas disponiveis e realizará o saque solicitado;
- Depois o sistema mostra quais e quantas notas foram usadas, para o valor solicitado;
- Depois de solicitado o valor de saque, o programa pergunta para o usuário se quer saber o novo saldo atual ou não;
- Se solicitado SIM, o sistema mostra o saldo antigo, mais o novo saldo depois do salque.
- Se solicitado NÃO, o sistema finaliza por isso mesmo apenas, mostrando apenas uma mensagem finalizado o serviço.
