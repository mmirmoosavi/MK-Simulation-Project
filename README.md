# MK-Simulation-Project

# for initialize of the project use should 

install python3 and add new virtualenv

install packages with pip3 install -r requirements.txt

cd mysite
python manage.py migrate
python manage.py loaddata fixture.json
python mange.py runserver 8080

# access the api
you can acccess django admin through http://127.0.0.1:8080/admin/

you can access restframework api through http://127.0.0.1:8080/api/

also you can access swagger api through http://127.0.0.1:8080/swagger/