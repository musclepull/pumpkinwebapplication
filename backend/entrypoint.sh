
  # VARIBLES
APPDIR="/api"
export PYTHONPATH=/api

cd ${APPDIR}

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 ./src/app.py
