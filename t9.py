@echo off
echo Installing ipykernel...
%PYTHON_HOME%\python.exe -m pip install --upgrade pip
%PYTHON_HOME%\python.exe -m pip install ipykernel
%PYTHON_HOME%\python.exe -m ipykernel install --user --name=customenv --display-name "Python (Custom Env)"
echo Done! You can now use it in VS Code!
pause