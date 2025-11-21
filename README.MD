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