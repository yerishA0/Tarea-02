#encoding: UTF-8

# Autor: yerish valdes A01375755
# Descripcion: porcentajes

# A partir de aquí escribe tu programa

hombres=int(input("Hombres inscritos:"))
mujeres=int(input("Mujeres inscritas:"))
total=hombres+mujeres
print("La poblacion total es de:", total)
hombres_porcentaje=(hombres*100)/total
print("porcentaje de hombres:",hombres_porcentaje,"%")
mujeres_porcentaje=(mujeres*100)/total
print("porcentaje de mujeres:",mujeres_porcentaje,"%")