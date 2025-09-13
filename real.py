import MockGPIO as GPIO
import time
import argparse
import tkinter as tk

PIN_LED = 18
PIN_CAM = 23
FREQ = 1000

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_CAM, GPIO.IN)

pwm = GPIO.PWM(PIN_LED, FREQ)
pwm.start(0)

# Se ajusta el brillo del LED
def set_brightness(brightness):
    pwm.ChangeDutyCycle(brightness)

# Loop para iniciar el control del LED basado en la señal de la cámara
def loop(brightness):
    try:
        while True:
            if GPIO.input(PIN_CAM) == GPIO.HIGH:
                set_brightness(brightness)
                time.sleep(0.1)  # estabilización
                set_brightness(0)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()

# Interfaz de línea de comandos
def cli_mode():
    parser = argparse.ArgumentParser(description="Control de LED con PWM y señal de cámara")
    parser.add_argument("--brillo", type=int, default=50, help="Brillo (0-100)")
    args = parser.parse_args()
    print(f"Iniciando en CLI con brillo {args.brillo}%...")
    loop(args.brillo)

# Entrada gráfica usando Tkinter
def gui_mode():
    from tkinter import ttk
    def update_brightness(val):
        brillo = int(float(val))
        set_brightness(brillo)
        lbl_valor.config(text=f"{brillo}%")

    root = tk.Tk()
    root.title("💡 Control LED PWM")
    root.geometry("400x250")
    root.configure(bg="#1e1e2f")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 12))
    style.configure("TScale", background="#1e1e2f")
    style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)

    lbl_title = ttk.Label(root, text="Control de Brillo LED", font=("Segoe UI", 16, "bold"), foreground="#00ff99")
    lbl_title.pack(pady=15)

    frame_valor = ttk.Frame(root)
    frame_valor.pack()
    ttk.Label(frame_valor, text="Brillo: ").pack(side="left")
    lbl_valor = ttk.Label(frame_valor, text="0%", font=("Segoe UI", 12, "bold"), foreground="#00ffcc")
    lbl_valor.pack(side="left")

    scale = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_brightness, length=300)
    scale.pack(pady=20)

    btn_exit = ttk.Button(root, text="Apagar y salir", command=lambda: (pwm.stop(), GPIO.cleanup(), root.destroy()))
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    # Cambiar de modo CLI a GUI según se desee
    # Uno de los dos modos debe estar activo y sirven para propósitos diferentes
    # El primero es para uso en terminal, el segundo para uso con interfaz gráfica

    #cli_mode()
     gui_mode()
