@echo off
if not "%1" == "uac" (
echo 申请 UAC 权限...
goto GetUAC
)else ( goto DO )

:GetUAC
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "uac", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"
exit /B

:DO
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"


c:\python27\python.exe %~dp0win_hosts.py
pause