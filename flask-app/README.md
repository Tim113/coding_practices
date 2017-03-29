# Flask_webapp_framework
Boiler plate for flask webapp: Cosmo framework (from Mercury)

To save people the time and sweat of working through how to set up a flask webapp, here is a minimal webapp.

See below for relevant instructions
To run the app:

1) create virtualenv

2) pip install requirements

3) create a postgresql db (called 'app_name' with credentials of 'RDS_')

3) `python initdb.py`

4) `python application` => 'http://0.0.0.0:5000/'

Login page => 'Hello World' :)

Have fun!

ps change 'app_name' to whatever your app is called, except for the following line in templates/base.html. Should've named it something different, only realised the clash half way through....

```<title>{# {% block page_title %}{{app_name}}{% endblock %} #}</title>```

### Tools and Technologies

#### Flask

Flask is a python micro web framework which also quick and easy web development Find more information [here](http://flask.pocoo.org/).

Flask Security for login management. (https://pythonhosted.org/Flask-Security/)

### Setup

#### Dependacies 

##### Python 3.4.3 

Download [here](https://www.python.org/downloads/release/python-343/).
Python 3.4+ comes with pip as part of the installation process so it is not required as a separate download

##### Virtualenv

virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

` $ pip install virtualenv `

For specific python version:
` virtualenv -p /usr/bin/<python version> virtualenv `

Please create and use a virtual environment for your development. This keeps the required libraries to a minimum and helps to identify version conflict issues. 

The best feature of virtualenv is that it allows the user to export the installed libraries inside the virtual environment to a text file 

`pip freeze > requirements.txt`

You can then use this file to install all the required dependencies into a fresh environment. This file should already exist in the repository

`pip install -r requirements.txt`

Find more information [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

#### Testing

To run the Flask app locally open a new terminal and navigate to the project folder.

Execute the command `python application.py`

The web app is now exposed at 'http://0.0.0.0:5000/' in your web browser.

#### Security

Under no circumstances should any passwords for any API's or databases be hard coded or added as a file to this repository. Even adding the details in one commit and then removing them in the next is bad for security because git keeps a history of file contents and so the credentials will still be in the git history. 

The best way to use required credentials in your code is to reference them from another file or set them as environmental variables. Use gitignore to make sure that these files are not added to file tracking. 

###### Database details

For storing the database details we will use environment variables referenced in the code see config.py. For local use either set your own global environment variables or use a script to assign and release in a virtual environment. You can find instructions on how to do this [here](http://stackoverflow.com/a/38645983). 

The environment variables you will need to set in your local are:

 * RDS_BD_TYPE
 * RDS_DB_NAME
 * RDS_USERNAME
 * RDS_HOSTNAME
 * RDS_PASSWORD
 * RDS_PORT

