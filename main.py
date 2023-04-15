import tkinter as tk
import os

# Variables globales para el tiempo programado y el ID del proceso de apagado
tiempo_horas = 0
tiempo_minutos = 0
proceso_apagado = None

# Funciones para manejar eventos de la interfaz gráfica
def apagar():
    global tiempo_horas, tiempo_minutos, proceso_apagado
    tiempo_horas = int(entry_horas.get())
    tiempo_minutos = int(entry_minutos.get())
    tiempo_total = tiempo_horas * 60 + tiempo_minutos
    if tiempo_total > 0:
        proceso_apagado = os.system(f"shutdown /s /t {tiempo_total * 60}")
        resultado.set(f"El ordenador se apagará en {tiempo_horas} horas y {tiempo_minutos} minutos.")
    else:
        resultado.set("Por favor, ingrese un tiempo válido.")

def cancelar_apagado():
    global proceso_apagado
    if proceso_apagado is not None:
        os.system("shutdown -a")
        resultado.set("Se ha cancelado el apagado programado.")
        proceso_apagado = None
    else:
        resultado.set("No hay un apagado programado.")

def reiniciar():
    os.system("shutdown /r /t 1")
    resultado.set("El ordenador se reiniciará en 1 segundo.")

def standby():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    resultado.set("El ordenador se pondrá en standby (suspensión) en 1 segundo.")

# Configuración de la ventana de la aplicación
ventana = tk.Tk()
ventana.title("PC Timer")
ventana.geometry("300x250")
ventana.resizable(True, True)

# Etiquetas y entradas de texto para el tiempo en horas y minutos
label_horas = tk.Label(ventana, text="Horas:")
label_horas.grid(row=0, column=0, padx=10, pady=10)
entry_horas = tk.Entry(ventana)
entry_horas.grid(row=0, column=1, padx=10, pady=10)

label_minutos = tk.Label(ventana, text="Minutos:")
label_minutos.grid(row=1, column=0, padx=10, pady=10)
entry_minutos = tk.Entry(ventana)
entry_minutos.grid(row=1, column=1, padx=10, pady=10)

# Botones para apagar, reiniciar, standby y cancelar apagado
boton_apagar = tk.Button(ventana, text="Apagar", command=apagar)
boton_apagar.grid(row=2, column=0, padx=10, pady=10)

# Crear un boton centrado con texto SOS que manda un comando al cmd
boton_sos = tk.Button(ventana, text="Cancelar Apagado", command=lambda: os.system("shutdown -a"))
boton_sos.grid(row=2, column=1, columnspan=2, padx=10, pady=10)


#crear separador vertical
separador = tk.Frame(ventana, height=2, bd=1, relief=tk.SUNKEN)
separador.grid(row=4, columnspan=2, sticky=tk.EW, padx=5, pady=5)

boton_reiniciar = tk.Button(ventana, text="Reiniciar (Imediato)", command=reiniciar)
boton_reiniciar.grid(row=6, column=0, padx=10, pady=10)

boton_standby = tk.Button(ventana, text="Suspender (Imediato)", command=standby)
boton_standby.grid(row=6, column=1, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()