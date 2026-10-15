import time
import treatwise

def test_openAppAndClose():
    app = treatwise.TaskListApp()

    # Fenster sofort vor dem Rendering-System verstecken
    app.withdraw()

    # Events im Hintergrund abarbeiten (ohne Grafik-Output)
    app.update_idletasks()
    app.update()

    # Interaktion simulieren: Button-Callback direkt triggern
    app.exitButton.cget("command")()
    
    # GUI-Zustand ohne visuelle Verzögerung abfragen
    app.update()

    # Aufräumen
    # app.destroy()