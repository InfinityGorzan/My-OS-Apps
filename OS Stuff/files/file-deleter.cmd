@echo off
echo Delete file wizard
echo Path of  file: Eg. E: or C:\users
set /P path=""
echo Name of  file:
set /P name=""
echo File extension:
set /P e=""
set p=%p%\
del %p%%name%.%e%
set file=%path%\%name%.%e%
echo Deleted %file%
set /P exit="Press any key to exit"