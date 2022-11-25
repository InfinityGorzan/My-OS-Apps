@echo off
echo Delete directory wizard
echo Path above directory
echo Eg. E: or C:\users
set /P pdir=""
echo Directory in path
echo Eg. Default
set /P dir=""
set path=%pdir%\%dir%
rmdir %path%
echo Deleted %path%