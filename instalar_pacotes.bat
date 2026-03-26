@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando pacotes um por um...
pip install PySide6
pip install reportlab
pip install matplotlib
pip install pandas
pip install openpyxl
pip install flask
pip install flask-basicauth
pip install requests
pip install uvicorn
pip install pillow
pip install pywin32
pip install psutil
pip install fastapi
pip install pydantic

echo.
echo Todos os pacotes foram instalados.
pause
