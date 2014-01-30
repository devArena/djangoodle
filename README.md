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
    5. For every time you want to work on project you must activate virutalenv. For windows execute: 
        
        ```
        source Scripts/activate 
        ```

        and for linux: 

        ```
        source bin/activate** 
        ```

* Database migration
	1. First time only, execute: 

        ```
        python manage.py syncdb
        ```

	2. After every github pull (if new migrations exists): 

        ```
        python manage.py migrate djangoodle
        ```

    3. Run: 

        ```
        manage.py schemamigration djangooodle --auto
        ```

        (update the database schema and migrationhistory table to generation N+1.)


Run it with:
    
    python manage.py runserver

Now you can open it on [http://localhost:8000/](http://localhost:8000/)

TODO:
1. Edit participants.
2. Deleting of participants (from everyone for now).
3. IDs hashing for URL-s (for events).
4. Enhanching user experience for adding event items.
5. Deploying.
6. Integration with memcache and Celery
7. Event groups
8. Summary of choices for all event items
9. Admin and user links and interfaces
10. Add and edit event items by admin
11. Admin can send emails with user links after event creation
12. Admin can finish poll and finished poll has highlighted best event item
13. Participants can add email if they want to receive notifications about the event.
