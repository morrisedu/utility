# my_utility
Utility Application* Link to live site: [utility](https://utils-staging.herokuapp.com/)

use the following credentials:
    username: testuser
    password: testpassword

## Description
An application to track basic quantifiable usages of day to day life

## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git https://github.com/morrisedu/utility.git
        $ cd utility

## Running the Application
* Install virtual environment using `$ python3 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3 pip install -r requirements.txt`

* Set the following configuration instances in a .env file in the root directory
    ```env
        SECRET_KEY='generate a secret key'
        DEBUG=True
        DB_NAME='the database name'
        DB_USER='your database username'
        DB_PASSWORD='your database password'
        DB_HOST='127.0.0.1'
        MODE='dev'
        ALLOWED_HOSTS='*'
        DISABLE_COLLECTSTATIC=1
        DATABASE_URL = ''
    ```
* To run the application, in your terminal:

        
        
## Testing the Application
* To run the tests for the class file:

        $ python3 manage.py  runserver
        
        
## Built With

* [Python3](https://docs.python.org/3/)
* Django
* Django Rest Framework
* Javascript (Ajax, ChartJS)
* Boostrap4
* HTML
* CSS


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :eduumorris@gmail.com

### License
[MIT](https://github.com/sawe-daisy/findjobo/blob/master/LICENSE)

Copyright (c) 2022 **eduumorris**


