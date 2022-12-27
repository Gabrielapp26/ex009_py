#Desafio 08
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 
print("Digite o valor do preço agora para saber o preço novo")
pa = float(input("Preço atual: "))
pd = pa - (pa * 5 / 100)
print("O valor do preço com desconto será {} reais".format(pd))