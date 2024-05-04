In order to run the project, please perform :

1. create a virtual environment :
pythom -m venv venv

2. activate the created environment :
venv\Scripts\activate

3. install dependencies :
pip install -r requirements.txt

4. create db tables :
python manage.py makemigrations
python manage.py migrate

5. run a local server :
python manage.py runserver