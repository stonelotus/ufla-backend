## Don't forget to fetch ! 
## Create branches for what you add
## Edit README for any changes in setup / how to run

# How to setup this : 

## Click emulator setup : 
Run "python -m venv env"
Add to .gitignore "env"

---

# How to run this : 
## Click register backend :
#### - This receives activities (e.g. clicks) from frontend and writes to DB -
Run "node app.js" in terminal.

## Click emulator backend
#### - This reads from DB and emulates activities (e.g. clicks) -
Go to "env/Scripts"
If using Powershell, run the "Activate.ps1" script
If using Windows, but another terminal, run the "activate.bat" script
If using Linux, run the "activate" script

<b>On first setup only</b> pip install selenium

To run the module, run "python clicker.py"


# TODO 
Don't forget to associate a specific ID to the clicker bot, so that when we test the app based on existent user flows, the DB doesn't register these as valid user behaviour as well.

