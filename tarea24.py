def contar_votos():
    votos = []  
    print("Ingresa los votos uno por uno (finaliza con 0 / introducirlo en el terminal de forma vertical):")

    while True:
        voto = int(input())
        if voto == 0:
            break
        if voto in [1, 2, 3, 4]:  
            votos.append(voto)
        else:
            print("Voto inválido. Solo se aceptan votos para candidatos 1 a 4.")

    total_votos = len(votos)
    print("\nResultados:")
    for candidato in range(1, 5):
        cantidad = votos.count(candidato)
        porcentaje = (cantidad / total_votos) * 100 if total_votos > 0 else 0
        print(f"Candidato {candidato}: {cantidad} votos - {porcentaje:.2f}%")

print(contar_votos())

