# django-lightweight-tests
Run Django tests with optimization options to decrease runtime while keeping them trustable.

In our tests using SQL Server, a 30 minutes runtime was reduced by 90%.

Most of these ideas were based on the article [7 Ways to Speed Up Your Django Test Suite](https://brobin.me/blog/2016/08/7-ways-to-speed-up-your-django-test-suite/) by Tobin Brown.

## How it works
This package removes the following functionalities from Django, which greatly reduces tests runtime:

#### Migrations
Unless you test your migration files, there is no need to run all migrations everytime you run your test suite. So this option creates all necessary database structure without looking at your migration files.

#### Warnings
Supress warnings to reduce print statements and make your test output cleaner.

#### Password hasher
If your tests create a lot of users, it may be useful to use a simple password hasher.

#### Middlewares
Adds only necessary middlewares to the request object.

#### DEBUG = False
Decreases Django overhead when debugging is activated.

#### SQLite
Run tests using SQLite.

## How to install
Add this line to your `requirements.txt`:
```
-e git+https://github.com/luisccf/django-lightweight-tests.git#egg=django-lightweight-tests
```
Then simply run
```
pip install -r requirements.txt
```

## How to use
Add the following code to your `manage.py`:
```python
import sys
from django_lightweight_tests import LightweightTest

...

is_testing = 'test' in sys.argv
if is_testing:
    LightweightTest()

...

execute_from_command_line(sys.argv)
```

How you check if you are running your tests depends on your test runner. We run our tests using `python manage.py test`, so this check works for us.

When you run your tests, pass the option `--light`:
```sh
python manage.py test --light
```

You can change the arg name when instantiating the class:
```python
LightweightTest(cmd_option='--opt')
```
```sh
python manage.py test --opt
```
