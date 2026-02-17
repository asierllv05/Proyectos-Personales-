import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk
from guizero import Drawing

def crear_grafico(tiempo=None, aceleracion=None):
    if tiempo is None or aceleracion is None:
        # Crear una figura y ejes vacíos
        fig, ax = plt.subplots()
        ax.set_facecolor((0.2, 0.2, 0.2))  # Color de fondo
        ax.tick_params(axis='both', which='both', labelbottom=False, labelleft=False)
        canvas = FigureCanvasTkAgg(fig, master=drawing)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(tiempo, aceleracion, label='Aceleración', color='b')
        plt.title('Aceleración - Tiempo')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Aceleración (m/s^2)')
        plt.legend()
        plt.grid(True)
        canvas = FigureCanvasTkAgg(plt.gcf(), master=drawing)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Si se proporcionan datos
# Leer el archivo Excel
df = pd.read_excel('datos3.xlsx')

# Extraer las columnas relevantes
tiempo = df['Time (s)']
aceleracion = df['Absolute acceleration (m/s^2)']

# Crear una ventana Tkinter
root = Tk()
root.title("Gráfico de Aceleración")

# Crear un widget Drawing para el gráfico
drawing = Drawing(root, width=800, height=600)
drawing.pack()

# Crear el gráfico
crear_grafico(tiempo, aceleracion)

# Mostrar la ventana
root.mainloop()

