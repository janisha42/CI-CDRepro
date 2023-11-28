# CI-CDRepro
Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: 

Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository. 
Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
Task 3: Write a Python Script to Check for New Commits
 Create a Python script to check for new commits using the GitHub API.
Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.
Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.
Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 
_________________________________________________________________________________________________________
**Solution:** This repository collaborated with Poovarasan and Janisha
* Launch a Amazon EC2 instance with Ubuntu Os, security group which allows all the IP address.
* After launch the instance connect with the root user then update the OS and install Nginx software with below commands.
    sudo apt-get update
    sudo apt install nginx
* Ensure the nginx server is up and running.
* clon this repository.
  # index.html
   Html file contains the web page code.
  # check_commit1.py
    python file which checks the new commit and trigger the deploy.sh file to deploy the new changes.
  # deploy.sh
    deploy.sh file which clone the repository again with changes, copy the html file to nginx server html part restart the server and make sure web page updated with latest change.
  # script.sh
    Run python file every minutu to check new commit.

* After clone the repository copying the file to nginx, check the status of nginx.
   systemctl start nginx
   systemctl enable nginx
   systemctl status nginx
* copy the files in the template folder and move them to /usr/local/nginx/html/ 
