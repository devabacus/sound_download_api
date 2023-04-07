python -m venv env
.\env\Scripts\Activate.ps1

pip install -r requirements.txt

python -m pip freeze > requirements.txt
