frase = "No seu mínimo, faça seu melhor"
vogais = ("aeiouAEIOU")
consoantes = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

cont_vogais = 1
cont_consoantes = 1

for letter in frase:
  if letter in vogais:
        cont_vogais += 1
  elif letter in consoantes:
        cont_consoantes += 1

print(f"Número de vogais: {cont_vogais}")
print(f"Número de consoantes: {cont_consoantes}")