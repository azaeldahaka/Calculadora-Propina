import tkinter as tk
from tkinter import messagebox
from main import calculadora_propina

MAX_DIGITS = 15  # Definir el máximo número de dígitos permitido en los campos de entrada

def on_calcular(event=None):
    try:
        total_factura = entry_factura.get().strip()  # Obtener el valor del campo y eliminar espacios en blanco
        porcentaje_propina = entry_porcentaje.get().strip()

        if len(total_factura) > MAX_DIGITS or len(porcentaje_propina) > MAX_DIGITS:
            messagebox.showerror("Error", f"Los números no deben tener más de {MAX_DIGITS} dígitos.")
            return

        if not total_factura or not porcentaje_propina:  # Verificar si algún campo está vacío
            messagebox.showerror("Error", "Ningún campo debe estar vacío.")
            return

        total_factura = float(total_factura)
        porcentaje_propina = float(porcentaje_propina)

        if total_factura <= 0 and porcentaje_propina <= 0:
            messagebox.showerror("Error", "Ambos valores deben ser mayor a cero.")
            return
        
        if total_factura <= 0:
            messagebox.showerror("Error", "El monto de la factura debe ser mayor que cero.")
            return

        if porcentaje_propina <= 0:
            messagebox.showerror("Error", "El porcentaje de propina debe ser mayor que cero.")
            return

        propina = calculadora_propina(total_factura, porcentaje_propina)
        total_con_propina = total_factura + propina
        resultado.set(f"Monto de la propina: ${propina:.2f}\nMonto total con propina: ${total_con_propina:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Propinas")

# Establecer dimensiones fijas y deshabilitar cambio de tamaño
root.geometry("400x200")  # Ancho x Alto
root.resizable(False, False)  # El primer argumento deshabilita el cambio de ancho, el segundo deshabilita el cambio de alto

# Crear los widgets de la interfaz
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_factura = tk.Label(frame, text="Monto total de la factura ($):")
label_factura.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_factura = tk.Entry(frame)
entry_factura.grid(row=0, column=1, padx=10, pady=5)
entry_factura.bind('<Return>', on_calcular)  # Asociar la tecla "Enter" al evento on_calcular

label_porcentaje = tk.Label(frame, text="Porcentaje de propina:")
label_porcentaje.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_porcentaje = tk.Entry(frame)
entry_porcentaje.grid(row=1, column=1, padx=10, pady=5)
entry_porcentaje.bind('<Return>', on_calcular)  # Asociar la tecla "Enter" al evento on_calcular

button_calcular = tk.Button(frame, text="Calcular Propina", command=on_calcular)
button_calcular.grid(row=2, columnspan=2, padx=10, pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado)
label_resultado.grid(row=3, columnspan=2, padx=10, pady=5)

# Iniciar el bucle de eventos
root.mainloop()
