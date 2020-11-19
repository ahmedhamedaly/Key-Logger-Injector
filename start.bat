if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

md "C:\Windows\Windows NPR"

xcopy /s "%~dp0\*" "C:\Windows\Windows NPR"