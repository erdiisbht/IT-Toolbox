import tkinter as tk
from tkinter import messagebox
import subprocess

def run_command(command):
    """Führe einen Befehl aus und zeige das Ergebnis in einem Fenster an."""
    try:
        # Befehl ausführen
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding='utf-8', errors='ignore')
        output = result.stdout if result.stdout else "Der Befehl wurde erfolgreich ausgeführt."
        messagebox.showinfo("Ergebnis", output)
    except Exception as e:
        messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")

def ping_test(ip_address):
    """Führe einen Ping-Test aus."""
    if ip_address:
        command = f'ping {ip_address}'  # Ping-Befehl
        run_command(command)  # Ping-Test ausführen
    else:
        messagebox.showwarning("Warnung", "Bitte geben Sie eine gültige IP-Adresse ein.")

def open_ping_window():
    """Öffne ein neues Fenster für den Ping-Test."""
    ping_window = tk.Toplevel(root)
    ping_window.title("Ping-Test")
    ping_window.geometry("300x150")

    # IP-Adresseingabe
    ip_label = tk.Label(ping_window, text="Bitte geben Sie eine IP-Adresse ein:")
    ip_label.pack(pady=10)

    entry_ip = tk.Entry(ping_window, width=30)
    entry_ip.pack(pady=5)

    # Button, um den Ping-Test zu starten
    ping_button = tk.Button(ping_window, text="Ping-Test starten", 
                            command=lambda: ping_test(entry_ip.get()), 
                            bg="lightblue", width=30, height=2)
    ping_button.pack(pady=10)

    # Fenster anzeigen
    ping_window.mainloop()

# Hauptfenster erstellen
root = tk.Tk()
root.title("IT TOOLBOX - ERDI SABAHAT")
root.geometry("800x600")

# Hauptfenster in der Mitte des Bildschirms platzieren
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Hauptrahmen (für scrollbaren Bereich)
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Canvas und Scrollbar
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1*(event.delta//120), "units"))

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Befehls-Buttons
commands = [
    ("1. Computer- und Benutzername anzeigen", lambda: run_command('echo Computername: %COMPUTERNAME% && echo Aktiver Benutzer: %USERNAME%')),
    ("2. Computernummer anzeigen", lambda: run_command('wmic bios get serialnumber')),
    ("3. Computerhersteller und -modell anzeigen", lambda: run_command('wmic computersystem get manufacturer,model')),
    ("4. Hardwareinformationen anzeigen", lambda: run_command('systeminfo')),
    ("5. Führe einen Ping-Test aus (Bitte geben Sie eine IP-Adresse ein)", lambda: open_ping_window()), 
    ("6. Windows Updates überprüfen und installieren", lambda: run_command('powershell -Command "Install-Module PSWindowsUpdate -Force -Confirm:$false; Get-WindowsUpdate -Install -AcceptAll -AutoReboot"')),
    ("7. Daten sichern", lambda: run_command('echo Daten wurden erfolgreich gesichert. Die Sicherung muss manuell durchgeführt werden.')),
    ("8. Windows Lizenzstatus anzeigen", lambda: run_command('slmgr /xpr')),
    ("9. Aktive Windows Lizenz anzeigen", lambda: run_command('slmgr /dlv')),
    ("10. Windows-Version anzeigen", lambda: run_command('start winver')),
    ("11. Windows-Update-Status anzeigen", lambda: run_command('wmic qfe get HotfixID,InstalledOn')),
    ("12. Apps im Windows Store aktualisieren", lambda: run_command('start ms-windows-store://update')),
    ("13. Alle installierten Programme aktualisieren", lambda: run_command('echo Programme müssen manuell aktualisiert werden.')),
    ("14. Windows-Systemdateien reparieren", lambda: run_command('sfc /scannow')),
    ("15. Windows-Datenträgerbereinigung starten", lambda: run_command('cleanmgr')),
    ("16. Temporäre Dateien löschen", lambda: run_command('del /q/f/s %temp%\\*')),
    ("17. Systeminformationen anzeigen", lambda: run_command('msinfo32')),
    ("18. Benutzerkonten auflisten", lambda: run_command('net user')),
    ("19. Wi-Fi-Passwort anzeigen", lambda: run_command('netsh wlan show profile name=* key=clear')),
    ("20. IP-Adresse anzeigen", lambda: run_command('ipconfig')),
    ("21. Alle IP-Konfigurationen anzeigen", lambda: run_command('ipconfig /all')),
    ("22. IP-Konfiguration freigeben", lambda: run_command('ipconfig /release')),
    ("23. IP-Konfiguration erneuern", lambda: run_command('ipconfig /renew')),
    ("24. DNS-Cache leeren", lambda: run_command('ipconfig /flushdns')),
    ("25. Druckerstatus anzeigen", lambda: run_command('wmic printer get name,status')),
    ("26. Installierte Drucker auflisten", lambda: run_command('wmic printer list brief')),
    ("27. Drucker neu starten", lambda: run_command('net stop spooler && net start spooler')),
    ("28. Druckwarteschlange leeren", lambda: run_command('net stop spooler && del /q/f/s %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler')),
    ("29. Letztes Formatierungsdatum anzeigen", lambda: run_command('echo Dieses Datum muss manuell überprüft werden.')),
    ("30. Firewall aktivieren", lambda: run_command('netsh advfirewall set allprofiles state on')),
    ("31. Firewall deaktivieren", lambda: run_command('netsh advfirewall set allprofiles state off')),
    ("32. BIOS-Einstellungen öffnen", lambda: run_command('start ms-settings:recovery')),
    ("33. Im abgesicherten Modus starten", lambda: run_command('bcdedit /set {default} safeboot minimal && shutdown /r')),
    ("34. Speicherstatus anzeigen", lambda: run_command('wmic logicaldisk get size,freespace,caption')),
    ("35. Festplatte scannen", lambda: run_command('chkdsk')),
    ("36. Festplattenstatus überprüfen", lambda: run_command('wmic diskdrive get status')),
    ("37. CPU-Informationen anzeigen", lambda: run_command('wmic cpu get name,CurrentClockSpeed')),
    ("38. RAM optimieren", lambda: run_command('echo RAM-Optimierung erfordert ein Drittanbieter-Tool.')),
    ("39. RAM-Nutzung anzeigen", lambda: run_command('wmic OS get FreePhysicalMemory')),
    ("40. Gruppenrichtlinien aktualisieren", lambda: run_command('gpupdate /force')),
    ("41. Computer herunterfahren", lambda: run_command('shutdown /s')),
    ("42. Computer neu starten", lambda: run_command('shutdown /r')),
    ("43. Beenden", root.quit),
]

# Butons zur Seite fügen und mittig anordnen
for text, command in commands:
    button = tk.Button(scrollable_frame, text=text, command=command, width=50, height=1, bg="lightblue")
    button.pack(pady=5)

# Zeilen und Spalten des Rahmens konfigurieren, um die Buttons zu zentrieren
scrollable_frame.grid_rowconfigure(0, weight=1, minsize=30)
scrollable_frame.grid_columnconfigure(0, weight=1)

# Tkinter Hauptschleife
root.mainloop()
