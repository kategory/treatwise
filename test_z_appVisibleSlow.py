import time
import treatwise

def test_openAppAndClose():
    app = treatwise.TaskListApp()

    app.update_idletasks()
    app.update()

    # 1 Sekunde warten, damit du den Screen/das Bild siehts
    time.sleep(1.0)

    # Prüfen, ob das Fenster aufgerufen wurde (Optionaler Assert)
    assert app.winfo_exists()

    # Anwendung sauber beenden und aufräumen
    app.destroy()