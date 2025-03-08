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

REM Prompt the user to choose which application to run
echo.
echo Please choose which application to run:
echo   1 - Streamlit App
echo   2 - FastAPI App
echo   3 - Both Streamlit and FastAPI Apps
choice /C 123 /M "Enter your choice: "

if errorlevel 3 (
    echo Launching both Streamlit and FastAPI apps...
    start cmd /k "streamlit run app.py"
    start cmd /k "uvicorn api:app --reload"
    goto end
)

if errorlevel 2 (
    echo Launching FastAPI app...
    uvicorn api:app --reload
    goto end
)

if errorlevel 1 (
    echo Launching Streamlit app...
    streamlit run app.py
)

:end
pause
