@echo off
:: Change to the script's directory
cd /d %~dp0

:: Create the virtual environment
echo Creating virtual environment...
py -m venv MAIN\venv

:: Activate the virtual environment
echo Activating virtual environment...
call MAIN\venv\Scripts\activate.bat

:: Change to the MAIN directory
cd MAIN

:: Install required Python packages
echo Installing required packages...
pip install -r requirements.txt

:: Run the Django development server
echo Starting the Django development server...
py manage.py runserver

:: Keep the command prompt open after running the server
pause
