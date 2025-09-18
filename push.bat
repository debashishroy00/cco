@echo off
REM CCOM v0.3 - Quick commit and push to GitHub

echo Committing CCOM v0.3 to GitHub...
echo.

REM Check if git repo exists
if not exist .git (
    echo Initializing git repository...
    git init
    git remote add origin https://github.com/debashishroy00/cco.git
)

REM Show current status
echo Current git status:
git status
echo.

REM Add all files
echo Adding files...
git add .

REM Show what will be committed
echo.
echo Files to be committed:
git diff --staged --name-only
echo.

REM Check if there are changes to commit
git diff --staged --quiet
if %errorlevel% equ 0 (
    echo No changes to commit.
    pause
    exit /b 0
)

REM Get timestamp
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "MIN=%dt:~10,2%" & set "SS=%dt:~12,2%"
set "timestamp=%YYYY%-%MM%-%DD% %HH%:%MIN%"

REM Commit with descriptive message
git commit -m "CCOM v0.3 - Claude Code Integration with prefix-based activation (%timestamp%)"

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin master

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully pushed CCOM v0.3 to GitHub!
    echo.
    echo CCOM v0.3 Features Updated:
    echo   ✅ Claude Code native integration
    echo   ✅ Prefix-based activation ("ccom" commands)
    echo   ✅ Visual engagement indicators
    echo   ✅ Cross-project functionality
    echo.
    echo Test the updates:
    echo   python ccom/cli.py --init
    echo   python ccom/cli.py --status
    echo.
    echo Ready for PyPI (when needed):
    echo   pip install build twine
    echo   python -m build
    echo   python -m twine upload dist/*
) else (
    echo.
    echo ❌ Push failed. Common issues:
    echo   - Check GitHub credentials
    echo   - Ensure remote origin is correct
    echo   - Try: git push --force-with-lease origin main
)

echo.
pause