from customtkinter import *

# Klassen werden großgeschrieben (PascalCase) Huch
class TaskListApp(CTk):
    
    # Methoden fangen klein an (camelCase)
    def __init__(self):
        super().__init__()

        # Fenster-Grundeinstellungen
        self.title("Aufgabenliste")
        self.geometry("500x520")
        
        # Optional: Das Design-Thema festlegen (System, Dark, Light)
        set_appearance_mode("System")
        set_default_color_theme("blue")

        # Aufgaben-Daten im Sourcecode hardcodiert
        self.tasks = [
            {"date": "2026-04-16", "text": "Einkaufsliste prüfen", "status": "Offen"},
            {"date": "2026-04-16", "text": "Taschen packen", "status": "Fertig"},
            {"date": "2026-04-17", "text": "Hausaufgaben kontrollieren", "status": "Offen"},
            {"date": "2026-04-17", "text": "Rechnung ausdrucken", "status": "Offen"},
            {"date": "2026-04-18", "text": "Termin bestätigen", "status": "Fertig"},
            {"date": "2026-04-18", "text": "Projektbesprechung vorbereiten", "status": "Offen"},
            {"date": "2026-04-19", "text": "Mail beantworten", "status": "Fertig"},
            {"date": "2026-04-19", "text": "Update installieren", "status": "Offen"},
            {"date": "2026-04-20", "text": "Präsentation üben", "status": "Offen"},
            {"date": "2026-04-20", "text": "Benutzerfeedback lesen", "status": "Fertig"},
            {"date": "2026-04-21", "text": "Bericht fertigstellen", "status": "Offen"},
            {"date": "2026-04-21", "text": "Fotos sortieren", "status": "Fertig"},
            {"date": "2026-04-22", "text": "Software testen", "status": "Offen"},
            {"date": "2026-04-22", "text": "Budget prüfen", "status": "Fertig"},
            {"date": "2026-04-23", "text": "Backup erstellen", "status": "Offen"},
            {"date": "2026-04-23", "text": "Workshop planen", "status": "Fertig"},
            {"date": "2026-04-24", "text": "Material bestellen", "status": "Offen"},
            {"date": "2026-04-24", "text": "Website aktualisieren", "status": "Fertig"},
            {"date": "2026-04-25", "text": "Telefonkonferenz führen", "status": "Offen"},
            {"date": "2026-04-25", "text": "Termin eintragen", "status": "Fertig"}
        ]

        # Überschrift (Hallo)
        self.titleLabel = CTkLabel(
            self,
            text="Aufgaben für diese Woche",
            font=("Arial", 20, "bold")
        )
        self.titleLabel.pack(pady=(20, 10))

        # Scrollbarer Bereich fuer die Aufgabenliste
        self.taskFrame = CTkScrollableFrame(self, width=460, height=360)
        self.taskFrame.pack(padx=20, pady=(0, 10), fill="both", expand=True)

        self.taskFrame.grid_columnconfigure(0, minsize=105, weight=0)
        self.taskFrame.grid_columnconfigure(1, minsize=240, weight=1)
        self.taskFrame.grid_columnconfigure(2, minsize=80, weight=0)

        headers = ["Datum", "Aufgabe", "Status"]
        for column, header in enumerate(headers):
            headerLabel = CTkLabel(
                self.taskFrame,
                text=header,
                anchor="w",
                font=("Arial", 14, "bold")
            )
            headerLabel.grid(row=0, column=column, sticky="ew", padx=8, pady=(0, 6))

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

            statusLabel = CTkLabel(
                self.taskFrame,
                text=task["status"],
                anchor="w",
                font=("Arial", 14),
                text_color=statusColor
            )
            statusLabel.grid(row=row, column=2, sticky="ew", padx=8, pady=4)

        # Exit-Knopf
        self.exitButton = CTkButton(
            self, 
            text="Exit", 
            command=self.exitApp,
            fg_color="darkred",
            hover_color="red"
        )
        self.exitButton.pack(pady=(0, 20))

    # Die Methode, die den Knopf-Klick verarbeitet
    def exitApp(self):
        self.destroy()

# --- Programmstart ---
if __name__ == "__main__":
    myApp = TaskListApp()
    myApp.mainloop()


