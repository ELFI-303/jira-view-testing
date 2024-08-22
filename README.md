# jira-view-testing
This program is a automated solution for testing random Jira issue tickets in order to verify if they are concording with the Jira server version. 
This program can be used to make easier and faster migrations from server to cloud.
The tool mentioned here is a script that will help the migration team test the visual comparing the server Jira environment and the test or cloud (production) environment.

To make this script work, you will need to have installed Docker and Quartz :

# Installation :

Docker Desktop
You can download Docker Desktop with this link :https://www.docker.com/products/docker-desktop/

XQuartz
You can download XQuartz with this link : https://github.com/XQuartz/XQuartz/releases/download/XQuartz-2.8.5/XQuartz-2.8.5.pkg 

:warning:  Be careful XQuartz will ask you to restart the computer after the installation so save your work !! :warning:

Once you downloaded and installed the two softwares we need to configure them so they are able to work together.

Launch XQuartz by going to :  Launchpad > Other > XQuartz 

Once XQuartz is running go to the Settings and then to Security and check “Allow connections from network clients” and then re-restart your laptop.

After this you can use the Terminal by going to :  Launchpad > Other > Terminal  and type these commands :

(If you haven’t already, download v0-0-2 DOCKER.zip and open the zip file, i expect your file to be downloaded in your /Downloads/ folder in this case, 

if you want to move the file somewhere else you will have to change the path when using the “cd” command)

 cd Downloads/test-view-compose 

 bash launch.sh 

This will start everything needed for the script to run, once every steps are done the terminal should return this:

Now if you refresh the Safari window that has been opened, you should be able to see this window :

Using the script :
First of all, XQuartz needs to be running at the same time, if not you will get an internal error.

The first question will be whether you want the script to compare with sandbox or cloud.

The second question will be the name of the project you want to test (write down the key of the project).

The third question will ask you the number of ticket you want to test during the execution.

And the last but not least the script will ask you what is the highest ticket of this project (the tickets will get a random number between 1 and the highest ticket number) so the ticket number is the highest ticket you want to tackle during this test.

Starting the app from docker : 
You will need to have XQuartz started to start the application container.


In order to start the view-testing-script go to  Actions  and press on the start button.

And then to use it, click on the hyper link  80:80  OR go to you browser and paste this url address in your search bar: http://localhost:80

 

