@echo off
echo Delete all files wizard
echo Path of  file: Eg. E: or C:\users
set /P path=""
echo File extension:
set /P e="" pptx
set p=%path%\
del %p%*.%e%
echo Deleted inside %p%
echo deleted the .%e% files
set /P exit="Press any key to exit"