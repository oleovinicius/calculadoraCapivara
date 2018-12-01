goto MAIN

:MAIN
echo off
cls
echo BEM VINDO
echo Iniciando instalacao de pacotes
echo Inicianto metodo1 (python para um usuario)
pause
goto metodo1

:metodo1
cd C:\Users\%username%\AppData\Local\Programs\Python\Python37-32
python -m pip install --upgrade pip
pip install -r C:\Users\%username%\Documents\calculadoraCapivara\requirements.txt
pip install -r C:\Users\%username%\Documentos\calculadoraCapivara\requirements.txt
echo Iniciando metodo2 (python para todos os usuarios)
goto metodo2

:metodo2
cd C:\Program Files\Python37
pause
python -m pip install --upgrade pip
pause
pip install -r C:\Users\%username%\Documents\calculadoraCapivara\requirements.txt
pause
pip install -r C:\Users\%username%\Documentos\calculadoraCapivara\requirements.txt
