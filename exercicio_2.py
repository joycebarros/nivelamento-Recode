print("********************************")
print("Verifique o seu peso ideal!")
print("********************************")

print("Qual o seu sexo?")
sexo = input("Digite (H) para Homem ou (M) para Mulher: ")
altura_str = input("Digite a sua altura (exemplo 1.70): ")
altura = float(altura_str)

if(sexo == "H"):
    print("Seu peso ideal é: ", round(72.7 * altura - 58))
else:
    print("Seu peso ideal é: ", round(62.1 * altura - 44.7))
