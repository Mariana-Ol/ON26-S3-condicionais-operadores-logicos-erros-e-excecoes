#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
#e escreva o valor a ser pago pelo cliente.

morangos, macas = float(input('Quantos quilos de morango foram comprados? ')), float(input('Quantos quilos de maçã foram comprados? '))

if morangos <= 5:
    custo_morangos = 2.5*morangos
else:
    custo_morangos = 2.2*morangos

if macas <= 5:
    custo_macas = 1.8*macas
else:
    custo_macas = 1.5*macas

custo_total = custo_morangos + custo_macas

if (morangos + macas > 8) or (custo_total > 25):
    custo_total = custo_total*0.90

print('Valor total da compra:', custo_total) 

