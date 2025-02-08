#Escreva um programa que pergunte o valor total da conta em seguida pergunte "Quantos clientes existem",divida as contas pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "Cada cliente deve pagar:[x valor]"
conta=float(input("Valor total da conta:"))
clientes=int(input("Numeros de clientes:"))
print("Cada cliente deve pagar",conta/clientes)