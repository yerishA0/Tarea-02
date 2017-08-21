#encoding: UTF-8

# Autor: yerish valdes A01375755
# Descripcion: cuenta total por una comida

# A partir de aquí escribe tu programa
costo=int(input("Costo de la comida:"))
propina=costo*0.12
print("propina:",propina)
iva=costo*0.16
print("IVA:",iva)
cuenta_total=costo+propina+iva
print("la cuenta total es: ",cuenta_total)