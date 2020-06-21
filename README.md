# GitHub-Automation
This is Repo of github automation.

# Things You Need For this automation
<strong>1. Selenium
2. Chrome webdriver</strong>

# How To Get Selenium
Simply just do "pip install selenium" in your commande line prompt(make sure you have installed the python in your computer)

# How To Get Chrome Webdriver
<h3>=>To get chrome web driver you have to install chocolatey package manager</h3>
<h5>=>Steps to Install chocolatey/choco on Windows 10</h5>
1. Click Start and type <strong>“powershell“</strong>
2. Right-click Windows Powershell and choose <strong>“Run as Administrator“</strong>(make sure it is on administration mode)
3. Paste the following command into Powershell and press enter.
<strong>Set-ExecutionPolicy Bypass -Scope Process -Force; `
  iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))</strong>
4. Answer Yes when prompted
5. Close and reopen an elevated PowerShell window to start using choco
<hr>
<h3>=>Now we are ready to install chrome driver</h3>
1. open your commande prompt and <strong>run it as administration</strong>
2. write<strong>choco install chromedrive r</strong> and press enter
3. It will get download.
How ever if you have any problem you can go to this link for help: <link>https://chocolatey.org/docs/installation#more-install-options</link>
<hr>

# And you are good to go!!!! 
<hr>
Make sure you put this script file in very conveniant drictory of system So, you dont have to write long cd commands to choose the directory.
Go to your script directory location in cmd and just write this command<strong>python.exe Github-auto.py</strong> and hit the enter button.
<strong>Boom the magic will happen!!</strong>
  
