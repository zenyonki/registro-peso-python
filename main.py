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

