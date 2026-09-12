#  important codes 
python -m venv .venv
.venv\Scripts\activate
deactivate(to deactivate venv )
pip install -r requirements.txt

uvicorn backend.app.main:app --reload

# process 
