@echo off
REM Hash Table Simulator - Quick Launcher
REM This batch file helps you quickly run any part of the simulator

echo.
echo ========================================
echo   Hash Table Simulator - Quick Launcher
echo ========================================
echo.
echo What would you like to do?
echo.
echo 1. Test Setup (Verify everything works)
echo 2. Launch GUI (Graphical Interface)
echo 3. Launch Console (Text Interface)
echo 4. Run Demo Examples
echo 5. Exit
echo.

choice /c 12345 /n /m "Enter your choice (1-5): "

if errorlevel 5 goto :exit
if errorlevel 4 goto :demos
if errorlevel 3 goto :console
if errorlevel 2 goto :gui
if errorlevel 1 goto :test

:test
echo.
echo Running test setup...
echo.
C:/Users/itsha/Hashing_Project/.venv/Scripts/python.exe test_setup.py
pause
goto :menu

:gui
echo.
echo Launching GUI...
echo.
start C:/Users/itsha/Hashing_Project/.venv/Scripts/python.exe gui_simulator.py
goto :exit

:console
echo.
echo Launching Console Interface...
echo.
C:/Users/itsha/Hashing_Project/.venv/Scripts/python.exe console_simulator.py
pause
goto :menu

:demos
echo.
echo Running Demo Examples...
echo.
C:/Users/itsha/Hashing_Project/.venv/Scripts/python.exe demo_examples.py
pause
goto :menu

:menu
echo.
echo.
goto :eof

:exit
echo.
echo Thank you for using Hash Table Simulator!
echo.
