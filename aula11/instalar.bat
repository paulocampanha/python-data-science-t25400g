@echo off
REM Script para instalar bibliotecas Python: numpy, pandas e matplotlib

echo Instalando numpy, pandas e matplotlib...
py -m pip install --upgrade pip
py -m pip install numpy pandas matplotlib

echo.
echo Instalação concluída!
pause
