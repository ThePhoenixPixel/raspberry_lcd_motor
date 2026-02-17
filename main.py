import RPi.GPIO as GPIO
from RPLCD import CharLCD
from gpiozero import RotaryEncoder
import time

# --------------------
# GPIO Modus
# --------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# --------------------
# LCD
# --------------------
lcd = CharLCD(
    cols=16,
    rows=2,
    pin_rs=37,
    pin_e=35,
    pins_data=[40, 38, 36, 32, 33, 31, 29, 23],
    numbering_mode=GPIO.BOARD
)

# --------------------
# Rotary Encoder (BCM!)
# --------------------
zahl = 0
encoder = RotaryEncoder(a=17, b=27, max_steps=0)

# --------------------
# Buttons + Servo
# --------------------
save_button = 16      # BOARD 16 -> Menü / Speichern
toggle_button = 22    # BOARD 22 -> Toggle Position
servo_pin = 12        # BOARD 12 (PWM)

GPIO.setup(save_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(toggle_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

# --------------------
# Speicher
# --------------------
pos1 = 0
pos2 = 90
menu_active = False
menu_selection = 0   # 0 = Pos1, 1 = Pos2
current_toggle = 0   # aktuelle Zielposition

# --------------------
# Funktionen
# --------------------
def set_servo_angle(angle):
    angle = max(0, min(180, angle))
    duty = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def update_lcd():
    lcd.clear()
    if not menu_active:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Servo Winkel:")
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f"{zahl} Grad")
    else:
        lcd.cursor_pos = (0, 0)
        if menu_selection == 0:
            lcd.write_string(">Pos1")
        else:
            lcd.write_string(" Pos1")

        lcd.cursor_pos = (1, 0)
        if menu_selection == 1:
            lcd.write_string(">Pos2")
        else:
            lcd.write_string(" Pos2")

# --------------------
# Encoder Steuerung
# --------------------
def rechts():
    global zahl, menu_selection
    if not menu_active:
        if zahl < 180:
            zahl += 1
    else:
        menu_selection = (menu_selection + 1) % 2
    update_lcd()

def links():
    global zahl, menu_selection
    if not menu_active:
        if zahl > 0:
            zahl -= 1
    else:
        menu_selection = (menu_selection - 1) % 2
    update_lcd()

encoder.when_rotated_clockwise = rechts
encoder.when_rotated_counter_clockwise = links

# --------------------
# Start
# --------------------
update_lcd()

# --------------------
# Hauptloop
# --------------------
try:
    while True:

        # Menü öffnen / speichern
        if GPIO.input(save_button) == GPIO.LOW:
            time.sleep(0.3)

            if not menu_active:
                menu_active = True
            else:
                if menu_selection == 0:
                    pos1 = zahl
                else:
                    pos2 = zahl
                menu_active = False

            update_lcd()

        # Toggle Button
        if GPIO.input(toggle_button) == GPIO.LOW:
            time.sleep(0.3)

            if current_toggle == 0:
                set_servo_angle(pos1)
                current_toggle = 1
            else:
                set_servo_angle(pos2)
                current_toggle = 0

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    servo.stop()
    lcd.clear()
    GPIO.cleanup()
