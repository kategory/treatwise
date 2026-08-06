from customtkinter import *
from definitions import currencyName

# Klassen werden großgeschrieben (PascalCase) Huch
class TaskListApp(CTk):
    
    # Methoden fangen klein an (camelCase)
    def __init__(self):
        super().__init__()

        # Fenster-Grundeinstellungen
        self.title("Aufgabenliste")
        self.geometry("600x560")

        # Initialer Zoom-Level
        self.currentScaling = 1.0
        
        # Strg + Mausrad zum Zoomen binden
        self.bind("<Control-MouseWheel>", self.zoom)

        #testKatja
        
        # Optional: Das Design-Thema festlegen (System, Dark, Light)
        set_appearance_mode("System")
        set_default_color_theme("blue")

        # Aufgaben-Daten im Sourcecode hardcodiert
        self.tasks = [
            {"date": "2026-04-16", "text": "Einkaufsliste prüfen", "status": "Offen", "reward": 10},
            {"date": "2026-04-16", "text": "Taschen packen", "status": "Fertig", "reward": 15},
            {"date": "2026-04-17", "text": "Hausaufgaben kontrollieren", "status": "Offen", "reward": 5},
            {"date": "2026-04-17", "text": "Rechnung ausdrucken", "status": "Offen", "reward": 5},
            {"date": "2026-04-18", "text": "Termin bestätigen", "status": "Fertig", "reward": 2},
            {"date": "2026-04-18", "text": "Projektbesprechung vorbereiten", "status": "Offen", "reward": 20},
            {"date": "2026-04-19", "text": "Mail beantworten", "status": "Fertig", "reward": 5},
            {"date": "2026-04-19", "text": "Update installieren", "status": "Offen", "reward": 10},
            {"date": "2026-04-20", "text": "Präsentation üben", "status": "Offen", "reward": 15},
            {"date": "2026-04-20", "text": "Benutzerfeedback lesen", "status": "Fertig", "reward": 10},
            {"date": "2026-04-21", "text": "Bericht fertigstellen", "status": "Offen", "reward": 25},
            {"date": "2026-04-21", "text": "Fotos sortieren", "status": "Fertig", "reward": 10},
            {"date": "2026-04-22", "text": "Software testen", "status": "Offen", "reward": 30},
            {"date": "2026-04-22", "text": "Budget prüfen", "status": "Fertig", "reward": 15},
            {"date": "2026-04-23", "text": "Backup erstellen", "status": "Offen", "reward": 5},
            {"date": "2026-04-23", "text": "Workshop planen", "status": "Fertig", "reward": 20},
            {"date": "2026-04-24", "text": "Material bestellen", "status": "Offen", "reward": 10},
            {"date": "2026-04-24", "text": "Website aktualisieren", "status": "Fertig", "reward": 15},
            {"date": "2026-04-25", "text": "Telefonkonferenz führen", "status": "Offen", "reward": 10},
            {"date": "2026-04-25", "text": "Termin eintragen", "status": "Fertig", "reward": 2},
            {"date": "2026-07-09", "text": "Git erklären", "status": "Offen", "reward": 50},
        ]

        # Überschrift (Hallo)
        self.titleLabel = CTkLabel(
            self,
            text="Aufgaben für diese Woche",
            font=("Arial", 20, "bold")
        )
        self.titleLabel.pack(pady=(20, 10))

        # Scrollbarer Bereich fuer die Aufgabenliste
        self.taskFrame = CTkScrollableFrame(self, width=540, height=360)
        self.taskFrame.pack(padx=20, pady=(0, 10), fill="both", expand=True)

        self.taskFrame.grid_columnconfigure(0, minsize=105, weight=0)
        self.taskFrame.grid_columnconfigure(1, minsize=240, weight=1)
        self.taskFrame.grid_columnconfigure(2, minsize=80, weight=0)
        self.taskFrame.grid_columnconfigure(3, minsize=80, weight=0)

        headers = ["Datum", "Aufgabe", "Status", currencyName]
        for column, header in enumerate(headers):
            headerLabel = CTkLabel(
                self.taskFrame,
                text=header,
                anchor="w",
                font=("Arial", 14, "bold")
            )
            headerLabel.grid(row=0, column=column, sticky="ew", padx=8, pady=(0, 6))

        self.statusButtons = []
        self.rewardVars = []

        for row, task in enumerate(self.tasks, start=1):
            statusColor = "green" if task["status"] == "Fertig" else "orange"

            dateLabel = CTkLabel(
                self.taskFrame,
                text=task["date"],
                anchor="w",
                font=("Arial", 14)
            )
            dateLabel.grid(row=row, column=0, sticky="ew", padx=8, pady=4)

            textLabel = CTkLabel(
                self.taskFrame,
                text=task["text"],
                anchor="w",
                font=("Arial", 14)
            )
            textLabel.grid(row=row, column=1, sticky="ew", padx=8, pady=4)

            statusLabel = CTkButton(
                self.taskFrame,
                text=task["status"],
                anchor="w",
                font=("Arial", 14),
                text_color=statusColor,
                fg_color="transparent",
                hover_color="gray30",
                command=lambda idx=row-1: self.toggleStatus(idx)
            )
            statusLabel.grid(row=row, column=2, sticky="ew", padx=8, pady=4)
            self.statusButtons.append(statusLabel)
            
            rewardVar = StringVar(value=str(task["reward"]))
            rewardVar.trace_add("write", self.updateRewardSum)
            self.rewardVars.append(rewardVar)
            
            rewardEntry = CTkEntry(
                self.taskFrame,
                textvariable=rewardVar,
                width=60,
                font=("Arial", 14)
            )
            rewardEntry.grid(row=row, column=3, sticky="e", padx=8, pady=4)

        # Summen Label
        self.rewardSumLabel = CTkLabel(
            self,
            text=f"Summe {currencyName}: 0",
            font=("Arial", 16, "bold")
        )
        self.rewardSumLabel.pack(pady=(0, 10))

        # Exit-Knopf
        self.exitButton = CTkButton(
            self, 
            text="Exit", 
            command=self.exitApp,
            fg_color="darkred",
            hover_color="red"
        )
        self.exitButton.pack(pady=(0, 20))
        
        self.updateRewardSum()

    def toggleStatus(self, idx):
        task = self.tasks[idx]
        if task["status"] == "Offen":
            task["status"] = "Fertig"
        else:
            task["status"] = "Offen"

        btn = self.statusButtons[idx]
        statusColor = "green" if task["status"] == "Fertig" else "orange"
        btn.configure(text=task["status"], text_color=statusColor)
        
        self.updateRewardSum()

    def updateRewardSum(self, *args):
        total = 0
        for i, task in enumerate(self.tasks):
            if task["status"] == "Fertig":
                try:
                    val = int(self.rewardVars[i].get())
                    total += val
                except ValueError:
                    pass
        self.rewardSumLabel.configure(text=f"Summe {currencyName}: {total}")

    def zoom(self, event):
        # event.delta ist bei Windows ueblicherweise +/- 120
        if event.delta > 0:
            self.currentScaling += 0.1
        elif event.delta < 0:
            self.currentScaling -= 0.1
            
        # Begrenzen wir den Zoom-Level (z.B. zwischen 50% und 250%)
        self.currentScaling = max(0.5, min(self.currentScaling, 2.5))
        
        # Skalierung fuer Widgets und Fenster anwenden
        set_widget_scaling(self.currentScaling)
        set_window_scaling(self.currentScaling)

    # Die Methode, die den Knopf-Klick verarbeitet
    def exitApp(self):
        self.destroy()

# --- Programmstart ---
if __name__ == "__main__":
    myApp = TaskListApp()
    myApp.mainloop()


