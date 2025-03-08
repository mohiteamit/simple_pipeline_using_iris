@echo off
REM Reads the .env file and calls the virtual environment activation script

for /F "usebackq tokens=1,* delims==" %%a in (".env") do (
    if /I "%%a"=="VENV" (
        call %%b
    )
)
