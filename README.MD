*Media HUB*
-------
Media sharing platform that has role based access
-------
*Roles allowed*

Teacher role - manage assigned student content , media uploads
Student role - share media uploads
Admin role - overseeing all content and managing the platform
--------
*Tools of use*

1. Django
2. Python libraries (ready made snippets for a specific job)
3. Pillow : media transactions in python frameworks (absolute media url , )
4. Cloudinary : media storage and also url access generation (url -> save to database for an upload)
5. Python-decouple : media tasks
------
*Apps in projects*

1. Accounts : authentication and authorization (signups, login , forgot password)
2. Media_assets : uploads tasks , displays , updates
------
*Steps*

1. Install the libraries : pip install libraryname pip install -r requirements.txt
2. Create our apps
3. Configure our project settings
4. Register our apps
5. Register cloudinary (give the cloudinary configs)
6. Register a custom authentication process
7. Emails registry
- Authentication and Authorization (accounts app)
-  Authentication = identity identification, who are you ? Authorization = access priviledges - role based authorization , token based authorization
8. Create our custom user model - models.py
9. Extend the integrated form captures - forms.py
10. Create the views action for registration and login , logout and profile view , custompasswordresetview , custompasswordresetconfirmview - views.py
11. Register the views actions as URL route - urls.py
12. Register the models for admin to use and manage content on - admin.py
