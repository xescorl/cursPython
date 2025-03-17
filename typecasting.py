# Typecasting

nom = "joan"
edat = 25
promig = 7.5
es_estudiant = True

# Float -> Integer
print("Float -> Integer")
print(f"{promig} -> {int(promig)}")
# Integer -> String
print("Integer -> String")
print(f"{edat} -> {str(edat)}")
print(f"Integer + Integer = {edat + edat}")
print(f"Str + Str = {str(edat) + str(edat)}")
print(f"Str += Str = {str(edat) + "1"}")
# String -> Integer
print("String -> Integer")
print(f"{nom} -> {int(promig)}")
# Float -> Integer
print("String -> Bool")
print(f"{nom} -> {bool(nom)}")
print("String buit -> Bool")
print(f"{""} -> {bool("")}")
# Integer -> Float
print("Integer -> Float")
print(f"{edat} -> {float(edat)}")
