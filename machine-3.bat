@ECHO OFF

ECHO Creating machine (3)...

venv\Scripts\activate.bat && cd machines && python main.py -c machine-3.json
