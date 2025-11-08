import os
import time

valor1 = 0
enfeite = "| ---------- ENDEREÇO CLASS FULL ---------- | \n"
print("| ---------- CALCULADORA DE IP ---------- |")
ip01, ip02, ip03, ip04 = map(int, input("DIGITE O SEU ENDEREÇO IP: ").split("."))
lista_ip = [ip01, ip02, ip03, ip04]

while ip01 > 255 or ip02 > 255 or ip03 > 255 or ip04 > 255:
    print("O IP digitado tem que ser menor que 256!")
    ip01, ip02, ip03, ip04 = map(int, input("DIGITE O SEU ENDEREÇO IP: ").split("."))
mascara = int(input("DIGITE A MASCARA DO ENDEREÇO: "))
while mascara > 32 or mascara < 0:
    print("Mascara indisponível! Digite novamente:")
    mascara = int(input("DIGITE A MASCARA DO ENDEREÇO: "))
else:
    print("CALCULANDO...")
    time.sleep(3)
    os.system('cls')


    print(f"-=-=-=-= DIGITOS -=-=-=-= \nENDEREÇO: {ip01}.{ip02}.{ip03}.{ip04} \nMASCARA: {mascara}") 
    hosts = (2**(32-mascara))-2
    print(f"QUANTIDADE DE HOSTS: {hosts}")

    if ip01 == 192 or ip01 == 172 or ip01 == 10:
        print("IP DO TIPO -PRIVADO-")
    else:
        print("IP DO TIPO -PUBLICO-")

    if ip01 >= 1 and ip01 <=127 or 0 <= mascara <= 8:
        print("CLASSE - A")
        sub_rede = 2**(mascara-8)
        if mascara-8 < 0:
            sub_rede = 2**((mascara-8)*(-1))
    elif ip01 >= 128 and ip01 <=191 or 9 <= mascara <= 16:
        print("CLASSE - B")
        sub_rede = 2**(mascara-16)
        if mascara-16 < 0:
            sub_rede = 2**((mascara-16)*(-1))
    elif ip01 >= 192 and ip01 <=223 or 17 <= mascara <= 24:
        print("CLASSE - C")
        sub_rede = 2**(mascara-24)
        if mascara-24 < 0:
            sub_rede = 2**((mascara-24)*(-1))
    else:
        print("CLASSE - Acima da classe C!!")
    print(f"TOTAL SUB REDES: {sub_rede}")

    if mascara == 24:
        print(f"{enfeite} \nENDEREÇO DA REDE: {ip01}.{ip02}.{ip03}.0 \nFIRST HOST: {ip01}.{ip02}.{ip03}.{0+1} \nLAST HOST: {ip01}.{ip02}.{ip03}.254 \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{ip03}.255")
    elif mascara == 16:
        print(f"{enfeite} \nENDEREÇO DA REDE: {ip01}.{ip02}.0.0 \nFIRST HOST: {ip01}.{ip02}.0.{0+1} \nLAST HOST: {ip01}.{ip02}.255.254 \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.255.255")
    elif mascara == 8:
        print(f"{enfeite} \nENDEREÇO DA REDE: {ip01}.0.0.0 \nFIRST HOST: {ip01}.0.0.{0+1} \nLAST HOST: {ip01}.255.255.254 \nENDEREÇO DE BROADCAST: {ip01}.255.255.255")
    elif mascara == 32:
        print(f"{enfeite} \nENDEREÇO DA REDE: {ip01}.{ip02}.{ip03}.{ip04} \nFIRST HOST: {ip01}.{ip02}.{ip03}.{ip04+1} \nLAST HOST: 255.255.255.254 \nENDEREÇO DE BROADCAST: 255.255.255.255")
    else:
        print("| ----------- ENDEREÇO CLASS LESS ---------- | \n")

        if 0 < mascara < 8:
            passo = 2**(8-mascara)
            if ip02 == passo or ip02 == passo+1:
                for i in range(1, ip01, passo):
                    valor1 = i -1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {valor1}.0.0.0 \nFIRST HOST: {valor1}.0.0.1 \nLAST HOST: {broad}.255.255.254 \nENDEREÇO DE BROADCAST: {broad}.255.255.255")

            elif mascara == 1:
                pulo = [0, 128]
                if ip01 >0 and ip01 <128:
                    print(f"ENDEREÇO DE REDE: {pulo[0]}.0.0.0 \nFIRST HOST: {pulo[0]}.0.0.1 \nLAST HOST: {pulo[1] - 1}.255.255.254 \nENDEREÇO DE BROADCAST: {pulo[1] - 1}.255.255.255")
                else:
                    print(f"ENDEREÇO DE REDE: {pulo[1]}.0.0.0 \nFIRST HOST: {pulo[1]}.0.0.1 \nLAST HOST: {256 - 1}.255.255.254 \nENDEREÇO DE BROADCAST: {256 - 1}.255.255.255")
            else:
                for i in range(1, ip01+passo, passo):
                    valor1 = i -1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {valor1}.0.0.0 \nFIRST HOST: {valor1}.0.0.1 \nLAST HOST: {broad}.255.255.254 \nENDEREÇO DE BROADCAST: {broad}.255.255.255")
            
        elif mascara > 8 and mascara < 16: 
            passo = 2**(16-mascara)
            if ip02 == passo or ip02 == passo+1:
                for i in range(1, ip02*2, passo):
                    valor1 = i -1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{valor1}.0.0 \nFIRST HOST: {ip01}.{valor1}.0.1 \nLAST HOST: {ip01}.{broad}.255.254 \nENDEREÇO DE BROADCAST: {ip01}.{broad}.255.255")
            else:
                for i in range(1, ip02, passo):
                    valor1 = i -1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{valor1}.0.0 \nFIRST HOST: {ip01}.{valor1}.0.1 \nLAST HOST: {ip01}.{broad}.255.254 \nENDEREÇO DE BROADCAST: {ip01}.{broad}.255.255")
        elif mascara >16 and mascara < 24:
            passo = 2**(24-mascara)
            if ip03 == passo:
                for i in range(1, ip03*2, passo):
                    valor1 = i - 1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{ip02}.{valor1}.0 \nFIRST HOST: {ip01}.{ip02}.{valor1}.1 \nLAST HOST: {ip01}.{ip02}.{broad}.254 \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{broad}.255")
            elif ip03 == passo+1:
                for i in range(1, ip03+passo, passo):
                    valor1 = i - 1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{ip02}.{valor1}.0 \nFIRST HOST: {ip01}.{ip02}.{valor1}.1 \nLAST HOST: {ip01}.{ip02}.{broad}.254 \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{broad}.255")
            else:
                for i in range(1, ip03, passo):
                    valor1 = i - 1
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{ip02}.{valor1}.0 \nFIRST HOST: {ip01}.{ip02}.{valor1}.1 \nLAST HOST: {ip01}.{ip02}.{broad}.254 \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{broad}.255")
        elif mascara > 24 and mascara < 32:
            passo = 2**(32-mascara)
            if ip04 == passo or ip04 == passo+1:     
                for i in range(0, ip04+passo, passo):
                    valor1 = i 
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{ip02}.{ip03}.{valor1} \nFIRST HOST: {ip01}.{ip02}.{ip03}.{valor1+1} \nLAST HOST: {ip01}.{ip02}.{ip03}.{(broad)-1} \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{ip03}.{broad}")
            else:
                for i in range(0, ip04, passo):
                    valor1 = i 
                broad = valor1+passo-1
                print(f"ENDEREÇO DE REDE: {ip01}.{ip02}.{ip03}.{valor1} \nFIRST HOST: {ip01}.{ip02}.{ip03}.{valor1+1} \nLAST HOST: {ip01}.{ip02}.{ip03}.{(broad)-1} \nENDEREÇO DE BROADCAST: {ip01}.{ip02}.{ip03}.{broad}")
        else:
            print("IMPOSSIVEL CALCULAR VALORES MAIORES QUE 32 E MENORES QUE 8")
