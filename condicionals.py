edat = int(input("Quants anys tens? "))
if edat >= 18:
    print("Ets major d'edat.")
elif edat >= 0 and edat < 18:
    print("Ets menor d'edat.")
elif edat == 0:
    print("Ets un nadó.")
elif edat > 100:
    print("Ets un supervivent.")
elif edat >= 30 and edat < 100:
    print("oldass.")
elif edat < 0:
    print("No pots tenir una edat negativa.")
else:
    print("No pots tenir una edat negativa.")

resposta = input("Tens ganes de jugar a un joc? (s/n) ")
if resposta == "s":
    print("Comencem!")
else:
    print("Fins la propera!")

nom = input("com et dius?")
if not bool(nom):
    print("no has escrit res")
else:
    print(f"Hola, {nom}!")