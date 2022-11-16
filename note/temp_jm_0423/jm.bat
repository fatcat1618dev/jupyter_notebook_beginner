@echo off
set $=--File Processing--v1.01.20220401--
title %$%
set Path=%cd%
set ac= &set cc= &set ec=  
color 0A

:ENTER
echo.
echo 	^>^>^>¡¾  Archived  ¡¿ --1-- ^>^>^> 
echo 	^>^>^>¡¾ Processed ¡¿  --2-- ^>^>^> 
echo 	^>^>^> ***Clear All ***--3-- ^>^>^> 
::echo 	^>^>^> Processed Clear --4-- ^>^>^>
::echo 	^>^>^> Archived Clear ***5*** ^>^>^>
echo 	^>^>^>       EXIT      --4-- ^>^>^>
echo.

::  /p
set /p KEY=¡¾SELECT¡¿
if %KEY% == 1 goto ONE 
if %KEY% == 2 goto TWO  
if %KEY% == 3 goto Three
::if %KEY% == 4 goto Four
::if %KEY% == 5 goto Five
if %KEY% == 4 goto EXIT

::%par%%par1%
:ONE  
copy %ac%%Path%\Original\*.*%ec%%cc% %ec%%ac%%Path%\Archived\*.*.rfvabc%cc% >nul 2>nul
goto ENTER

:TWO  
copy %cc%%Path%\Archived\*.rfvabc%ac%%ec% %ec%%cc%%Path%\Processed\*.%ac% >nul 2>nul
goto ENTER

:EXIT
::pause
exit

:Three
del %Path%\Original\*.* /f/q >nul 2>nul
del %Path%\Archived\*.* /f/q >nul 2>nul
del %Path%\Processed\*.* /f/q >nul 2>nul
goto ENTER
