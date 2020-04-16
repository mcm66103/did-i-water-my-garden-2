# did-i-water-my-garden-1
Did I Water my Garden Demo App pt. 1

## Getting started
`pip install -r requirements.txt`

create a .env file in app/app and set your secret key.

app/app/.env
`SECRET_KEY=your_secret_key`

run your migrations
`python manage.py migrate`

run dev runserver
`python manage.py runserver`

Your database will be empty and this may cause problems at first.

You can populate your database using the commands from step 12 in the instructions.

[tutorial pt. 1](https://read.maverickmoore.com/learn-django-tutorial-startproject/)
