# Django Restaurant

A Backend for restaurant management which served using GraphQL built using Django.

## Technologies Used
- Django
- PostgreSQL

## Development

### Requirements
1. Python 3.9 or higher
2. PostgreSQL
3. Redis
4. Docker
5. Docker Compose
6. Virtualenv (optional)

### Running Locally
1. Copy `.env.eample` file to `.env`
2. If you have docker installed, run `docker-compose up -d` to bring up the DB and Redis
3. Update he DB credential in `.env`
4. Run `pip install -r requirements.txt` to install the dependencies. It is recommended to use virtualenv.
5. Run `python manage.py migrate` to migrate the db
6. Run `python manage.py loaddata seeds/types.json`
7. Run `python manage.py loaddata seeds/packages.json`
8. Run `python manage.py loaddata seeds/data.json`
9. Run `python manage.py runserver` to start the development server at `http://127.0.0.1:8000`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
