# Instructions for Automated WhatsApp Message
Want to send automated Whatsapp message to your loved one continuously? You can customize the message and calling name as you like. If you input near about 40-50 calling name and message it would be impossible for the receiver to understand whether those messages are automated or not. 
Interested?? Follow the steps and be the most romantic person. 

#Process:
1.	Log in or Create an account in https://www.twilio.com/ 
2.	In Twilio go to: All Products and Services > Programmable Messaging > Try it Out > Try WhatsApp
3.	 Send that shown message from whatsapp to the shown number. Click “Next: Send a One-Way Message”
4.	Click on Appointment Reminders 
5.	Copy the whole “To and From whatsapp number” including “whatsapp:” 
6.	Select Python and mark “Show Auth Token”
7.	Copy “account_sid” and “auth_token” 

#Open any IDE (Ex- VS Code):
1.	Open terminal 
2.	Clone this project https://github.com/rakib-nitk/automated-whatsapp-message.git
3.	Install Twilio (pip install twilio)
4.	Note down the version of Twilio. 

#Open “autosms.py” with VS Code Editor:
1.	Add names 
2.	Add messages 
3.	You can also change the time schedule 
8.	Fill “account_sid” and “auth_token” 
4.	Add message for morning, afternoon and night.
5.	Fill the From and To phone number with the whatsapp number you copied before.

#Open “clock_1.py”:
1.	Change the sleep time as you like. Time should be in second. (Optional. default is 50 minutes)

#Open “requirements.txt”:
1.	If installed version of Twilio is not 6.49.0 then change the version. 
(you’ll get the version while installing Twilio)

#Heroku:
1.	 Log in or Create an account in Heroku
2.	Got to: New > Create New App > Give a name of your app> Create App
3.	Download and Install The Heroku CLI | Heroku Dev Center

#Run these commands on the terminal of VS Code  (all commands will be shown after clicking Create app):
1.	heroku login
2.	git init 
3.	heroku git:remote -a (name of your app)
4.	git add .
5.	git commit -m “Comment anything here”
6.	git push heroku master

#Go to Heroku website:
1. Click on resources. From Dynos run clock_1.py.
2. Settings > Reveal Config Vars. Add config vars- Key: TZ, Value: Asia/Dhaka (for Bangladesh, or change based on your country.) 

#You can also check this tutorial - https://youtu.be/pQeFxdT3FGY

Have fun, enjoy!!
