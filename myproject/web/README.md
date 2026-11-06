# MotoShift
Django + Tailwind (CDN) + JavaScript website for a two-wheeler transport product: doorstep pickup, 360° digital inspection, live GPS, and instant transit insurance.
## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata demo
python manage.py runserver
```
Open http://127.0.0.1:8000/
Demo tracking IDs: `MOT-48291`, `MOT-11004`
Admin: `python manage.py createsuperuser` then http://127.0.0.1:8000/admin/