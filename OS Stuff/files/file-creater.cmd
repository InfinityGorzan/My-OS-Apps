@echo off
echo Create new file wizard
echo Path of new file: Eg. E: or C:\users
set /P path=""
echo Name of new file:
set /P name=""
echo File extension:
set /P e=""
set p=%p%\
echo Created using file-creater.cmd> %p%%name%.%e%
set file=%path%\%name%.%e%
echo Created at %file%
set /P exit="Press any key to exit"