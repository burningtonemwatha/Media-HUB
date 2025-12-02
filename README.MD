Media HUB

media sharing platform that has role based access

teacher role - manage assigned student content , media uploads
student role - share media uploads
admin role - overseeing all content and managing the platform

Tools of use
django
python libraries (ready made snippets for a specific job)
pillow : media transactions in python frameworks (absolute media url , )
cloudinary : media storage and also url access generation (url -> save to database for an upload)
python-decouple : media tasks
Apps in projects
accounts : authentication and authorization (signups, login , forgot password)
media_assets : uploads tasks , displays , updates
steps
install the libraries : pip install libraryname pip install -r requirements.txt
create our apps
configure our project settings
register our apps
register cloudinary (give the cloudinary configs)
register a custom authentication process
emails registry
Authentication and Authorization (accounts app)
Authentication = identity identification, who are you ? Authorization = access priviledges - role based authorization , token based authorization

Create our custom user model - models.py
Extend the integrated form captures - forms.py
Create the views action for registration and login , logout and profile view , custompasswordresetview , custompasswordresetconfirmview - views.py
Register the views actions as URL route - urls.py
Register the models for admin to use and manage content on - admin.py
Register the apps url to the projects urls = project/urls.py
Create the templates
create a templates folder - within the app
create a global templates folder - register it's configuration in the settings.py file
Make databases migrations and then populate the templates python manage.py makemigrations python manage.py migrate
Template creation
Configuration level file : base.html

Defining your blocks : title , extra_css , content (most important) , footer, extra_js
Linking to global stylesheet / style lib. (bootstrap)
Link to global js files
Create the other pages by simplying extending (extends) the configs done on 1. Populate what is dynamic using block.

MVT - Model Views Templates
Media Asset app views
'''

Dashboard view : this allows my user to see uploaded items set as public
My media view : this allows users to see only their uploads
Upload media view : this allows user to upload media
Edit media view : this allows user to edit uploaded media
Delete media view : this allows user to delete their uploaded media
Media Detail view : this allows users to see all details for a media item '''
Configuring our environmental variables
Create a .env file for development purposes - store your info as variable references
Create a .gitignore file for github push purposes - include .env as one of the ignored files This abstracts sensitive info from the main application code
MPESA INTEGRATION
Created a separate app that will contain our mpesa integration procedures
Create a model , transactions model - this will update made on our app
Settings.py project - configure the needed environmental credentials
Populate views and urls to map to the views and the respective templates
MPESA + MEDIAHUB app connection
Media Details screen my user will see a donate to me button
Donate to me -> redirected to the payment screen
Pay -> utilize the views function for proper redirect