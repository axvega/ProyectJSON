# funciones.py

def listar_informacion(animales):
    print("\n" * 50)  # Limpiar pantalla (aunque en algunos entornos no funciona)
    print("La lista de información es la siguiente:")
    print("-" * 80)
    # Cabecera única
    print(f"{'Nombre':<25} {'Altura (m)':<12} {'Alimento':<15} {'Hábitats':<20} {'Conservación':<20} {'Vida (años)':<12}")
    print("-" * 80)
    
    for animal in animales["animales"]:
        nombre = animal["nombre"]
        altura = animal["caracteristicas_fisicas"]["altura_promedio_m"]
        alimento = animal["dieta"]["alimento_principal"]
        habitats = ", ".join(animal["habitats"])
        estado_conservacion = animal["estado_conservacion"]["nivel_amenaza"]
        vida_promedio = animal["vida_promedio_años"]
        # Alineamos cada campo con un ancho fijo
        print(f"{nombre:<25} {altura:<12.1f} {alimento:<15} {habitats:<20} {estado_conservacion:<20} {vida_promedio:<12}")
    print("-" * 80)
    print("Fin de la lista")

def contar_poblacion(animales):
    menor_10000 = []
    mayor_10000 = []
    
    for animal in animales["animales"]:
        poblacion = animal["estado_conservacion"]["poblacion_estimada"]
        nombre = animal["nombre"]
        if poblacion < 10000:
            menor_10000.append(nombre)
        else:
            mayor_10000.append(nombre)
    
    print("Animales con población < 10,000:")
    print("-" * 50)
    print(f"{'Nombre':<25}")
    print("-" * 50)
    for animal in menor_10000:
        print(f"{animal:<25}")
    print(f"Total: {len(menor_10000)}")
    
    print("\nAnimales con población >= 10,000:")
    print("-" * 50)
    print(f"{'Nombre':<25}")
    print("-" * 50)
    for animal in mayor_10000:
        print(f"{animal:<25}")
    print(f"Total: {len(mayor_10000)}")

def filtrar_por_peso(animales):
    peso_min = float(input("Ingrese el peso mínimo: "))
    peso_max = float(input("Ingrese el peso máximo: "))
    print("-" * 70)
    print(f"{'Nombre':<25} {'Peso (kg)':<15} {'Frecuencia de alimentación':<30}")
    print("-" * 70)
    
    for animal in animales["animales"]:
        peso = animal["caracteristicas_fisicas"]["peso_promedio_kg"]
        if peso_min <= peso <= peso_max:
            nombre = animal["nombre"]
            frecuencia = animal["dieta"]["frecuencia_alimentacion"]
            print(f"{nombre:<25} {peso:<15.1f} {frecuencia:<30}")

def buscar_por_alimento(animales):
    alimento = input("Ingrese un alimento: ")
    print("-" * 70)
    print(f"{'Nombre':<25} {'Tipo':<15} {'Hábitats':<30}")
    print("-" * 70)
    
    for animal in animales["animales"]:
        principal = animal["dieta"]["alimento_principal"]
        otros = animal["dieta"]["otros_alimentos"]
        if principal == alimento or alimento in otros:
            nombre = animal["nombre"]
            tipo = animal["tipo"]
            habitats = ", ".join(animal["habitats"])
            print(f"{nombre:<25} {tipo:<15} {habitats:<30}")

def continente_poblacion(animales):
    continente = input("Ingrese un continente: ")
    frecuencia = input("Ingrese una frecuencia de alimentación: ")
    animales_encontrados = []
    
    for animal in animales["animales"]:
        if (continente in animal["continentes"] and 
            animal["dieta"]["frecuencia_alimentacion"] == frecuencia):
            animales_encontrados.append({
                "nombre": animal["nombre"],
                "peso": animal["caracteristicas_fisicas"]["peso_promedio_kg"],
                "poblacion": animal["estado_conservacion"]["poblacion_estimada"]
            })
    
    animales_encontrados.sort(key=lambda x: x["peso"], reverse=True)
    print(f"Animales en {continente} con frecuencia {frecuencia}:")
    print("-" * 70)
    print(f"{'Nombre':<25} {'Peso (kg)':<15} {'Población':<15}")
    print("-" * 70)
    
    for animal in animales_encontrados:
        print(f"{animal['nombre']:<25} {animal['peso']:<15.1f} {animal['poblacion']:<15}")
    print(f"Total: {len(animales_encontrados)}")