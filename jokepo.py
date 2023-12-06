
from random import randint

vitoria_jogador_humano = 0
vitoria_jogador_humano_2 = 0
vitoria_jogador_computador_1 = 0
vitoria_jogador_computador_2 = 0
derota_jogador_humano = 0
derota_jogador_humano_2 = 0
derota_jogador_computador_1 = 0
derota_jogador_computador_2 = 0
empate_jogador_humano = 0
empate_jogador_humano_2 = 0
empate_jogador_computador_1 = 0
empate_jogador_computador_2 = 0
total_de_jogos_jogador_humano = 0
total_de_jogos_jogador_humano_2 = 0
total_de_jogos_jogador_computador_1 = 0
total_de_jogos_jogador_computador_2 = 0

def menu_de_retorno():
    print("[1] SIM")
    print("[2] NÃO")
    opcao_retorno = int(input("Você deseja retornar ao menu principal?"))
    while opcao_retorno <3 and opcao_retorno:
        if opcao_retorno == 1:
            print("Retornando ao menu principal")
            print("---------------------------")
            inicializando_o_jogo()
        if (opcao_retorno == 2):
            print("Volte sempre")
            break
    else:
        print("Opção errada")
        print("Digite novamente")
             

def menu_do_inicializando_o_jogo():
    print("MENU PRINCIPAL")
    print("[1]HUMANO X HUMANO")
    print("[2]HUMANO X COMPUTADOR")
    print("[3]COMPUTADOR X COMPUTADOR")
    print("[4]SAIR")

def inicializando_o_jogo():
    menu_do_inicializando_o_jogo()
    modo_de_jogo = int(input("Escolha o modo de jogo:"))
    while modo_de_jogo >0 and modo_de_jogo <5:

        if modo_de_jogo == 1:
            print("Modo de jogo escolhido: HUMANO X HUMANO")
            print("---------------------------")
            Humano_x_Humano()
            
        elif modo_de_jogo == 2:
            print("Modo de jogo escolhido: HUMANO X COMPUTADOR")
            print("---------------------------")
            Humano_x_Computador()
        elif modo_de_jogo == 3:
            print("Modo de jogo escolhido: COMPUTADOR X COMPUTADOR")
            print("---------------------------")
            Computador_x_Computador() 
        elif modo_de_jogo == 4:
            print("Volte sempre")
            break       
    else:
        print("Opção Inválida")
        print("Digite novamente")
        inicializando_o_jogo()

def menu_de_modo_de_jogo():
    print("Escolha sua jogada")
    print("[1]PEDRA")
    print("[2]PAPEL")
    print("[3]TESOURA")         

def Humano_x_Humano():
    global vitoria_jogador_humano, vitoria_jogador_humano_2, derota_jogador_humano, derota_jogador_humano_2, empate_jogador_humano, empate_jogador_humano_2, total_de_jogos_jogador_humano, total_de_jogos_jogador_humano_2, porcentual_de_vitorias_jogador_1_modo_de_jogo_1, porcentual_de_vitorias_jogador_2_modo_de_jogo_1    
    menu_de_modo_de_jogo()    
    jogador_1 = int(input("JOGADOR 1:"))
    jogador_2 = int(input("JOGADOR 2:")) 
    while jogador_1 <4 and jogador_1 >0 and (jogador_2 <4 and jogador_2 >0):        
        print("-------------------------")
        print("JO")
        print("KEN")
        print("PÔ")
        print("-------------------------")
        if (jogador_1== 2 and jogador_2 == 1) or (jogador_1 == 3 and jogador_2  == 2) or (jogador_1 == 1 and jogador_2 == 3):
            
            vitoria_jogador_humano+=1
            derota_jogador_humano_2 += 1
            total_de_jogos_jogador_humano  +=1
            total_de_jogos_jogador_humano_2 += 1
            print("O jogador 1 venceu a disputa ")

        elif ((jogador_2  == 2 and jogador_1 == 1) or (jogador_2 == 3 and jogador_1 == 2) or (jogador_2 == 1 and jogador_1 == 3)):
            vitoria_jogador_humano_2 += 1
            derota_jogador_humano += 1
            total_de_jogos_jogador_humano += 1
            total_de_jogos_jogador_humano_2 += 1
            print("O jogador 2 venceu a disputa")
            print("-------------------------")

        else:
            print("Empate")
            empate_jogador_humano+=1
            empate_jogador_humano_2+=1
            total_de_jogos_jogador_humano += 1
            total_de_jogos_jogador_humano_2 += 1


        print("-------------------------")
        print("Jogador 1:")
        print("NÚMEROS DE PARTIDAS:", total_de_jogos_jogador_humano )
        print("VITÓRIAS:", vitoria_jogador_humano)
        print("DERROTAS:", derota_jogador_humano)
        print("EMPATES:", empate_jogador_humano)
        porcentual_de_vitorias_jogador_1_modo_de_jogo_1 = ((vitoria_jogador_humano / total_de_jogos_jogador_humano)) * 100
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_jogador_1_modo_de_jogo_1)
        print("---------------------------")
        print("Jogador 2: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_jogador_humano_2)
        print("VITÓRIAS:", vitoria_jogador_humano_2)
        print("DERROTAS:", derota_jogador_humano_2)
        print("EMPATES:", empate_jogador_humano_2)
        porcentual_de_vitorias_jogador_2_modo_de_jogo_1 = ((vitoria_jogador_humano_2 / total_de_jogos_jogador_humano_2)) * 100
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_jogador_2_modo_de_jogo_1)
        print("---------------------------")
        menu_de_retorno()

    else:
        print("Opção Inválida")
        print("Digite novamente")   
        Humano_x_Humano()    
    

def Humano_x_Computador():
    import random
    menu_de_modo_de_jogo()   
    global vitoria_jogador_humano, vitoria_jogador_computador_1, derota_jogador_humano, derota_jogador_computador_1, empate_jogador_humano, empate_jogador_computador_1, total_de_jogos_jogador_humano, total_de_jogos_jogador_computador_1, porcentual_de_vitorias_jogador_humano_modo_de_jogo_2, porcentual_de_vitorias_computador_modo_de_jogo_2
    jogador_1 = int(input("JOGADOR 1:"))
    while jogador_1<4 and jogador_1 >0:
         
        computador_modo_de_jogo_2 = random.randint(1, 3)
        print("Computador:",computador_modo_de_jogo_2)
         
        print("-------------------------")
        print("JO")
        print("KEN")
        print("PÔ")
        print("-------------------------")

        if (jogador_1 == 2 and computador_modo_de_jogo_2 == 1) or (jogador_1 == 3 and computador_modo_de_jogo_2 == 2) or (jogador_1 == 1 and computador_modo_de_jogo_2 == 3):  
            vitoria_jogador_humano+=1
            derota_jogador_computador_1 += 1
            total_de_jogos_jogador_humano += 1
            total_de_jogos_jogador_computador_1 += 1
            print("O jogador humano venceu a disputa ")
            print("-------------------------")

        elif ((computador_modo_de_jogo_2 == 1 and jogador_1 == 2) or (computador_modo_de_jogo_2 == 3 and jogador_1 == 2) or (computador_modo_de_jogo_2 == 1 and jogador_1 == 3)):
            vitoria_jogador_computador_1 += 1
            derota_jogador_humano += 1
            total_de_jogos_jogador_computador_1 += 1
            total_de_jogos_jogador_humano += 1
            print("O Computador venceu a disputa")
            print("------------------------")
        else:
            empate_jogador_humano+=1
            empate_jogador_computador_1+=1
            total_de_jogos_jogador_computador_1 += 1
            total_de_jogos_jogador_humano += 1
            print("Empate")
            print("-------------------------")
       
        print("Jogador Humano: ")
        print("NÚMEROS DE PARTIDAS:", total_de_jogos_jogador_humano)
        print("DERROTAS:", derota_jogador_humano)
        print("VITÓRIAS:", vitoria_jogador_humano)
        print("EMPATES:", empate_jogador_humano)
        porcentual_de_vitorias_jogador_humano_modo_de_jogo_2 = (( vitoria_jogador_humano / total_de_jogos_jogador_humano)) * 100
        print("PORCENTUAL DE VITÓRIAS :", porcentual_de_vitorias_jogador_humano_modo_de_jogo_2)
        print("---------------------------")
        print("Computador: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_jogador_computador_1)
        print("VITÓRIAS:",  vitoria_jogador_computador_1) 
        print("DERROTAS:", derota_jogador_computador_1)
        print("EMPATES:", empate_jogador_computador_1)
        porcentual_de_vitorias_computador_modo_de_jogo_2 = ((vitoria_jogador_computador_1 /total_de_jogos_jogador_computador_1) * 100)
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_computador_modo_de_jogo_2)
        print("---------------------------")
        menu_de_retorno()
    else:
        print("Opção Inválida")
        print("Digite novamente")
        Humano_x_Computador()


def Computador_x_Computador():
    import random
    global vitoria_jogador_computador_1, vitoria_jogador_computador_2, derota_jogador_computador_1, derota_jogador_computador_2, empate_jogador_computador_1, empate_jogador_computador_2, total_de_jogos_jogador_computador_1, total_de_jogos_jogador_computador_2, porcentual_de_vitorias_computador_1_modo_de_jogo_3, porcentual_de_vitorias_computador_2_modo_de_jogo_3
    menu_de_modo_de_jogo() 
    computador_1_modo_de_jogo_3 = random.randint(1, 3)
    computador_2_modo_de_jogo_3 = random.randint(1, 3)
    print("-------------------------")
    print("COMPUTADOR_1:",computador_1_modo_de_jogo_3)
    print("COMPUTADOR_2:",computador_2_modo_de_jogo_3)
    print("-------------------------")
    print("JO")
    print("KEN")
    print("PÔ")
    print("-------------------------")
    if (computador_1_modo_de_jogo_3 == 2 and computador_2_modo_de_jogo_3 == 1) or (computador_1_modo_de_jogo_3 == 3 and computador_2_modo_de_jogo_3 == 2) or (computador_1_modo_de_jogo_3 == 1 and computador_2_modo_de_jogo_3 == 3):
        vitoria_jogador_computador_1+=1
        derota_jogador_computador_2+=1
        total_de_jogos_jogador_computador_1+=1
        total_de_jogos_jogador_computador_2+=1
        print("O computador 1 venceu a disputa ")
        print("-------------------------")
    
    elif ((computador_2_modo_de_jogo_3 == 2 and computador_1_modo_de_jogo_3 == 1) or (computador_2_modo_de_jogo_3 == 1 and computador_1_modo_de_jogo_3 == 3) or (computador_2_modo_de_jogo_3 == 3 and computador_1_modo_de_jogo_3 == 2)):
    
        vitoria_jogador_computador_2+=1
        derota_jogador_computador_1+=1
        total_de_jogos_jogador_computador_1+=1
        total_de_jogos_jogador_computador_2+=1
        print("O Computador 2 venceu a disputa")
        print("-------------------------")
    else:
        empate_jogador_computador_1+=1
        empate_jogador_computador_2+=1
        total_de_jogos_jogador_computador_1+=1
        total_de_jogos_jogador_computador_2+=1
        print("Empate")

    print("Computador 1: ")
    print("NÚMEROS DE PARTIDAS:", total_de_jogos_jogador_computador_1)
    print("VITÓRIAS:", vitoria_jogador_computador_1 )
    print("DERROTAS:",   derota_jogador_computador_1)
    print("EMPATES:", empate_jogador_computador_1)
    porcentual_de_vitorias_computador_1_modo_de_jogo_3 = ((vitoria_jogador_computador_1/total_de_jogos_jogador_computador_1)) * 100
    print("PORCENTUAL DE VITÓRIAS :",porcentual_de_vitorias_computador_1_modo_de_jogo_3)
    print("---------------------------")
    print("Computador 2: ")
    print("NÚMEROS DE PARTIDAS:", tdotal_de_jogos_jogador_computador_2)
    print("VITÓRIAS:",  vitoria_jogador_computador_2)
    print("DERROTAS:", derota_jogador_computador_2)
    print("EMPATES:", empate_jogador_computador_2)
    porcentual_de_vitorias_computador_2_modo_de_jogo_3 = ( vitoria_jogador_computador_2 / total_de_jogos_jogador_computador_2 ) * 100
    print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_computador_2_modo_de_jogo_3)
    print("-------------------------")
    menu_de_retorno()
 
inicializando_o_jogo()
