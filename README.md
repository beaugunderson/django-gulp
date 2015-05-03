## django-gulp

### Installation

Add "polls" to your `INSTALLED_APPS` setting like this:

```
INSTALLED_APPS = (
    'django_gulp',
    ...
)
```

Now when you run `./manage.py runserver` or `./manage.py collectstatic` your
`gulp` tasks will run as well!

### Heroku

`django-gulp` works on Heroku! You'll just need to use buildpack-multi and make
sure your `.buildpacks` file looks like this:

```
https://github.com/heroku/heroku-buildpack-nodejs.git
https://github.com/heroku/heroku-buildpack-python.git
```

To use buildback-multi set your configuration like so:

```
$ heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-multi.git
```
