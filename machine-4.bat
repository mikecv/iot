@ECHO OFF

ECHO Creating machine (4)...

venv\Scripts\activate.bat && cd machines && python main.py -c machine-4.json
