import tkinter as tk
from tkinter import ttk

class FakePWM:
    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq
        self.duty = 0
        print(f"[SIM] PWM creado en pin {pin} con {freq} Hz")

    def start(self, duty):
        self.duty = duty
        print(f"[SIM] PWM iniciado con duty {duty}%")

    def ChangeDutyCycle(self, duty):
        self.duty = duty
        print(f"[SIM] Duty cycle cambiado a {duty}%")

    def stop(self):
        print("[SIM] PWM detenido")

PIN_LED = 18
FREQ = 1000
pwm = FakePWM(PIN_LED, FREQ)
pwm.start(0)

def set_brightness(brightness):
    pwm.ChangeDutyCycle(brightness)

def gui_mode():
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

    btn_exit = ttk.Button(root, text="Apagar y salir", command=lambda: (pwm.stop(), root.destroy()))
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    gui_mode()