#En este programa, hara una simulacion de procesos, el usuario ingresara un numero de n procesos y entrara en ejecucion y se dividira en lotes.
#Cada 5 procesos son 1 lote.
#Los resultados se guardara en en .txt

import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
tiempo_acumulado = 0  # Inicializa una variable global que acumulará el tiempo durante la ejecución.
lotes = 0  # Inicializa una variable global para llevar la cuenta de los lotes de procesos.
procesos_ejecutados = 0 #Inicializa una variable global para llevar la cuenta de los procesos en ejecucion.

# Crear archivos vacíos para resultados y procesos
with open("resultados.txt", "w"):  # Abre el archivo 'resultados.txt' en modo escritura (crea uno si no existe).
    pass  # No realiza ninguna operación, ya que solo se usa para asegurarse de que el archivo 'resultados.txt' esté vacío.
with open("procesos.txt", "w"):  # Similar al anterior, crea o vacía el archivo 'procesos.txt'.
    pass

# Función para validar si la entrada es un número entero
def validar_numero(entrada):
    try:
        int(entrada)  # Intenta convertir la entrada a un entero.
        return True  # Si tiene exito, la entrada es un número entero, y devuelve True.
    except ValueError:
        return False  # Si ocurre una excepción (ValueError), la entrada no es un número entero y devuelve False.

# Función para guardar resultados en el archivo 'resultados.txt'
def guardar_resultados(resultados):
    lotes = 0  # Inicializa una variable para llevar la cuenta de los lotes.
    x = 10  # Inicializa una variable para contar cada 10 resultados y crear un nuevo lote.
    with open("resultados.txt", "a") as file:  # Abre el archivo 'resultados.txt' en modo escritura (append).
        for resultado in resultados:
            if x == 10:  # Cada 10 resultados, crea un nuevo lote.
                lotes += 1
                x = 0
                file.write(f"\n======= LOTE: {lotes} =======\n\n")  # Encabezado del lote.
            file.write(f"{resultado}\n")  # Escribe el resultado en el archivo.
            x += 1
        file.write("\n")  # Línea en blanco después de todos los resultados.

# Función para guardar procesos en el archivo 'procesos.txt'
def guardar_procesos(procesos):
    lote = 0  # Inicializa una variable para llevar la cuenta de los lotes de procesos.
    y = 5  # Inicializa una variable para contar cada 5 procesos y crear un nuevo lote.
    with open("procesos.txt", "a") as file:  # Abre el archivo 'procesos.txt' en modo escritura (append).
        for proceso in procesos:
            if y == 5:  # Cada 5 procesos, crea un nuevo lote.
                lote += 1
                y = 0
                file.write(f"\n======= LOTE: {lote} =======\n\n")  # Encabezado del lote.
            file.write(f"Proceso {proceso['NumProceso']}: {proceso['Nombre']}, {proceso['Num1']} {proceso['Operacion']} {proceso['Num2']} \nTiempo: {proceso['Tiempo']}s\n")
            y += 1
        file.write("\n")  # Línea en blanco después de todos los procesos.

# Función para generar procesos aleatorios
def generar_procesos():
    global procesosfaltantes, lotes  # Accede a las variables globales 'procesosfaltantes' y 'lotes'.
    cantidad_procesos = campo_generar.get()  # Obtiene la cantidad de procesos desde el campo de entrada.
    if validar_numero(cantidad_procesos):  # Verifica si la cantidad de procesos es un número válido.
        cantidad_procesos = int(cantidad_procesos)  # Convierte la cantidad de procesos a un entero.
        lotes = (cantidad_procesos // 5)  # Calcula la cantidad de lotes necesarios.
        procesos = []  # Inicializa una lista para almacenar los procesos generados.
        lote = 0
        label_lotes_restantes.config(text=f"Lotes Restantes: {lotes}")  # Actualiza la etiqueta en la interfaz.
        for i in range(cantidad_procesos):
            # Genera datos aleatorios para cada proceso
            nombre_aleatorio = random.choice(["Jose", "Carlos", "Carolina", "Juan"])
            operacion_aleatoria = random.choice(["+", "-", "*", "/"])
            tiempo_aleatorio = random.randint(5, 13)
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            if (i + 1) % 5 == 0:
                lote += 1
            nuevo_proceso = {"NumProceso": i + 1, "Nombre": nombre_aleatorio, "Operacion": operacion_aleatoria,"Num1": num1, "Num2": num2, "Tiempo": tiempo_aleatorio,"Lote": lote} #Crea un diccionario con los datos generados aleatoriamente
            procesos.append(nuevo_proceso)  # Agrega el nuevo proceso a la lista de procesos.
            # Imprime todos los procesos almacenados en la lista de procesos
        guardar_procesos(procesos)  # Llama a la función para guardar los procesos en el archivo.
        ejecutar_proceso(procesos)  # Llama a la función para ejecutar los procesos.
    else:
        messagebox.showerror("Error", "Ingresa un número válido en el campo de Número de procesos")  # Muestra un mensaje de error si la cantidad de procesos no es válida.


# Función para ejecutar el proceso actual y actualizar la interfaz gráfica

def ejecutar_proceso(procesos):
    global tiempo_acumulado, lotes  # Accede a las variables globales 'tiempo_acumulado' y 'lotes'.
    
    if procesos:  # Verifica si hay procesos restantes en la lista.
        proceso_actual = procesos.pop(0)  # Obtiene el primer proceso de la lista y lo remueve.     
        cuadro_enProceso.config(text=f"Proceso Actual: {proceso_actual['NumProceso']}, {proceso_actual['Nombre']}, {proceso_actual['Num1']} {proceso_actual['Operacion']} {proceso_actual['Num2']} \nTiempo Restante: {proceso_actual['Tiempo']}s")
        
        # Función interna para actualizar el tiempo restante y continuar con el siguiente proceso
        def actualizar_tiempo():
            global tiempo_acumulado, lotes, procesos_ejecutados # Accede a las variables globales 'tiempo_acumulado' y 'lotes'.
            if procesos_ejecutados == 0:
                procesos_ejecutados = 4
            proceso_actual["Tiempo"] -= 1  # Reduce el tiempo restante del proceso en 1 segundo.
            tiempo_acumulado += 1  # Aumenta el tiempo acumulado en 1 segundo.
            cuadro_enProceso.config(text=f"Proceso: {proceso_actual['NumProceso']}.  {proceso_actual['Nombre']}, {proceso_actual['Num1']} {proceso_actual['Operacion']} {proceso_actual['Num2']} \nTiempo Restante: {proceso_actual['Tiempo']}s")
            cuadro_procesos.config(text=" ") # Actualiza el cuadro de procesos
            
            if len(procesos) // 5 > 0: #Verifica que haya mas de un lote, como usa cuantos procesos tiene la lista principal se actualiza cada que sale un proceso
                label_procesos_restantes.config(text=f"Procesos Restantes: {procesos_ejecutados}") #Aqui imprime la variable de control para imprimir los procesos ejecutados 
            else:  #En caso de nada más haber un lote pendiente se toma la longitud de la lista, esto en caso de a haber un lote no completo se imprime aquí, ya que toma los lotes restantes
                label_procesos_restantes.config(text=f"Procesos Restantes: {len(procesos)}") # Se imprime los procesos restantes

            for proceso in procesos[:procesos_ejecutados]: #Crea un bucle for para imprimir los procesos de la lista principal con un limite de los procesos ejecutados para que nada más imprima 5
                cuadro_procesos.config(text=cuadro_procesos.cget("text") + f"\nProceso {proceso['NumProceso']}: {proceso['Nombre']}, {proceso['Num1']} {proceso['Operacion']} {proceso['Num2']} \nTiempo: {proceso['Tiempo']}s")
            
            if proceso_actual["Tiempo"] > 0: #Verifica que aun queda tiempo
                reloj_global.config(text=f"Reloj Global:\n{tiempo_acumulado}s") # Actualiza el reloj global
                ventana.after(1000, actualizar_tiempo)  # Llama a la función después de 1000 ms (1 segundo).
            else:
                # Calcular resultado y mostrar en la interfaz
                resultado = eval(str(proceso_actual['Num1']) + proceso_actual['Operacion'] + str(proceso_actual['Num2']))
                resultado_formateado = "{:.2f}".format(resultado)
                if proceso_actual['NumProceso'] % 5 == 0:
                    lotes -= 1
                procesos_ejecutados -= 1
                label_lotes_restantes.config(text=f"Lotes Restantes: {lotes}")
                cuadro_resultados.config(text=cuadro_resultados.cget("text") + f"\nProceso {proceso_actual['NumProceso']}: {proceso_actual['Nombre']}, {proceso_actual['Num1']} {proceso_actual['Operacion']} {proceso_actual['Num2']} \nResultado: {resultado_formateado}")
                ejecutar_proceso(procesos)  # Llama a la función para ejecutar el siguiente proceso.

        ventana.after(1000, actualizar_tiempo)  # Llama a la función después de 1 segundo.
    else:
        label_procesos_restantes.config(text=f"Procesos Restantes: 0") # Se vacia el texto de procesos restantes
        label_lotes_restantes.config(text=f"Lotes Restantes: 0")  # Actualiza la etiqueta de lotes restantes.
        cuadro_procesos.config(text="")  # Borra el cuadro de procesos pendientes.
        cuadro_enProceso.config(text="")  # Borra el cuadro de proceso actual.

# Función para obtener resultados y guardar en el archivo 'resultados.txt'
def obtener_resultados():
    resultados_texto = cuadro_resultados.cget("text")  # Obtiene el texto del cuadro de resultados.
    if resultados_texto:
        resultados_lista = resultados_texto.split("\n")  # Divide el texto en una lista por cada salto de línea.
        resultados_lista = [resultado.strip() for resultado in resultados_lista if resultado.strip()]  # Elimina espacios en blanco.
        guardar_resultados(resultados_lista)  # Llama a la función para guardar los resultados en el archivo.
        messagebox.showinfo("Guardado", "Resultados guardados en 'resultados.txt'")  # Muestra un mensaje de información.
        ventana.destroy()  # Cierra la ventana principal.
    else:
        messagebox.showwarning("Advertencia", "No hay resultados para guardar.")  # Muestra un mensaje de advertencia si no hay resultados.

# Crear la ventana raíz
ventana = tk.Tk()
ventana.title("Procesamiento Por Lotes")  # Establecer el título de la ventana
ventana.geometry("800x800")  # Establecer el tamaño inicial de la ventana

# Pantalla en el centro
ventana.resizable(False, False)  # Desactivar la capacidad de redimensionar la ventana
screen_width = ventana.winfo_screenwidth() 
screen_height = ventana.winfo_screenheight() # Obtener el alto de la pantalla
x_position = (screen_width - 800) // 2
y_position = (screen_height - 800) // 2
ventana.geometry(f"800x800+{x_position}+{y_position}")  # Colocar la ventana en el centro de la pantalla

# Campos de texto
campo_generar = tk.Entry(ventana, width=10, font=("Arial", 10))  # Crear un campo de entrada para el número de procesos
campo_generar.place(relx=0.33, rely=0.07, anchor="center")  # Posicionar el campo de entrada en la ventana

# Botones
boton_generar = tk.Button(ventana, text="Generar", command=generar_procesos)  # Crear un botón para generar procesos
boton_generar.place(relx=0.39, rely=0.047)  # Posicionar el botón en la ventana

boton_resultados = tk.Button(ventana, text="Obtener Resultados", command=obtener_resultados)  # Botón para obtener resultados
boton_resultados.place(relx=0.8, rely=0.85)  # Posicionar el botón en la ventana

# Etiquetas de información
reloj_global = tk.Label(ventana, text="Reloj Global:", font=("Arial", 15))  # Etiqueta para mostrar el reloj global
reloj_global.place(relx=0.78)  # Posicionar la etiqueta en la ventana

procesos = tk.Label(ventana, text="Procesos", font=("Arial", 16))  # Etiqueta para la sección de procesos
procesos.place(relx=0.1, rely=0.09)  # Posicionar la etiqueta en la ventana

enproceso = tk.Label(ventana, text="En Proceso", font=("Arial", 16))  # Etiqueta para la sección de procesos en ejecución
enproceso.place(relx=0.43, rely=0.2)  # Posicionar la etiqueta en la ventana

resultados = tk.Label(ventana, text="Resultados", font=("Arial", 16))  # Etiqueta para la sección de resultados
resultados.place(relx=0.78, rely=0.09)  # Posicionar la etiqueta en la ventana

numeroprocesos = tk.Label(ventana, text="Número de procesos: ", font=("Arial", 16))  # Etiqueta para el número de procesos
numeroprocesos.place(relx=0.01, rely=0.045)  # Posicionar la etiqueta en la ventana

label_procesos_restantes = tk.Label(ventana, text="Procesos Restantes: 0", font=("Arial", 12))  # Etiqueta para mostrar procesos restantes
label_procesos_restantes.place(relx=0.01, rely=0.80)  # Posicionar la etiqueta en la ventana

label_lotes_restantes = tk.Label(ventana, text="Lotes Restantes: 0", font=("Arial", 12))  # Etiqueta para mostrar lotes restantes
label_lotes_restantes.place(relx=0.01, rely=0.85)  # Posicionar la etiqueta en la ventana

# Cuadros de texto
cuadro_procesos = tk.Label(ventana, text=" ", bg="white", width=30, height=35, bd=2, relief="solid")  # Cuadro de texto para mostrar procesos
cuadro_procesos.place(relx=0.03, rely=0.13)  # Posicionar el cuadro en la ventana

cuadro_enProceso = tk.Label(ventana, text="", bg="white", width=40, height=15, bd=2, relief="solid")  # Cuadro de texto para mostrar el proceso en ejecución
cuadro_enProceso.place(relx=0.32, rely=0.25)  # Posicionar el cuadro en la ventana

cuadro_resultados = tk.Label(ventana, text=" ", bg="white", width=30, height=35, bd=2, relief="solid")  # Cuadro de texto para mostrar resultados
cuadro_resultados.place(relx=0.7, rely=0.13)  # Posicionar el cuadro en la ventana

ventana.mainloop()  # Iniciar el bucle principal de la ventana
