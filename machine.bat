@ECHO OFF

ECHO Creating machine...

venv\Scripts\activate.bat && cd machines && python main.py
