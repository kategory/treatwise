from customtkinter import *
from definitions import currencyName
from task import *
from datetime import datetime

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
        self.tasks = Tasks([
            Task( "2026-04-16", "Einkaufsliste prüfen", "Offen", 10 ),
            Task( "2026-04-16", "Taschen packen", "Fertig", 15),
            Task( "2026-04-17", "Hausaufgaben kontrollieren", "Offen", 5),
            Task( "2026-04-17", "Rechnung ausdrucken", "Offen", 5),
            Task( "2026-04-18", "Termin bestätigen", "Fertig", 2),
            Task( "2026-04-18", "Projektbesprechung vorbereiten", "Offen", 20),
            Task( "2026-04-19", "Mail beantworten", "Fertig", 5),
            Task( "2026-04-19", "Update installieren", "Offen", 10),
            Task( "2026-04-20", "Präsentation üben", "Offen", 15),
            Task( "2026-04-20", "Benutzerfeedback lesen", "Fertig", 10),
            Task( "2026-04-21", "Bericht fertigstellen", "Offen", 25),
            Task( "2026-04-21", "Fotos sortieren", "Fertig", 10),
            Task( "2026-04-22", "Software testen", "Offen", 30),
            Task( "2026-04-22", "Budget prüfen", "Fertig", 15),
            Task( "2026-04-23", "Backup erstellen", "Offen", 5),
            Task( "2026-04-23", "Workshop planen", "Fertig", 20),
            Task( "2026-04-24", "Material bestellen", "Offen", 10),
            Task( "2026-04-24", "Website aktualisieren", "Fertig", 15),
            Task( "2026-04-25", "Telefonkonferenz führen", "Offen", 10),
            Task( "2026-04-25", "Termin eintragen", "Fertig", 2),
            Task( "2026-07-09", "Git erklären", "Offen", 50)
        ])

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

        # Sort state: column index (0..3) and direction
        self.sortColumn = None
        self.sortAscending = True

        # Widgets state
        self.statusButtons = []

        # Render the initial table (will use current sort state)
        self.renderTable()

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
        task = self.tasks.collection[idx]
        if task.status == "Offen":
            task.status = "Fertig"
        else:
            task.status = "Offen"

        # update button appearance (buttons correspond to current rendered order)
        try:
            btn = self.statusButtons[idx]
            statusColor = "green" if task.status == "Fertig" else "orange"
            btn.configure(text=task.status, text_color=statusColor)
        except IndexError:
            pass

        # Reapply sort and re-render to preserve ordering
        self.applySortAndRender()
        self.updateRewardSum()

    def updateRewardSum(self, *args):
        self.rewardSumLabel.configure(text=f"Summe {currencyName}: {self.tasks.reward()}")

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

    # --- Sorting and rendering helpers ---
    def onHeaderClick(self, column):
        # Toggle sort direction when clicking same column
        if self.sortColumn == column:
            self.sortAscending = not self.sortAscending
        else:
            self.sortColumn = column
            self.sortAscending = True

        self.applySortAndRender()

    def applySortAndRender(self):
        self.sortTasks()
        self.renderTable()

    def sortTasks(self):
        col = self.sortColumn
        if col is None:
            return

        def date_key(task):
            try:
                dt = datetime.strptime(task.date, "%Y-%m-%d")
                return (0, dt)
            except Exception:
                return (1, None)

        def text_key(task):
            try:
                return (0, task.text.lower())
            except Exception:
                return (1, "")

        def status_key(task):
            try:
                return (0, task.status.lower())
            except Exception:
                return (1, "")

        def reward_key(task):
            try:
                return (0, float(task.reward))
            except Exception:
                try:
                    return (0, float(str(task.reward)))
                except Exception:
                    return (1, 0)

        key_funcs = {
            0: date_key,
            1: text_key,
            2: status_key,
            3: reward_key
        }

        key = key_funcs.get(col, text_key)
        # reverse True means descending
        self.tasks.collection.sort(key=key, reverse=(not self.sortAscending))

    def renderTable(self):
        # Clear existing widgets in the frame
        for w in self.taskFrame.winfo_children():
            w.destroy()

        # Recreate column sizing (grid config is lost when widgets destroyed)
        self.taskFrame.grid_columnconfigure(0, minsize=105, weight=0)
        self.taskFrame.grid_columnconfigure(1, minsize=240, weight=1)
        self.taskFrame.grid_columnconfigure(2, minsize=80, weight=0)
        self.taskFrame.grid_columnconfigure(3, minsize=80, weight=0)

        headers = ["Datum", "Aufgabe", "Status", currencyName]
        self.statusButtons = []

        for column, header in enumerate(headers):
            # Add arrow indicator if this is the active sort column
            indicator = ""
            if self.sortColumn == column:
                indicator = " ▲" if self.sortAscending else " ▼"

            headerBtn = CTkButton(
                self.taskFrame,
                text=header + indicator,
                anchor="w",
                font=("Arial", 14, "bold"),
                fg_color="transparent",
                hover_color="gray30",
                command=lambda c=column: self.onHeaderClick(c)
            )
            headerBtn.grid(row=0, column=column, sticky="ew", padx=8, pady=(0, 6))

        for row, task in enumerate(self.tasks.collection, start=1):
            statusColor = "green" if task.status == "Fertig" else "orange"

            dateLabel = CTkLabel(
                self.taskFrame,
                text=task.date,
                anchor="w",
                font=("Arial", 14)
            )
            dateLabel.grid(row=row, column=0, sticky="ew", padx=8, pady=4)

            textLabel = CTkLabel(
                self.taskFrame,
                text=task.text,
                anchor="w",
                font=("Arial", 14)
            )
            textLabel.grid(row=row, column=1, sticky="ew", padx=8, pady=4)

            statusLabel = CTkButton(
                self.taskFrame,
                text=task.status,
                anchor="w",
                font=("Arial", 14),
                text_color=statusColor,
                fg_color="transparent",
                hover_color="gray30",
                command=lambda idx=row-1: self.toggleStatus(idx)
            )
            statusLabel.grid(row=row, column=2, sticky="ew", padx=8, pady=4)
            self.statusButtons.append(statusLabel)

            rewardEntry = CTkEntry(
                self.taskFrame,
                textvariable=StringVar(value=str(task.reward)),
                width=60,
                font=("Arial", 14)
            )
            rewardEntry.grid(row=row, column=3, sticky="e", padx=8, pady=4)

    # Die Methode, die den Knopf-Klick verarbeitet
    def exitApp(self):
        self.destroy()

# --- Programmstart ---
if __name__ == "__main__":
    myApp = TaskListApp()
    myApp.mainloop()


