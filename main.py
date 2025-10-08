#Needed libraries import
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Object, organizes code
class RegistroPesoApp:
    def __init__(self, ventana_principal):
    
        self.ventana = ventana_principal
        self.ventana.title("Registro de Peso Corporal")
        self.ventana.geometry("500x400")
    
        self.archivo_csv = "datos_peso.csv"
    
        self.inicializar_csv()
    
        self.crear_interfaz()

#Csv initialization
    def inicializar_csv(self):
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8')as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['Fecha', 'Peso_kg', 'Altura_cm', 'Cintura_cm', 'IMC', 'Notas'])

#Interface
    def crear_interfaz(self):
    #Data entry frame
        frame_entrada = tk.LabelFrame(self.ventana, text="Registrar Medición", padx=20, pady=20)
        frame_entrada.pack(padx=10, pady=10, fill="both", expand=True)
    
    #Date field
        tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", pady=5)
        self.entrada_fecha = tk.Entry(frame_entrada, width=30)
        self.entrada_fecha.grid(row=0, column=1, pady=5)
        #Today's date
        self.entrada_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        #Weight field
        tk.Label(frame_entrada, text="Peso (kg):").grid(row=1, column=0, sticky="w", pady=5)
        self.entrada_peso = tk.Entry(frame_entrada, width=30)
        self.entrada_peso.grid(row=1, column=1, pady=5)
        
        #Height field
        tk.Label(frame_entrada, text="Altura (cm):").grid(row=2, column=0, sticky="w", pady=5)
        self.entrada_altura = tk.Entry(frame_entrada, width=30)
        self.entrada_altura.grid(row=2, column=1, pady=5)
        
        #Waistline field
        tk.Label(frame_entrada, text="Cintura (cm) [Opcional]:").grid(row=3, column=0, sticky="w", pady=5)
        self.entrada_cintura = tk.Entry(frame_entrada, width=30)
        self.entrada_cintura.grid(row=3, column=1, pady=5)
        
        #Notes field
        tk.Label(frame_entrada, text="Notas:").grid(row=4, column=0, sticky="w", pady=5)
        self.entrada_notas = tk.Entry(frame_entrada, width=30)
        self.entrada_notas.grid(row=4, column=1, pady=5)
        
        #Buttons
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)
        
        #Save button
        btn_guardar = tk.Button(
            frame_botones,
            text="💾 Guardar Registro",
            command=self.guardar_datos,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        btn_guardar.pack(side="left", padx=5)
        
        #Graphics button
        btn_graficas = tk.Button(
            frame_botones,
            text="📊 Ver Gráficas",
                command=self.mostrar_graficas,
                bg="#2196F3",
                fg="white",
                font=("Arial", 10, "bold"),
                padx=10,
                pady=5
        )
        btn_graficas.pack(side="left", padx=5)

#Functions

#IMC Function
    def calcular_imc(self, peso_kg, altura_cm):
        try:
            altura_metros = altura_cm / 100
            imc = peso_kg / (altura_metros ** 2)
            return round(imc, 2)
        except:
            return 0.0

    #Save data function
    def guardar_datos(self):
        
        fecha = self.entrada_fecha.get().strip()
        peso = self.entrada_peso.get().strip()
        altura = self.entrada_altura.get().strip()
        cintura = self.entrada_cintura.get().strip()
        notas = self.entrada_notas.get().strip()
        
        if not fecha or not peso or not altura:
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, completa Fecha, Peso y Altura"
            )
            return
        
        try:
            peso_float = float(peso)
            altura_float = float(altura)
            cintura_float = float(cintura) if cintura else 0.0
        
        except ValueError:
            messagebox.showerror(
                "Error de Formato",
                "Peso, Altura y Cintura deben ser números"
            )
            return
        
        imc = self.calcular_imc(peso_float, altura_float)
        
        with open(self.archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([
                fecha,
                peso_float,
                altura_float,
                cintura_float if cintura else '',
                imc,
                notas
            ])
        
        messagebox.showinfo(
            "Éxito",
            f"Registro guardado correctamente\nIMC calculado: {imc}"
            )
        
        
        self.entrada_peso.delete(0, tk.END)
        self.entrada_cintura.delete(0, tk.END)
        self.entrada_notas.delete(0, tk.END)

    #Read data function
    def leer_datos_csv(self):
        fechas = []
        pesos = []
        imc_valores = []
        
        if not os.path.exists(self.archivo_csv):
            return fechas, pesos, imc_valores
        
        with open(self.archivo_csv, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                try:
                    fechas.append(fila['Fecha'])
                    pesos.append(float(fila['Peso_kg']))
                    imc_valores.append(float(fila['IMC']))
                
                except:
                    continue
                
        return fechas, pesos, imc_valores

    #Graphics function
    def mostrar_graficas(self):
        fechas, pesos, imc_valores = self.leer_datos_csv()
        
        if len(fechas) == 0:
            messagebox.showinfo(
                "Sin datos",
                "No hay registros para graficar. Agrega algunos datos primeros."
            )
            return
        
        ventana_graficas = tk.Toplevel(self.ventana)
        ventana_graficas.title("Gráficas de Progreso")
        ventana_graficas.geometry("1000x600")
        
        figura = Figure(figsize=(10, 6))
        
        ax1 = figura.add_subplot(2, 1, 1)
        ax1.plot(fechas, imc_valores, marker='o', linestyle='-', color='#2169F3', linewidth=2)
        ax1.set_title('Evolución del Peso', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Fecha')
        ax1.set_ylabel('Peso (kg)')
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        ax2 = figura.add_subplot(2, 1, 2)
        ax2.plot(fechas, imc_valores, marker='o', linestyle='-', color='#4CAF50', linewidth=2)
        ax2.set_title('Evolución del IMC', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Fecha')
        ax2.set_ylabel('IMC')
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis='x', rotation=45)
        
        ax2.axhspan(0, 18.5, alpha=0.2, color='lightblue', label='Bajo peso')
        ax2.axhspan(18.5, 25, alpha=0.2, color='lightgreen', label='Normal')
        ax2.axhspan(25, 30, alpha=0.2, color='yellow', label='Sobrepeso')
        ax2.axhspan(30, 40, alpha=0.2, color='orange', label='Obesidad')
        ax2.legend(loc='upper right')
        
        figura.tight_layout()
        
        canvas = FigureCanvasTkAgg(figura, master=ventana_graficas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

def main():
    ventana_principal = tk.Tk()
    app = RegistroPesoApp(ventana_principal)
    ventana_principal.mainloop()
    
if __name__ == "__main__":
    main()
    
    