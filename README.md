# "Cyber Security Base" course project 1 (https://cybersecuritybase.mooc.fi/module-3.1)

The project contains a web app that has five different flaws that are in the list of top 10 web application security risks created by OWASP (https://owasp.org/Top10/)

## Instructions to run the project app

### 1. [Install Flask](http://flask.pocoo.org/docs/1.0/installation/)

Create a project directory:

```
mkdir project
cd project
```

And a virtual environment `demoenv` (not necessary but recommended):

```
python3 -m venv demoenv
```

On Windows:

```
py -3 -m venv demoenv
```

Activate the environment:

```
. demoenv/bin/activate
```

On Windows:

```
demoenv/Scripts/activate
```

Install Flask:

```
pip install Flask
```

### 2. Create the database

Clone the git repository and move to `project_files` directory

Run `create_db.py` file on the command line

In order to get the app working you must create the database first!

### 3. Run the application

Set the following environment variables:

Show flask which file to run:

```
export FLASK_APP=app.py
```

Enable development environment to activate interactive debugger and reloader:

```
export FLASK_ENV=development
```

Set the port in which to run the application, e.g.:

```
export FLASK_RUN_PORT=8000
```

On Windows command line, you can the environment variables with:

```
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_RUN_PORT=8000
```

And on Windows PowerShell:

```
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
$env:FLASK_RUN_PORT = "8000"
```

Run the app:

```
flask run
```

Go to `localhost:8000` in your browser to see the website.
