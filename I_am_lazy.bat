@echo off

REM Load environment variables from .env file
if exist .env (
    for /F "tokens=1,* delims==" %%A in (.env) do (
        set %%A=%%B
    )
) else (
    echo .env file not found. Please create one with the VENV variable set.
    exit /b 1
)

REM Check if VENV is set
if "%VENV%"=="" (
    echo VENV variable not set in .env file. Please specify the path to your virtual environment.
    exit /b 1
)

REM Activate the virtual environment
echo Activating virtual environment...
call "%VENV%"
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
)

REM Run the Streamlit app
echo Launching the Streamlit app...
streamlit run app.py

REM Keep the command prompt open
pause
