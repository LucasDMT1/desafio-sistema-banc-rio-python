menu = """================ MENU ================
[1] Depositar
[2] Sacar
[3] Visualizar Extrato
[0] Sair
======================================"""


LIMITES_SAQUES = 3
saldo = 0
extrato = ""
numero_saque = 0
limite = 500

while True:
    opcao = int(input(menu))
    
    
    if opcao == 1:
        deposito = float(input("Digite a quantia que deseja depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato += f"Deposito: {deposito:.2f}\n"
            print(f"O seu saldo atual apos o deposito é de: R${saldo:.2f}")
        else:
             print("Operação falhou, o valor informado é invalido")
    
    elif opcao == 2:
        saque = float(input("Digite o valor que vc quer sacar: "))
        excedeu_saques = numero_saque >= LIMITES_SAQUES
        
        if excedeu_saques:
               print("Não foi possivel realizar o saque, numero de saques por dias exedidos")
        
        elif saque > saldo:
            print("Não foi possivel realizar o saque, saldo insuficiente")
        
        elif saque > limite:
             print("Não foi possivel realizar o saque, limite ultrapassado")
        
        elif saque > 0:
             saldo = saldo - saque
             extrato += f"Saque: R${saque:.2f}\n"
             print(f"O seu saldo apos o saque é de: {saldo}")
             numero_saque += 1
        else:
             print("O valor informado é invalido")
    
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
       
    elif opcao == 0:
         print("Obrigado por utilizar nosso sistema bancario!!!")
         break
         
    else:
         print("Não foi possivel realizar a Operação, opção selecionada invalida")
             
            
            
    


