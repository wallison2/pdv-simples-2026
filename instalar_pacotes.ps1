Write-Host "Ativando o ambiente virtual..."
& ".\venv\Scripts\Activate.ps1"

Write-Host "Instalando pacotes um por um..."

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

Write-Host "`nTodos os pacotes foram instalados com sucesso."
pause
