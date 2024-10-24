#Creacion de una Calculadora de consumo energia interna.
from time import process_time_ns

#titulo
print(" ")
print("Calculadora de Luz Medidor Interno")
print("------------------------------------")
print(" ")

print("Calculo Medidor Interno")
print(" ")

l_ant = float(input("Lectura Anterior : "))
l_act = float(input("Lectura Actual : "))
p_kwh = float(input("Precio kWh : "))

l_Interna = (l_act - l_ant) * p_kwh
print("Sub Total Interno a pagar :",l_Interna)

print(" ")
print("Calculo de Importes")
print(" ")

ene_act = float(input("Ingrese Energia Activa : "))
sub_tt = float(input("Ingrese Sub total : "))
tt_rec = float(input("Ingrese Total Recibo : "))
num_per = float(input("Ingrese Numero de Personas : "))

imp_1 = sub_tt - ene_act
imp_2 = tt_rec - sub_tt

if num_per > 1 :
    t_imp = (imp_1 + imp_2) / num_per
    print("Total de Importe :", t_imp)
else :
    t_imp = (imp_1 + imp_2)
    print("Total de Importe :", t_imp)

print("")
print("Total a pagar :", l_Interna + t_imp)




