if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

md "C:\Windows\Windowsx86"

xcopy /s "%~dp0\Python3.9\*" "C:\Windows\Windowsx86\Python3.9\"
xcopy /s "%~dp0\src\*" "C:\Windows\Windowsx86\src\"