# Bienvenida e instrucciones.

print("¡Hola! Soy una calculadora de licencias Creative Commons. Mi función es decirte si podés realizar una obra derivada a partir de una o más obras originales. Vos me tenés que indicar la licencia de la obra u obras originales. Yo te digo si podés hacer la obra derivada y, en ese caso, qué licencia o licencias podés colocarle a tu obra derivada.\n---")

# Lista de licencias para chequear input.

licencias = ["dominiopublico", "by", "bysa", "bynd", "bync", "byncsa", "byncnd"]

# Declaración de licencias para calcular compatibilidad.

dp = "dominiopublico"
by = "by"
bysa = "bysa"
bynd = "bynd"
bync = "bync"
byncsa = "byncsa"
byncnd = "byncnd"

def calculadora():
    while True:
        n = 0
        lista_de_licencias = []
        while True:
            if n < 1:
                licencia_input = input("Ingresá la licencia de la %dª obra: " % (n + 1))
            else:
                licencia_input = input("Ingresá la licencia de la %dª obra o tipeá 'Listo': " % (n + 1))
            licencia_input = licencia_input.strip()
            licencia_input = licencia_input.lower()
            licencia_input = licencia_input.replace(" ", "")
            licencia_input = licencia_input.replace("-", "")
            licencia_input = licencia_input.replace("cc", "")
            licencia_input = licencia_input.replace("ú", "u")
            licencia_input = licencia_input.replace("0", "dominiopublico")
            licencia_input = licencia_input.replace("zero", "dominiopublico")
            licencia_input = licencia_input.replace("cero", "dominiopublico")
            
            if licencia_input == "listo":
                break
            if licencia_input not in licencias:
                print("Ingresá una licencia válida. Por ejemplo: CC BY-SA")
                continue
            n = n + 1
            lista_de_licencias.append(licencia_input)
            
        ok = True

        if bynd in lista_de_licencias or byncnd in lista_de_licencias:
            print("\033[1m""- Estas obras no se pueden combinar en una obra derivada, dado que una o más de las obras tienen una licencia ND, que no admite obras derivadas.""\033[0m")
            ok = False
        if bysa in lista_de_licencias and byncsa in lista_de_licencias:
            print("\033[1m""- Las obras con licencias CCBY-SA y CCBY-NC-SA no se pueden combinar entre sí, dado que ambas, por su parte, exigen que la obra derivada tenga una licencia igual.""\033[0m")
            ok = False
        if bync in lista_de_licencias and bysa in lista_de_licencias:
            print("\033[1m""- Las obras con licencias CCBY-NC y CCBY-SA no se pueden combinar entre sí, dado que la licencia CCBY-NC no permite los usos comerciales y la licencia CCBY-SA exige que la obra derivada tenga una licencia igual que permite los usos comerciales.""\033[0m")
            ok = False
        
        if ok is False:
            seguir = input("¿Querés hacer otra consulta? (Sí / No) ")
            if seguir in ["no" , "No" , "n" , "N"]:
                print("¡Hasta luego!")
                quit()
                   
        if ok is True:
            print("\033[1m""- Podés realizar sin problemas una obra derivada a partir de esta obra u obras.""\033[0m")
            if bysa in lista_de_licencias:
                print("\033[1m""- La obra derivada debe tener una licencia CC BY-SA.""\033[0m")
            elif byncsa in lista_de_licencias:
                print("\033[1m""- La obra derivada debe tener una licencia CC BY-NC-SA.""\033[0m")
            elif bync in lista_de_licencias:
                print("\033[1m""- La obra derivada puede llevar una licencia CC BY-NC, CC BY-NC-SA o CC BY-NC-ND. Es técnicamente válido, aunque no recomendado, colocar a la obra derivada una licencia que permita los usos comerciales.""\033[0m")
            elif by in lista_de_licencias:
                print("\033[1m""- La obra derivada puede llevar cualquier licencia. Es técnicamente válido, aunque no recomendado, dedicar al dominio público la obra derivada.""\033[0m")
            else:
                print("La obra derivada puede llevar cualquier licencia o puede dedicarse al dominio público.")
        
            seguir = input("¿Querés hacer otra consulta? (Sí / No) ")
            if seguir in ["no" , "No" , "n" , "N"]:
                print("¡Hasta luego!")
                quit()

repetir = 1
while repetir == 1:        
    calculadora()
