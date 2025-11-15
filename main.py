import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO
import time

# Configuración GPIO
led_pwm = 32
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pwm, GPIO.OUT)
led = GPIO.PWM(led_pwm, 100)
led.start(100)
variable = 100

# Colores modernos
COLOR_PRIMARY = "#2C3E50"      # Azul oscuro
COLOR_SECONDARY = "#3498DB"    # Azul claro
COLOR_SUCCESS = "#27AE60"      # Verde
COLOR_DANGER = "#E74C3C"       # Rojo
COLOR_BG = "#ECF0F1"           # Gris claro
COLOR_CARD = "#FFFFFF"         # Blanco
COLOR_TEXT = "#2C3E50"         # Texto oscuro
COLOR_ACCENT = "#9B59B6"       # Morado

def actualizar_valor(val):
    valor = barra.get()
    led.ChangeDutyCycle(valor)
    label_valor.config(text=f"{valor}%")
    actualizar_indicador(valor)

def actualizar_indicador(valor):
    """Actualiza el indicador visual de brillo"""
    if valor == 0:
        indicador.config(bg="#34495E", text="● Apagado")
    elif valor < 33:
        indicador.config(bg="#E67E22", text="● Bajo")
    elif valor < 66:
        indicador.config(bg="#F39C12", text="● Medio")
    else:
        indicador.config(bg="#27AE60", text="● Alto")

def bosch_prende():
    valor = barra.get()
    led.ChangeDutyCycle(valor)
    label_valor.config(text=f"{valor}%")
    actualizar_indicador(valor)
    status_label.config(text="Estado: Encendido", fg=COLOR_SUCCESS)

def bosch_apaga():
    led.ChangeDutyCycle(0)
    label_valor.config(text="0%")
    actualizar_indicador(0)
    status_label.config(text="Estado: Apagado", fg=COLOR_DANGER)

def habilita_tec():
    boton_prende.config(state='disabled', bg="#BDC3C7", fg="#7F8C8D")
    boton_apaga.config(state='disabled', bg="#BDC3C7", fg="#7F8C8D")
    barra.config(state='normal')
    status_label.config(text="Modo: TEC (Control Manual)", fg=COLOR_SECONDARY)
    modo_label.config(text="Modo TEC", bg=COLOR_ACCENT)

def habilita_bosch():
    boton_prende.config(state='normal', bg=COLOR_SUCCESS, fg="white")
    boton_apaga.config(state='normal', bg=COLOR_DANGER, fg="white")
    barra.config(state='disabled')
    status_label.config(text="Modo: BOSCH (Control por Botones)", fg=COLOR_SECONDARY)
    modo_label.config(text="Modo BOSCH", bg=COLOR_SECONDARY)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Control LED - Reto BOSCH y TEC")
ventana.geometry("450x550")
ventana.configure(bg=COLOR_BG)
ventana.resizable(False, False)

# Estilo para ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('TScale', background=COLOR_CARD)

# Frame principal con padding
main_frame = tk.Frame(ventana, bg=COLOR_BG, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# Título principal
titulo = tk.Label(
    main_frame, 
    text="Control de LED PWM", 
    font=("Arial", 20, "bold"),
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
titulo.pack(pady=(0, 10))

# Frame para el selector de modo (con fondo de tarjeta)
modo_frame = tk.Frame(main_frame, bg=COLOR_CARD, relief=tk.FLAT, padx=20, pady=15)
modo_frame.pack(fill="x", pady=(0, 15))

modo_label = tk.Label(
    modo_frame,
    text="Modo BOSCH",
    font=("Arial", 12, "bold"),
    bg=COLOR_SECONDARY,
    fg="white",
    padx=15,
    pady=5
)
modo_label.pack(pady=(0, 10))

# Selector de modo con mejor estilo
opcion = tk.StringVar(value="Bosch")
selector_frame = tk.Frame(modo_frame, bg=COLOR_CARD)
selector_frame.pack()

selector1 = tk.Radiobutton(
    selector_frame,
    text="🔧 Modo Bosch",
    variable=opcion,
    value="Bosch",
    command=habilita_bosch,
    font=("Arial", 11),
    bg=COLOR_CARD,
    fg=COLOR_TEXT,
    selectcolor=COLOR_CARD,
    activebackground=COLOR_BG,
    activeforeground=COLOR_TEXT,
    padx=10,
    pady=5
)
selector1.pack(side="left", padx=10)

selector2 = tk.Radiobutton(
    selector_frame,
    text="🎛️ Modo Tec",
    variable=opcion,
    value="Tec",
    command=habilita_tec,
    font=("Arial", 11),
    bg=COLOR_CARD,
    fg=COLOR_TEXT,
    selectcolor=COLOR_CARD,
    activebackground=COLOR_BG,
    activeforeground=COLOR_TEXT,
    padx=10,
    pady=5
)
selector2.pack(side="left", padx=10)

# Frame para el control de brillo
brillo_frame = tk.Frame(main_frame, bg=COLOR_CARD, relief=tk.FLAT, padx=20, pady=20)
brillo_frame.pack(fill="x", pady=(0, 15))

brillo_titulo = tk.Label(
    brillo_frame,
    text="Brillo del LED",
    font=("Arial", 12, "bold"),
    bg=COLOR_CARD,
    fg=COLOR_TEXT
)
brillo_titulo.pack(anchor="w", pady=(0, 10))

# Valor actual del brillo
valor_frame = tk.Frame(brillo_frame, bg=COLOR_CARD)
valor_frame.pack(fill="x", pady=(0, 10))

label_valor = tk.Label(
    valor_frame,
    text="100%",
    font=("Arial", 24, "bold"),
    bg=COLOR_CARD,
    fg=COLOR_SECONDARY
)
label_valor.pack()

# Indicador visual de nivel
indicador = tk.Label(
    valor_frame,
    text="● Alto",
    font=("Arial", 10),
    bg=COLOR_SUCCESS,
    fg="white",
    padx=10,
    pady=3
)
indicador.pack(pady=(5, 0))
actualizar_indicador(100)

# Barra de control (Scale)
barra = tk.Scale(
    brillo_frame,
    from_=0,
    to=100,
    orient='horizontal',
    command=actualizar_valor,
    length=350,
    bg=COLOR_CARD,
    fg=COLOR_TEXT,
    troughcolor=COLOR_BG,
    activebackground=COLOR_SECONDARY,
    highlightthickness=0,
    font=("Arial", 10)
)
barra.set(100)
barra.pack(fill="x", pady=(10, 0))

# Etiquetas de rango
rango_frame = tk.Frame(brillo_frame, bg=COLOR_CARD)
rango_frame.pack(fill="x")
tk.Label(rango_frame, text="0%", bg=COLOR_CARD, fg=COLOR_TEXT, font=("Arial", 8)).pack(side="left")
tk.Label(rango_frame, text="100%", bg=COLOR_CARD, fg=COLOR_TEXT, font=("Arial", 8)).pack(side="right")

# Frame para botones
botones_frame = tk.Frame(main_frame, bg=COLOR_CARD, relief=tk.FLAT, padx=20, pady=20)
botones_frame.pack(fill="x", pady=(0, 15))

botones_titulo = tk.Label(
    botones_frame,
    text="Control Manual (Modo Bosch)",
    font=("Arial", 12, "bold"),
    bg=COLOR_CARD,
    fg=COLOR_TEXT
)
botones_titulo.pack(anchor="w", pady=(0, 15))

# Botones con mejor estilo
botones_container = tk.Frame(botones_frame, bg=COLOR_CARD)
botones_container.pack(fill="x")

boton_prende = tk.Button(
    botones_container,
    text="⚡ Encender",
    command=bosch_prende,
    font=("Arial", 12, "bold"),
    bg=COLOR_SUCCESS,
    fg="white",
    activebackground="#229954",
    activeforeground="white",
    relief=tk.FLAT,
    padx=30,
    pady=12,
    cursor="hand2"
)
boton_prende.pack(side="left", expand=True, fill="x", padx=(0, 10))

boton_apaga = tk.Button(
    botones_container,
    text="⏻ Apagar",
    command=bosch_apaga,
    font=("Arial", 12, "bold"),
    bg=COLOR_DANGER,
    fg="white",
    activebackground="#C0392B",
    activeforeground="white",
    relief=tk.FLAT,
    padx=30,
    pady=12,
    cursor="hand2"
)
boton_apaga.pack(side="left", expand=True, fill="x", padx=(10, 0))

# Barra de estado
status_frame = tk.Frame(main_frame, bg=COLOR_PRIMARY, relief=tk.FLAT, padx=15, pady=10)
status_frame.pack(fill="x")

status_label = tk.Label(
    status_frame,
    text="Modo: BOSCH (Control por Botones)",
    font=("Arial", 10),
    bg=COLOR_PRIMARY,
    fg="white"
)
status_label.pack()

# Inicializar estado
habilita_bosch()

ventana.mainloop()