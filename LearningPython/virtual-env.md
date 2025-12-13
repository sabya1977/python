How to create and use virtual environment in python
🔹Step 1:: 
    1. mkdir <project name>
    2. cd <project folder>

🔹Step 2:
    1. Create virtual envirornment using python -m venv <name of the env>
    2. For example, if you want to make a venv with python 3.12 then 
       C:\Users\sabya\AppData\Local\Programs\Python\Python312\python -m venv <name of the env>
    3. This will create a project environment with Lib, Scripts folder inside your   virtual env. folder.

🔹Step 3: Activate the environment
    1. Powershell - run <virtual env folder>\Scripts\Activate.ps1 
    2. For powershell, this command will automatically create a powershell
       function called deactivate. Get-Command deactivate
    2. Command prompt - run <virtual env folder>\Scripts\activate.bat 

🔹Step 4: Install required python package
    1. pip install numpy
    2. check if it's installed in your virtual env. or not using 
    pip show numpy. 
    3. If it shows Lib/site-packages of your virtual env. then it's installed for your virtual env. (C:\Users\sabya\gitrepos\python\venv-project\venv3.12\Lib\site-packages). 

🔹Step 5: Decactivate virtual env.
    1. deactivate for powecommand prompt rshell or <virtual env folder>\Scripts\deactivate.bat for command prompt.
    2. For powershell, deactivate


