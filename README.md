
# TryHackMe Readme Card

This is a simple unofficial tryhackme card to be used on Readme profile or any markdown file. It shows basic infos like global rank, badge and rooms completed. It uses your profile badge id to dynamically update the infos.

Future improvements:

 - Colors dynamically changed based on title or rank
 - Differents themes
 - Actually show badges(?)
 
 *Note: This was my first time building something with node/js/heroku, so any tip, fix or improvement will be very welcome.*
 ## How to deploy your own instance on Heroku

After clone the repository, we should initiate the manager

    npm init -y
Then, to install the necessary packages

    npm i express xml
  
To deploy the app in Heroku we should install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
After that, login on your heroku account

    heroku login
Then, create your instance on heroku (you can change the name later):

    heroku create
Now, to install the right builpacks

    heroku buildpacks:add --index 1 heroku/nodejs && heroku buildpacks:add --index 2 heroku/python
Finally, you can push the files to the heroku

    git push heroku main
You can test the app using

    heroku open card?id=1234

To use this on your readme you should use as:

    [![TryHackMe](http://YOUR-INSTANCE-NAME.herokuapp.com/card?id=YOUR_BADGE_ID)](https://github.com/FabioSLeao/tryhackme-card)

Changing the upper case text.


