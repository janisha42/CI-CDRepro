# CI-CDRepro
Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: 

* Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository. 
* Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
* Task 3: Write a Python Script to Check for New Commits
 Create a Python script to check for new commits using the GitHub API.
* Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.
* Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.
* Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 
_________________________________________________________________________________________________________
**Solution:** This repository collaborated with Poovarasan and Janisha
* Launch an Amazon EC2 instance with Ubuntu Os, a security group that allows all the IP addresses.
* After launching the instance connect with the root user then update the OS and install Nginx software with the below commands.
    sudo apt-get update
    sudo apt install nginx
* Ensure the nginx server is up and running.
* clon this repository.
  # index.html
   The HTML file contains the web page code.
  # check_commit1.py
    python program to fetch the latest sha for the commit using GitHub API and trigger the deploy.sh file to deploy the new changes.
  # deploy.sh
    shell script to update the local repo, copy the file to nginx folder, and then restart the nginx service.
  # script.sh
    Run a check_commit1.py Python file every minute to check new commits.
     * * * * * ./script.sh

* After cloning the repository and copying the file to nginx, check the status of nginx.
   systemctl start nginx
   systemctl enable nginx
   systemctl status nginx
* copy the files in the template folder and move them to /var/www/html
* restart nginx " systemctl restart nginx "
* check if the website did host on the public address for the server.
  http://public_address:80
  
Congrats!! you are done!!!
