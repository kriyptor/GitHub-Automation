# GitHub-Automation
This is Repo of github automation.

# Things You Need For this automation
<strong>1. Selenium</strong><br>
<strong>2. Chrome webdriver</strong><br>

# How To Get Selenium
Simply just do "pip install selenium" in your commande line prompt(make sure you have installed the python in your computer)

# How To Get Chrome Webdriver
<h3>=>To get chrome web driver you have to install chocolatey package manager</h3>

<h5>=>Steps to Install chocolatey/choco on Windows 10</h5>
<li>Click Start and type<strong>powershell</strong></li>

<li>Right-click Windows Powershell and choose<strong>Run as Administrator</strong> (make sure it is on administration mode)</li>

<li>Paste the following link command into Powershell and press enter:<strong>Set-ExecutionPolicy Bypass -Scope Process -Force; `iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))</strong></li>

<li>Answer Yes when prompted</li>

<li>Close and re-open an elevated PowerShell window to start using choco</li>
</ol>

<h3>=>Now we are ready to install chrome driver</h3>
<ol>
<li>open your commande prompt and <strong>run it as administration</strong></li>

<li>write<strong>choco install chromedrive r</strong> and press enter</li>

<li>It will get download</li>

<li>How ever if you have any problem you can go to this link for help: <link>https://chocolatey.org/docs/installation#more-install-options</link></li>
</ol>

# And you are good to go!!!! 

Make sure you put this script file in very conveniant drictory of system So, you dont have to write long cd commands to choose the directory.<br>
Go to your script directory location in cmd and just write this command <strong>python.exe Github-auto.py</strong> and hit the enter button.<br>
<strong>BOOM!! You have just created a new repo with just sinle command line!!</strong><br>
  
 # Happy Automation!!!!! :)
