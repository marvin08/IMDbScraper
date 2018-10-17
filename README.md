# IMDb Scraper

This is a python script which scrapes some useful information from the IMDb website and sends an e-mail to the user regarding the updates of the TV series which they asked for.

## Essential tools needed to run this script

- Make sure you have installed python3.
	
  - For Ubuntu/Debian based package managers:
   ```
   sudo apt-get update
   sudo apt-get install python3
   ```

  - For Fedora/CentOS/RPM based package managers:
   ```
   sudo -i
   yum install python3
   exit
   ```

  - For Arch based package managers:
   ```
   sudo pacman -S python-cairosvg
   sudo pacman -S python-lxml
   ```

- Make sure you have installed MySQL.
          
  - For Ubuntu users:
   ```
   sudo apt-get update
   sudo apt-get install mysql-server
   ```
 
- Use the command - `sudo pip3 install <package/module>`, for example, `sudo pip3 install re`, and ensure that you have installed the following packages/modules:
        
  - `re`
  - `mysql`
  - `mechanicalsoup`
  - `bs4`
  - `datetime`
  - `smtplib`
  - `email`
  - `passlib` 

NOTE:- Some of the above packages/modules might already be there in your system, so no need of installing them again. For example, smtp, email, etc. packages/modules are generally there and you don't need to install them.

## Some important points to consider before running the script

- **Please enter your username and password used in your MySQL server in the script. Replace `yourUsername` by your username and `yourPassword` by your password on lines 22 and 28 in the script. (NOTE:- Username is "root" in most cases.)**

- I have used `127.0.0.1` as host name for establishing MySQL connection. You may also use `localhost` but sometimes it gives an error if socket is not configured properly. 


## Running the script

- Clone the repository and then change the directory to the directory containing the script and then run it in *Terminal* (For Linux/MacOS users) or *Command Prompt*. (For Windows users.)

  - For Linux/MacOS users:
   ```
   python3 IMDbScraper.py
   ```	
       
  - For Windows users: (Make sure your PATH environment variable contains the python directory.)
   ```
   IMDbScraper.py
   ```

- After running the script, enter your e-mail address on which you want to get updates related to the TV series. Then, enter the TV series whose updates you want in your e-mail, in a comma separated way.

- This script takes input for multiple users, so, at any time when you want to exit, just interrupt the script. For example, Ubuntu users can use `CTRL + Z` command to stop/terminate the script in their terminal.










														 
