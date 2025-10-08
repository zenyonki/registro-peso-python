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
    def __init__(sel, ventana_principal):
    
        self.ventana = ventana_principal
        self.ventana.title("Registro de Peso Corporal")
        self.ventana.geometry("500x400")
    
        self.archivo_csv = "datos_peso.csv"
    
        self.inicializar_csv()
    
        self.crear_interfaz()

#Csv initialization
def inicializar_csv(sel):
    if not os.pathexist(self.archivo_csv):
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
    
    
    
    
    
    
    
    
    
    
    