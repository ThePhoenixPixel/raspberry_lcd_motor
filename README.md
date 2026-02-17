Servo Controller mit Rotary Encoder & LCD (Raspberry Pi)

Dieses Projekt steuert einen Servo-Motor mit einem Rotary Encoder über einen Raspberry Pi.
Ein 16x2 LCD Display zeigt den aktuellen Winkel sowie ein Menü zum Speichern von zwei Positionen an.

📦 Verwendete Hardware

Raspberry Pi

16x2 LCD Display (HD44780 kompatibel)

Rotary Encoder (CLK + DT)

2 Taster

Servo Motor (z.B. SG90)

Externe 5V Stromversorgung für Servo (empfohlen)

📚 Verwendete Python Libraries

RPi.GPIO

gpiozero

RPLCD

Installation:

sudo apt update
sudo apt install python3-gpiozero
pip3 install RPLCD

🔌 Pinbelegung
LCD (BOARD Mode)
LCD Pin	Raspberry Pi Pin
RS	37
E	35
D0–D7	40, 38, 36, 32, 33, 31, 29, 23
Rotary Encoder (BCM Mode!)
Encoder Pin	GPIO
CLK	GPIO17
DT	GPIO27

⚠️ Achtung: Encoder läuft im BCM Modus, Rest im BOARD Modus.

Buttons & Servo (BOARD Mode)
Funktion	Pin
Menü / Speichern	16
Toggle Position	22
Servo PWM	12
⚙️ Funktionsweise
Normalmodus

Drehung am Encoder → verändert Servo-Winkel (0–180°)

LCD zeigt aktuellen Winkel

Toggle-Button fährt zwischen gespeicherten Positionen

Menümodus

Menü-Button drücken → Menü öffnen

Mit Encoder zwischen Pos1 und Pos2 wechseln

Nochmal drücken → aktuelle Winkelposition speichern

🖥️ LCD Anzeige
Normalmodus:
Servo Winkel:
90 Grad

Menümodus:
>Pos1
 Pos2

▶️ Programm starten
python3 dein_script.py

🛑 Beenden

Mit:

CTRL + C


GPIO und PWM werden automatisch sauber beendet.

⚠️ Wichtige Hinweise

Servo sollte nicht direkt vom Raspberry Pi 5V Pin versorgt werden (Stromspitzen!)

Gemeinsame Masse (GND) zwischen Servo-Netzteil und Raspberry Pi erforderlich

Bei Zittern des Servos ggf. Duty-Cycle-Werte anpassen

🧠 Features

Winkelbegrenzung 0–180°

Zwei speicherbare Positionen

Menüführung über Encoder

Entprellung per Software

Automatisches Cleanup bei Programmende

🚀 Erweiterungsmöglichkeiten

Mehr Speicherpositionen

EEPROM Speicherung

OLED Display

Sanfte Servo-Bewegung (Interpolation)

Webinterface zur Steuerung
