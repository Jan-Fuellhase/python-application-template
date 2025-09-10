@echo off
setlocal

REM Change to the directory of this script
cd /d "%~dp0"

REM Prefer a local virtual environment if present (Windows venv layout)
set "VENV_PY=%~dp0venv\Scripts\python.exe"
if exist "%VENV_PY%" (
  set "PYCMD=%VENV_PY%"
) else (
  REM Try the Python launcher first (recommended on Windows)
  where py >nul 2>nul && (
    set "PYCMD=py -3"
  ) || (
    REM Fallbacks: python, then python3
    where python >nul 2>nul && (
      set "PYCMD=python"
    ) || (
      where python3 >nul 2>nul && (
        set "PYCMD=python3"
      )
    )
  )
)

if not defined PYCMD (
  echo.
  echo ERROR: Could not find Python. Please install Python 3 and ensure it's on PATH.
  echo Visit https://www.python.org/downloads/
  echo.
  pause
  exit /b 1
)

REM Run the application
%PYCMD% "%~dp0main.py"
set "EXITCODE=%ERRORLEVEL%"

if not "%EXITCODE%"=="0" (
  echo.
  echo The application exited with code %EXITCODE%.
  echo Press any key to close this window...
  pause >nul
  exit /b %EXITCODE%
)

endlocal
