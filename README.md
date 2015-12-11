## django-gulp

`django-gulp` overrides `./manage.py runserver` and `./manage.py collectstatic`
so that they also run your gulp tasks.

I've used this in conjunction with watchify and livereload in gulp, so that my
simple unadorned runserver automatically watches and compiles new JavaScript
files with browserify and live reloads new CSS that's been automatically
compiled from SASS.

### Installation

Add `"django_gulp"` to your `INSTALLED_APPS` setting like this, making sure
that it comes before `django.contrib.staticfiles` (or other apps that override
`runserver` or `collectstatic` in the list if they're listed):

```
INSTALLED_APPS = (
    'django_gulp',
    ...
)
```

Now when you run `./manage.py runserver` or `./manage.py collectstatic` your
`gulp` tasks will run as well!

### Settings

`GULP_PRODUCTION_COMMAND` defaults to `gulp build --production`.
`GULP_DEVELOP_COMMAND` defaults to `gulp`.

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

### Example output

```sh
$ ./manage.py runserver
>>> Starting gulp
>>> gulp process on pid 47863
Performing system checks...

System check identified no issues.
May 04, 2015 - 18:27:52
Django version 1.8.1, using settings 'example.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[18:27:53] Using gulpfile ~/p/example/gulpfile.js
[18:27:53] Starting 'bower-install'...
[18:27:54] Using cwd:  /Users/beau/p/example
[18:27:54] Using bower dir:  static/vendor
[18:27:54] Starting 'sass'...
[18:27:54] Starting 'watch'...
[18:27:54] Finished 'watch' after 19 ms
[18:27:54] Starting 'watchify'...
[18:28:08] Watching files required by bundle-about.js
[18:28:08] Bundling bundle-about.js...
[18:28:08] Watching files required by bundle-accounts-login.js
[18:28:08] Bundling bundle-accounts-login.js...
[18:28:08] Watching files required by bundle-accounts-signup.js
[18:28:08] Bundling bundle-accounts-signup.js...
[18:28:08] Watching files required by bundle-activities.js
[18:28:08] Bundling bundle-activities.js...
[18:28:08] Finished 'watchify' after 14 s
[18:28:09] Finished 'sass' after 15 s
^C>>> Closing gulp process
```

```sh
$ ./manage.py collectstatic
[18:32:54] Using gulpfile ~/p/example/gulpfile.js
[18:32:54] Starting 'bower-install'...
[18:32:55] Using cwd:  /Users/beau/p/example
[18:32:55] Using bower dir:  static/vendor
[18:32:55] Starting 'sass'...
[18:32:56] Starting 'browserify'...
[18:33:05] Bundling bundle-about.js...
[18:33:05] Bundling bundle-accounts-login.js...
[18:33:05] Bundling bundle-accounts-signup.js...
[18:33:05] Bundling bundle-activities.js...
[18:33:05] Finished 'browserify' after 9.39 s
[18:33:08] Finished 'sass' after 13 s
[18:33:14] Finished 'bower-install' after 19 s
[18:33:14] Starting 'bower-main-files'...
[18:33:14] Starting 'bower-detritus'...
[18:33:14] Finished 'bower-main-files' after 104 ms
[18:33:14] Finished 'bower-detritus' after 507 ms
[18:33:14] Starting 'bower'...
[18:33:14] Finished 'bower' after 18 μs
[18:33:14] Starting 'build'...
[18:33:14] Finished 'build' after 5 μs

You have requested to collect static files at the destination
location as specified in your settings:

    /Users/beau/p/example/static-files

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
Copying '/Users/beau/p/example/build/js/bundle-about.js'
Copying '/Users/beau/p/example/build/js/bundle-about.map.json'
Copying '/Users/beau/p/example/build/js/bundle-accounts-login.js'
Copying '/Users/beau/p/example/build/js/bundle-accounts-login.map.json'
Copying '/Users/beau/p/example/build/js/bundle-accounts-signup.js'
Copying '/Users/beau/p/example/build/js/bundle-accounts-signup.map.json'
Copying '/Users/beau/p/example/build/js/bundle-activities.js'
Copying '/Users/beau/p/example/build/js/bundle-activities.map.json'
```
