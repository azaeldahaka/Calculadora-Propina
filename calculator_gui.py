import tkinter as tk
from tkinter import messagebox
from main import calculadora_propina

def on_calcular():
    try:
        total_factura = float(entry_factura.get())
        porcentaje_propina = float(entry_porcentaje.get())

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

# Crear los widgets de la interfaz
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_factura = tk.Label(frame, text="Monto total de la factura ($):")
label_factura.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_factura = tk.Entry(frame)
entry_factura.grid(row=0, column=1, padx=10, pady=5)

label_porcentaje = tk.Label(frame, text="Porcentaje de propina:")
label_porcentaje.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_porcentaje = tk.Entry(frame)
entry_porcentaje.grid(row=1, column=1, padx=10, pady=5)

button_calcular = tk.Button(frame, text="Calcular Propina", command=on_calcular)
button_calcular.grid(row=2, columnspan=2, padx=10, pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado)
label_resultado.grid(row=3, columnspan=2, padx=10, pady=5)

# Iniciar el bucle de eventos
root.mainloop()
