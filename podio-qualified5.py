def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3):
    podio1 = int(tempo_chegada1)
    podio2 = int(tempo_chegada2)
    podio3 = int(tempo_chegada3)
    if (podio1 == 90) or (podio2 == 90) or (podio3 == 90):
        return print(f"-1 {podio2} minutos")
    elif(podio1 == 110) or (podio2 == 110) or (podio3 == 110):
        return print(f"-1 {podio3} minutos")
    elif (podio1 == 120) or (podio2 == 120) or (podio3== 120):
        return print(f"-1 {podio1} minutos")


podio_olimpico(120,90,110)


