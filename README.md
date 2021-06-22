Profile Manager App

Environment 
$ virtualenv -p /usr/bin/python2.7 venv
or 
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
then activate: source venv/bin/activate 
$ pip install -r requirements.txt

$ export FLASK_DEBUG=1
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
$ export UPLOAD_FOLDER=UPLOAD_FOLDER 
$ export ALLOWED_EXTENSIONS={'PDF','JPG','PNG'}
$ flask run
 * Serving Flask app "run"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


 migration

$ flask db stamp head //incase of target db not up to date error 
$ flask db migrate
$ flask db upgrade
