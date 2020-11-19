if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

md "C:\Windows\Windows NPR"

copy "%~dp0\src\*.*" "C:\Windows\Windows NPR"