# Test task "ToDo List"
## How to run:
1. Install python3
2. Install pip
3. Install project dependencies
```sh
pip install -r requirements.txt
```
4. Make DB migrations
```sh
python3 manage.py makemigrations
```
```sh
python3 manage.py migrate
```
5. Run the project
```sh
python3 manage.py runserver
```
6. Deployed project on development server usually available at http://127.0.0.1:8000/
