@ECHO OFF

ECHO Creating machine.

.\Scripts\activate.bat

cd machines
python main.py
