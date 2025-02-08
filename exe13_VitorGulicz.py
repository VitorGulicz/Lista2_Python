#Escreva um programa que solicite um determinado numero de dias, em seguida exiba o quanto esses dias equivalem em horas, minutos e segundos
dias=int(input("Numeros de dias:"))
hora=dias*24
minutos=hora*60
segundos=minutos*60
print("dias:",dias,"horas:",hora,"minutos:",minutos,"segundos:",segundos)