# WeatherAPI

WeatherAPI is a service based on openweathermap

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```bash
# 1-create a virtual enviroment 
virtualenv env
# active a virtual enviroment 
# Unix users
source env/bin/activate
# 2-install requirements
pip install -r requirements.txt
# 3-migrate the default migrations
python manage.py migrate

```

## Usage

```python
python manage.py runserver
```
Open browser using port 8000 and you can check the urls working in this API

http://localhost:8000/weather?city=Bogota&country=co

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)