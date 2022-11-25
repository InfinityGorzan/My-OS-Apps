@echo off
echo Please download python from Python.org
echo Press any key if your done
set /P continue=">>>"
pip install PyQt5
pip install PyQt5WebEngine
pip install tk
pip install tqdm
set /P exit="Installed required. Press any key to continue"
echo If you encounter issues, please research how to fix -
echo PIP is not found error. This might be the reason to encounter issues.
echo Please add Python to enviornment variables
set /P over=""