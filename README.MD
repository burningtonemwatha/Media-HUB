### Media HUB

media sharing platform that has role based access

1. teacher role - manage assigned student content , media uploads
2. student role - share media uploads
3. admin role - overseeing all content and managing the platform

---
### Tools of use

1. django
2. python libraries (ready made snippets for a specific job)
   -pillow : media transactions in python frameworks (absolute   media url , )
   -cloudinary : media storage and also url access generation (url -> save to database for an upload)
   -python-decouple : media tasks

---
### Apps in projects

1. accounts : authentication and authorization (signups, login , forgot password)
2. media_assets : uploads tasks , displays , updates

---
### Steps

1. install the libraries : pip install libraryname pip install -r requirements.txt
2. create our apps
3. configure our project settings
   -register our apps
   -register cloudinary (give the cloudinary configs)
   -register a custom authentication process
   -emails registry

---
### Authentication and Authorization (accounts app)

Authentication = identity identification, who are you ? Authorization = access priviledges - role based authorization , token based authorization

1. Create our custom user model - models.py
2. Extend the integrated form captures - forms.py
3. Create the views action for registration and login , logout and profile view , custompasswordresetview , custompasswordresetconfirmview - views.py
4. Register the views actions as URL route - urls.py
5. Register the models for admin to use and manage content on - admin.py
6. Register the apps url to the projects urls = project/urls.py
7. Create the templates
   -create a templates folder - within the app
   -create a global templates folder - register it's configuration in the settings.py file
8. Make databases migrations and then populate the templates python manage.py makemigrations python manage.py migrate

---
### Template creation

1. Configuration level file : base.html

   -Defining your blocks : title , extra_css , content (most important) , footer, extra_js
   -Linking to global stylesheet / style lib. (bootstrap)
   -Link to global js files
2. Create the other pages by simplying extending (extends) the configs done on 1. Populate what is dynamic using block.

---
### MVT - Model Views Templates

Media Asset app views
'''

1. Dashboard view : this allows my user to see uploaded items set as public
2. My media view : this allows users to see only their uploads
3. Upload media view : this allows user to upload media
4. Edit media view : this allows user to edit uploaded media
5. Delete media view : this allows user to delete their uploaded media
6. Media Detail view : this allows users to see all details for a media item '''

---
### Configuring our environmental variables

1. Create a .env file for development purposes - store your info as variable references
2. Create a .gitignore file for github push purposes - include .env as one of the ignored files This abstracts sensitive info from the main application code

---
### MPESA INTEGRATION

1. Created a separate app that will contain our mpesa integration procedures
2. Create a model , transactions model - this will update made on our app
3. Settings.py project - configure the needed environmental credentials
4. Populate views and urls to map to the views and the respective templates

---
### MPESA + MEDIAHUB app connection

-Media Details screen my user will see a donate to me button
-Donate to me -> redirected to the payment screen
-Pay -> utilize the views function for proper redirect

---
### Changes/ Updates

1. Settings.py - allowed hosts and csrf_domains
2. Urls.py/ project - adding the namespace for the mpesa app
3. Templates
   -media_assets - media_detail.html - added a button to mimic a checkout
   -mediampesa - index.html and waiting.html
4. Mediampesa app
   -urls.py
   -views.py - namespace addition to routes
5. On daraja mpesa console add lipa na mpesa express as a product to your app
6. Populate the .env variables needed check .env.example file
7. NGROK service for development purposes over a https network : https://.......................

---
### To use NGROK

1. launch your development server
2. open a new terminal / command prompt
3. ngrok http server:port