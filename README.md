Djangoodle
==========

Event:
* Name
* Description
* Time of creation
* Email of creator

Event Items:
* Type: DateTime or Categorical (or both)

Participants (tied to specific events)
* Event
* Name
* Array of event items

New event
Add event items
Create URL to event with hash:
* Admin link:
    * edit event properties
    * change event items
    * close event
    * send emails to potential participants
    * remove participants
* Public link:
    * Add participant to event
    * Choose event items
Show current results each event item and sorted list of current best event items


Pre-setup and daily usage:

* pip
    1. pip install -r requirements.txt


* Virtualenv
	0. Install virtualenv: pip install virtualenv
	1. Create folder "ProjectXY" for virtual environment and gihub project
	2. Make "ProjectXY" root folder.
	3. Execute in shell: virtual . 
	4. Execute in shell: git clone "link sa github-a"
    5. For every time you want to work on project you must activate virutalenv. For windows execute: source Scripts/activate and for linux: source bin/activate**. 
 

* Database migration
	1. First time only, execute: python manage.py syncdb
	2. After every github pull (if new migrations exists): python manage.py migrate djangoodle


Run it with:
    
    python manage.py runserver

Now you can open it on [http://localhost:8000/](http://localhost:8000/)

