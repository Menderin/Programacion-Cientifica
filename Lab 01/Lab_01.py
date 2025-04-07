import math
import matplotlib.pyplot as plt
# calculo de distancia
def distancia_euclidea(punto_frame_1, punto_frame_2):
    x1, y1 = punto_frame_1
    x2, y2 = punto_frame_2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cálculo de la rapidez
def rapidez(punto_1, punto_2, tiempo):
  distancia = distancia_euclidea(punto_1, punto_2)
  rapid = distancia/tiempo
  return rapid



with open("datos.txt", 'r', encoding= "utf-8") as archivo:
    for i in range(4):
        archivo.readline()

    
    personas = {}

    for linea in archivo:
        #leer
        datos = linea.split()
        id = int(datos[0])
        frame = int(datos[1])
        x = float(datos[2])
        y = float(datos[3])
        z = float(datos[4])
        #crear keys del diccionario
        if id not in personas:
            personas [id] = {"datos" : []}
        #valores de las keys
        personas [id]["datos"].append((frame,x,y,z))
        
        
    #ordenar por frame
    for id in personas:
        personas[id]["datos"] = sorted(personas[id]["datos"], key=lambda frame:frame[0])
        #print(personas[1])
        #print(personas.keys())
    
    
    rapidez_media = []

    #calccular velocidad media de todas las personas 
    for id in personas:
        lista_rapidez = []
        tiempo = 1.0/25.0

        punto1 = personas[id]["datos"][0][1:3] #x,y
        
        
        for p in personas[id]["datos"][1:]:
            punto2 = p[1:3]  # x, y del segundo frame
            lista_rapidez.append(rapidez(punto1, punto2, tiempo))  # rapidez
            punto1 = punto2  

        
        rapidez_media.append(sum(lista_rapidez)/len(lista_rapidez))
        #rapidez_media = sum(lista_rapidez)/len(lista_rapidez)
        print(f"La rapidez media de la persona {id} es: {sum(lista_rapidez)/len(lista_rapidez)}[m/seg]")
    print()
    print(f"La rapidez media de todas las personas es: {sum(rapidez_media)/len(rapidez_media)}[m/seg]")


    #Graficas
    # Dibujar línea entre los dos puntos
    fig, ax = plt.subplots(figsize=(10, 6))
    #Grafica de ejemplo
    for id in list(personas.keys())[:10]: #aqui obtenemos todas las keys (los id's) y los convertimos a lista, de los cuales
                                          # tomamos los primeros 10 para graficar, se convierte a lista debido a que, como tal, 
                                          # no se puede hacer slicing a las keys de un diccionario
        x_vals = [dato[1] for dato in personas[id]["datos"]]
        y_vals = [dato[2] for dato in personas[id]["datos"]]

        ax.plot(x_vals, y_vals, marker='o', linestyle='-', label=f'Persona {id}')
    # Etiquetas en los puntos
    #for i, dato in enumerate(persona_1):
    #    ax.text(dato[1], dato[2] + 0.005, f"{dato[0]}", ha='center')


    # Configuración del gráfico
    ax.set_title("Línea entre puntos")
    ax.set_xlabel("Posición X")
    ax.set_ylabel("Posición Y")
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 5)
    ax.grid(True)
    ax.legend()
    ax.set_aspect('equal')

    plt.show()

    #Revisar punto 3 y 4 del colab

    # Crear un histograma de todas las velocidades
    plt.hist(rapidez_media, bins=40, color='blue', edgecolor='black')  # bins define el número de intervalos

    # Agregar títulos y etiquetas
    plt.title('Histograma de velocidades de las personas')
    plt.xlabel('Velocidades [m/seg]')
    plt.ylabel('Frecuencia')

    # Mostrar el histograma
    plt.show()

    #heatmap 
    #actualizar el heatmap
    #heatmap, xedges, yedges = np.histogram2d(x_all, y_all, bins=50, range=[[-6, 6], [0, 5]])
    
    # Paso 3: Mostrar el mapa de calor
    #plt.imshow(heatmap.T, origin='lower', cmap='hot', extent=[-6, 6, 0, 5], aspect='auto')
    #plt.colorbar(label='Número de personas')
    #plt.title('Mapa de calor de zonas más concurridas')
    #plt.xlabel('Posición X')
    #plt.ylabel('Posición Y')
    #plt.grid(False)
    #plt.show()