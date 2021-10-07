@ECHO OFF

ECHO Creating machine (2)...

venv\Scripts\activate.bat && cd machines && python main.py -c machine-2.json
