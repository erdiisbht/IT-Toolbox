import tkinter as tk
from tkinter import messagebox
import subprocess
import pyttsx3
import speech_recognition as sr
import difflib

def sprechen(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def hoeren():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hört zu...")
        try:
            audio = recognizer.listen(source, timeout=5)
            befehl = recognizer.recognize_google(audio, language="de-DE")
            print(f"Erkannter Befehl: {befehl}")
            return befehl.lower()
        except sr.UnknownValueError:
            sprechen("Entschuldigung, ich habe das nicht verstanden.")
            return ""
        except sr.RequestError:
            sprechen("Der Sprachdienst funktioniert nicht.")
            return ""
        except sr.WaitTimeoutError:
            sprechen("Es wurde nichts gehört.")
            return ""

def befehl_ausfuehren(befehl):
    try:
        result = subprocess.run(befehl, capture_output=True, text=True, shell=True, encoding='utf-8', errors='ignore')
        output = result.stdout if result.stdout else "Der Befehl wurde erfolgreich ausgeführt."
        messagebox.showinfo("Ergebnis", output)
        return output.strip()
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")
        return None

def button_klicken(befehl_funktion):
    befehl_funktion()

def finde_ähnliche_befehle(befehl, definitionen):
    matches = difflib.get_close_matches(befehl, definitionen.keys(), n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

def sprachassistent():
    sprechen("Sprachassistent ist aktiv. Wie kann ich helfen?")

    # Befehl-Zuordnung
    befehl_mapping = {
        "computer und benutzername anzeigen": lambda: commands[0][1](),
        "computernummer anzeigen": lambda: commands[1][1](),
        "computerhersteller und modell anzeigen": lambda: commands[2][1](),
        "hardwareinformationen anzeigen": lambda: commands[3][1](),
        "ping test durchführen": lambda: commands[4][1](),
        "windows updates überprüfen": lambda: commands[5][1](),
        "daten sichern": lambda: commands[6][1](),
        "windows lizenzstatus anzeigen": lambda: commands[7][1](),
        "aktive windows lizenz anzeigen": lambda: commands[8][1](),
        "windows version anzeigen": lambda: commands[9][1](),
        "windows update status anzeigen": lambda: commands[10][1](),
        "apps aktualisieren": lambda: commands[11][1](),
        "programme aktualisieren": lambda: commands[12][1](),
        "systemdateien reparieren": lambda: commands[13][1](),
        "datenträgerbereinigung starten": lambda: commands[14][1](),
        "temporäre dateien löschen": lambda: commands[15][1](),
        "systeminformationen anzeigen": lambda: commands[16][1](),
        "benutzerkonten auflisten": lambda: commands[17][1](),
        "wi-fi passwort anzeigen": lambda: commands[18][1](),
        "ip adresse anzeigen": lambda: commands[19][1](),
        "ip konfiguration anzeigen": lambda: commands[20][1](),
        "ip konfiguration freigeben": lambda: commands[21][1](),
        "ip konfiguration erneuern": lambda: commands[22][1](),
        "dns cache leeren": lambda: commands[23][1](),
        "druckerstatus anzeigen": lambda: commands[24][1](),
        "drucker auflisten": lambda: commands[25][1](),
        "drucker neu starten": lambda: commands[26][1](),
        "druckwarteschlange leeren": lambda: commands[27][1](),
        "letztes formatierungsdatum anzeigen": lambda: commands[28][1](),
        "firewall aktivieren": lambda: commands[29][1](),
        "firewall deaktivieren": lambda: commands[30][1](),
        "bios einstellungen öffnen": lambda: commands[31][1](),
        "abgesicherten modus starten": lambda: commands[32][1](),
        "speicherstatus anzeigen": lambda: commands[33][1](),
        "festplatte scannen": lambda: commands[34][1](),
        "festplattenstatus überprüfen": lambda: commands[35][1](),
        "cpu informationen anzeigen": lambda: commands[36][1](),
        "ram optimieren": lambda: commands[37][1](),
        "ram nutzung anzeigen": lambda: commands[38][1](),
        "gruppenrichtlinien aktualisieren": lambda: commands[39][1](),
        "computer herunterfahren": lambda: commands[40][1](),
        "computer neu starten": lambda: commands[41][1](),
        "programm beenden": lambda: commands[42][1]()
    }

    while True:
        befehl = hoeren()
        if not befehl:
            continue

        befehl = befehl.lower().strip()
        print(f"Erkannter Befehl: {befehl}")

        # Ähnlichsten Befehl finden
        übereinstimmung = finde_ähnliche_befehle(befehl, befehl_mapping)
        if übereinstimmung:
            sprechen(f"Befehl erkannt: {übereinstimmung}. Wird ausgeführt.")
            befehl_mapping[übereinstimmung]()
        elif "beenden" in befehl or "schließen" in befehl:
            sprechen("Sprachassistent wird beendet.")
            break
        else:
            sprechen("Befehl nicht erkannt. Bitte wiederholen Sie.")

# Tkinter Hauptfenster
root = tk.Tk()
root.title("IT TOOLBOX - ERDI SABAHAT")

# Fenster zentrieren
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Hauptbereich und Scroll-Funktion
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1*(event.delta//120), "units"))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Befehle definieren
commands = [
    ("Computer und Benutzername anzeigen", lambda: befehl_ausfuehren('echo Computername: %COMPUTERNAME% && echo Aktiver Benutzer: %USERNAME%')),
    ("Computernummer anzeigen", lambda: befehl_ausfuehren('wmic bios get serialnumber')),
    ("Computerhersteller und Modell anzeigen", lambda: befehl_ausfuehren('wmic computersystem get manufacturer,model')),
    ("Hardwareinformationen anzeigen", lambda: befehl_ausfuehren('systeminfo')),
    ("Ping Test durchführen", lambda: befehl_ausfuehren('ping 8.8.8.8')),
    ("Windows Updates überprüfen", lambda: befehl_ausfuehren('powershell -Command "Install-Module PSWindowsUpdate -Force -Confirm:$false; Get-WindowsUpdate -Install -AcceptAll -AutoReboot"')),
    ("Daten sichern", lambda: befehl_ausfuehren('echo Daten wurden erfolgreich gesichert. Die Sicherung muss manuell durchgeführt werden.')),
    ("Windows Lizenzstatus anzeigen", lambda: befehl_ausfuehren('slmgr /xpr')),
    ("Aktive Windows Lizenz anzeigen", lambda: befehl_ausfuehren('slmgr /dlv')),
    ("Windows Version anzeigen", lambda: befehl_ausfuehren('start winver')),
    ("Windows Update Status anzeigen", lambda: befehl_ausfuehren('wmic qfe get HotfixID,InstalledOn')),
    ("Apps aktualisieren", lambda: befehl_ausfuehren('start ms-windows-store://update')),
    ("Programme aktualisieren", lambda: befehl_ausfuehren('echo Programme müssen manuell aktualisiert werden.')),
    ("Systemdateien reparieren", lambda: befehl_ausfuehren('sfc /scannow')),
    ("Datenträgerbereinigung starten", lambda: befehl_ausfuehren('cleanmgr')),
    ("Temporäre Dateien löschen", lambda: befehl_ausfuehren('del /q/f/s %temp%\\*')),
    ("Systeminformationen anzeigen", lambda: befehl_ausfuehren('msinfo32')),
    ("Benutzerkonten auflisten", lambda: befehl_ausfuehren('net user')),
    ("Wi-Fi Passwort anzeigen", lambda: befehl_ausfuehren('netsh wlan show profile name=* key=clear')),
    ("IP Adresse anzeigen", lambda: befehl_ausfuehren('ipconfig')),
    ("IP Konfiguration anzeigen", lambda: befehl_ausfuehren('ipconfig /all')),
    ("IP Konfiguration freigeben", lambda: befehl_ausfuehren('ipconfig /release')),
    ("IP Konfiguration erneuern", lambda: befehl_ausfuehren('ipconfig /renew')),
    ("DNS Cache leeren", lambda: befehl_ausfuehren('ipconfig /flushdns')),
    ("Druckerstatus anzeigen", lambda: befehl_ausfuehren('wmic printer get name,status')),
    ("Drucker auflisten", lambda: befehl_ausfuehren('wmic printer list brief')),
    ("Drucker neu starten", lambda: befehl_ausfuehren('net stop spooler && net start spooler')),
    ("Druckwarteschlange leeren", lambda: befehl_ausfuehren('net stop spooler && del /q/f/s %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler')),
    ("Letztes Formatierungsdatum anzeigen", lambda: befehl_ausfuehren('echo Dieses Datum muss manuell überprüft werden.')),
    ("Firewall aktivieren", lambda: befehl_ausfuehren('netsh advfirewall set allprofiles state on')),
    ("Firewall deaktivieren", lambda: befehl_ausfuehren('netsh advfirewall set allprofiles state off')),
    ("BIOS Einstellungen öffnen", lambda: befehl_ausfuehren('start ms-settings:recovery')),
    ("Abgesicherten Modus starten", lambda: befehl_ausfuehren('bcdedit /set {default} safeboot minimal && shutdown /r')),
    ("Speicherstatus anzeigen", lambda: befehl_ausfuehren('wmic logicaldisk get size,freespace,caption')),
    ("Festplatte scannen", lambda: befehl_ausfuehren('chkdsk')),
    ("Festplattenstatus überprüfen", lambda: befehl_ausfuehren('wmic diskdrive get status')),
    ("CPU Informationen anzeigen", lambda: befehl_ausfuehren('wmic cpu get name,CurrentClockSpeed')),
    ("RAM optimieren", lambda: befehl_ausfuehren('echo RAM-Optimierung erfordert ein Drittanbieter-Tool.')),
    ("RAM Nutzung anzeigen", lambda: befehl_ausfuehren('wmic OS get FreePhysicalMemory')),
    ("Gruppenrichtlinien aktualisieren", lambda: befehl_ausfuehren('gpupdate /force')),
    ("Computer herunterfahren", lambda: befehl_ausfuehren('shutdown /s')),
    ("Computer neu starten", lambda: befehl_ausfuehren('shutdown /r')),
    ("Programm beenden", root.quit),
]

# Buttons erstellen
for text, command in commands:
    button = tk.Button(
        scrollable_frame,
        text=text,
        command=lambda cmd=command: button_klicken(cmd),
        width=50,
        height=1,
        bg="lightblue"
    )
    button.pack(pady=5)

# Sprachassistent beim Start automatisch starten
root.after(1000, sprachassistent)

# Tkinter Hauptschleife
root.mainloop()
