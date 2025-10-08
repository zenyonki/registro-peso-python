# 📊 Registro de Peso Corporal

Aplicación de escritorio desarrollada en Python con **tkinter** para registrar y visualizar el progreso de peso corporal y métricas de salud.

## 🎯 Objetivo del Proyecto

Este proyecto fue creado como ejercicio de aprendizaje para dominar los fundamentos de **Python**, **tkinter** y **visualización de datos**. El enfoque está en crear una aplicación funcional que integre múltiples conceptos de programación.

---

## 🧠 Conceptos Aprendidos

### **Programación Orientada a Objetos (POO)**
- Creación de clases y métodos
- Uso de `__init__` como constructor
- `self` para referenciar instancias de clase
- Encapsulación de funcionalidad

### **Interfaz Gráfica con tkinter**
- **Widgets fundamentales:**
  - `Tk()`: Ventana principal
  - `LabelFrame`: Contenedores con título
  - `Label`: Etiquetas de texto
  - `Entry`: Campos de entrada de texto
  - `Button`: Botones interactivos
  - `Toplevel`: Ventanas secundarias
  
- **Layout managers:**
  - `.grid()`: Posicionamiento en cuadrícula
  - `.pack()`: Empaquetado secuencial
  - `sticky`, `padx`, `pady`: Control de espaciado

- **Eventos y comandos:**
  - `command=funcion`: Asignar funciones a botones
  - Obtención de datos con `.get()`
  - Limpieza de campos con `.delete()`
  - Inserción de valores con `.insert()`

### **Manejo de Archivos CSV**
- **Escritura:**
  - `csv.writer()` para escribir datos
  - `.writerow()` para agregar filas
  - Modo `'w'` (write) y `'a'` (append)
  
- **Lectura:**
  - `csv.DictReader()` para leer como diccionarios
  - Acceso a columnas por nombre
  - Iteración sobre filas

### **Validación de Datos**
- Bloques `try/except` para capturar errores
- Validación de campos obligatorios
- Conversión segura de tipos (`float()`, `int()`)
- Uso de `.strip()` para limpiar espacios

### **Visualización con Matplotlib**
- Creación de figuras con `Figure()`
- Múltiples gráficas con `add_subplot()`
- Personalización de gráficas:
  - Líneas con `plot()`
  - Marcadores (`marker='o'`, `marker='s'`)
  - Colores y estilos de línea
  - Rejillas con `.grid()`
  - Títulos y etiquetas de ejes
  
- **Técnicas avanzadas:**
  - `axhspan()` para zonas de color
  - Leyendas con `.legend()`
  - Rotación de etiquetas con `tick_params()`
  - `tight_layout()` para ajuste automático
  - Integración en tkinter con `FigureCanvasTkAgg`

### **Manejo de Fechas**
- Módulo `datetime`
- Formato de fechas con `.strftime()`
- Fecha actual con `datetime.now()`

### **Buenas Prácticas**
- Docstrings para documentar funciones
- Nombres descriptivos de variables y funciones
- Separación de lógica en métodos
- Manejo de excepciones
- Validación de existencia de archivos con `os.path.exists()`

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.12+ | Lenguaje de programación |
| **tkinter** | Built-in | Interfaz gráfica de usuario |
| **matplotlib** | 3.x | Visualización de datos |
| **csv** | Built-in | Manejo de archivos CSV |
| **datetime** | Built-in | Manejo de fechas |

---

## ✨ Características

- ✅ **Registro de datos:** Fecha, peso, altura, cintura y notas
- ✅ **Cálculo automático de IMC** (Índice de Masa Corporal)
- ✅ **Almacenamiento persistente** en formato CSV
- ✅ **Validación de datos** con mensajes de error informativos
- ✅ **Gráficas interactivas:**
  - Evolución del peso en el tiempo
  - Evolución del IMC con zonas de interpretación (bajo peso, normal, sobrepeso, obesidad)
- ✅ **Interfaz intuitiva** con colores y emojis
- ✅ **Limpieza automática** de campos después de guardar

---

## 📋 Requisitos

### **Sistema Operativo:**
- Linux (probado en Fedora)
- Windows
- macOS

### **Dependencias:**

```bash
# Python 3.12 o superior
python3 --version

# tkinter (en Fedora)
sudo dnf install python3-tkinter

# matplotlib
pip install matplotlib
```

---

## 🚀 Instalación y Uso

### **1. Clonar el repositorio:**
```bash
git clone https://github.com/TU-USUARIO/registro-peso-python.git
cd registro-peso-python
```

### **2. Instalar dependencias:**
```bash
pip install matplotlib
```

### **3. Ejecutar la aplicación:**
```bash
python3 main.py
```

---

## 📖 Cómo Usar la Aplicación

1. **Registrar medición:**
   - Ingresa la fecha (se rellena automáticamente con hoy)
   - Ingresa tu peso en kilogramos
   - Ingresa tu altura en centímetros
   - Opcionalmente: medida de cintura y notas
   - Click en **💾 Guardar Registro**

2. **Ver progreso:**
   - Click en **📊 Ver Gráficas**
   - Se abrirá una ventana con dos gráficas:
     - Evolución de tu peso
     - Evolución de tu IMC con zonas interpretativas

3. **Datos guardados:**
   - Los datos se almacenan en `datos_peso.csv`
   - Puedes abrirlo con Excel o cualquier editor de texto

---

## 📂 Estructura del Proyecto

```
registro-peso-python/
├── main.py              # Código principal de la aplicación
├── datos_peso.csv       # Base de datos (se crea automáticamente)
├── README.md            # Este archivo
├── .gitignore           # Archivos a ignorar en Git
└── screenshots/         # Capturas de pantalla (opcional)
```

---

## 🎨 Estructura del Código

### **Clase Principal: `RegistroPesoApp`**

```python
class RegistroPesoApp:
    def __init__(self, ventana_principal)
        # Inicializa la aplicación
    
    def inicializar_csv(self)
        # Crea el archivo CSV si no existe
    
    def crear_interfaz(self)
        # Construye la interfaz gráfica
    
    def calcular_imc(self, peso_kg, altura_cm)
        # Calcula el IMC
    
    def guardar_datos(self)
        # Valida y guarda datos en CSV
    
    def leer_datos_csv(self)
        # Lee todos los registros del CSV
    
    def mostrar_graficas(self)
        # Genera y muestra las gráficas
```

---

## 📊 Formato del CSV

El archivo `datos_peso.csv` tiene la siguiente estructura:

```csv
Fecha,Peso_kg,Altura_cm,Cintura_cm,IMC,Notas
2024-01-15,70.5,175,85,23.02,Me siento bien
2024-01-22,69.8,175,84,22.81,Bajé un poco
```

---

## 🧪 Validaciones Implementadas

- ✅ Campos obligatorios no vacíos (fecha, peso, altura)
- ✅ Peso y altura deben ser números válidos
- ✅ Mensajes de error descriptivos
- ✅ Manejo de excepciones para evitar crashes
- ✅ Validación de existencia de archivos antes de leer

---

## 🎓 Aprendizajes Clave

### **1. Integración de múltiples librerías**
Combinar tkinter (GUI), matplotlib (gráficas) y CSV (persistencia) en una sola aplicación cohesiva.

### **2. Separación de responsabilidades**
Cada método tiene una única función clara: validar, guardar, leer, graficar.

### **3. Experiencia de usuario**
- Campos prellenados (fecha actual)
- Mensajes claros de éxito/error
- Limpieza automática de campos
- Validación preventiva

### **4. Visualización efectiva**
- Uso de colores para interpretación rápida
- Zonas de IMC para contexto visual
- Múltiples gráficas relacionadas

---

## 🔮 Mejoras Futuras

Ideas para expandir el proyecto:

- [ ] Agregar gráfica de evolución de cintura
- [ ] Panel de estadísticas (promedio, máximo, mínimo)
- [ ] Exportar datos a Excel
- [ ] Establecer y visualizar metas de peso
- [ ] Tabla con historial de registros (Treeview)
- [ ] Editar o eliminar registros existentes
- [ ] Múltiples usuarios
- [ ] Backup automático de datos
- [ ] Selector de fecha visual (calendario)
- [ ] Gráfica de tendencia con línea de regresión

---

## 🤝 Contribuciones

Este es un proyecto educativo. Si encuentras bugs o tienes sugerencias de mejora, siéntete libre de:

1. Hacer fork del proyecto
2. Crear una rama para tu feature (`git checkout -b feature/MejoraNueva`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/MejoraNueva`)
5. Abrir un Pull Request

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@zenyonki](https://github.com/zenyonki)
- Email: miguelct89@gmail.com

---

## 🙏 Agradecimientos

Proyecto desarrollado como parte del aprendizaje de Python, tkinter y visualización de datos.

---


**⭐ Si este proyecto te fue útil para aprender, considera darle una estrella en GitHub!**
