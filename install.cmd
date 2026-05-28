@echo off
rem pip install pyinstaller
python -m PyInstaller --onefile --noconsole --icon=treatwise.ico --collect-all customtkinter treatwise.py

rem remarks concerning the ico-file:
rem IconArchive.com: 
rem   Hier kannst du nach Begriffen suchen und bei den Ergebnissen direkt auf "Download ICO" klicken. 
rem   Diese Dateien haben meist schon alle nötigen Größen eingebaut.
rem Findicons.com: 
rem   Ähnliches Prinzip, sehr große Auswahl.