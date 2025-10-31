@echo off
REM Quick Deployment Script for Hash Table Simulator
REM This script helps you deploy to Vercel quickly

echo ============================================
echo Hash Table Simulator - Vercel Deployment
echo ============================================
echo.

REM Change to the web-app directory
cd /d "%~dp0"

echo Current directory: %CD%
echo.

echo Choose deployment option:
echo 1. Deploy to Preview (for testing)
echo 2. Deploy to Production
echo 3. Check deployment status
echo 4. View logs
echo 5. Exit
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Deploying to Preview...
    echo This will create a temporary URL for testing.
    echo.
    npx vercel
) else if "%choice%"=="2" (
    echo.
    echo Deploying to Production...
    echo This will update your live site.
    echo.
    npx vercel --prod
) else if "%choice%"=="3" (
    echo.
    echo Checking deployment status...
    echo.
    npx vercel list
) else if "%choice%"=="4" (
    echo.
    echo Viewing recent logs...
    echo.
    npx vercel logs
) else if "%choice%"=="5" (
    echo.
    echo Exiting...
    exit /b 0
) else (
    echo.
    echo Invalid choice. Please run the script again.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Deployment complete!
echo ============================================
echo.
pause
