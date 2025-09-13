
BCM = 'BCM'    
OUT = 'OUT'     
IN = 'IN'        
HIGH = 1        
LOW = 0          


_pin_modes = {}
_pin_values = {}

def setmode(mode):
    print(f"[MockGPIO] Modo configurado: {mode}")

def setup(pin, mode):
    _pin_modes[pin] = mode
    print(f"[MockGPIO] Pin {pin} configurado como {mode}")

def input(pin):
    return _pin_values.get(pin, LOW)

def output(pin, value):
    _pin_values[pin] = value
    estado = 'HIGH' if value else 'LOW'
    print(f"[MockGPIO] Pin {pin} salida: {estado}")

def cleanup():
    _pin_modes.clear()
    _pin_values.clear()
    print("[MockGPIO] Limpieza realizada")

class PWM:
    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq
        self.duty_cycle = 0
        print(f"[MockGPIO] PWM inicializado en pin {pin} con frecuencia {freq}Hz")

    def start(self, duty_cycle):
        self.duty_cycle = duty_cycle
        print(f"[MockGPIO] PWM iniciado con ciclo de trabajo {duty_cycle}%")

    def ChangeDutyCycle(self, duty_cycle):
        self.duty_cycle = duty_cycle
        print(f"[MockGPIO] PWM ciclo de trabajo cambiado a {duty_cycle}%")

    def stop(self):
        print("[MockGPIO] PWM detenido")
