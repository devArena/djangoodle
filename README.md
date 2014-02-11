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


* Virtualenv
	0. Install virtualenv: 

        ```
        pip install virtualenv
	    ```

    1. Create folder "ProjectXY" for virtual environment and gihub project
	2. Make "ProjectXY" root folder.
	3. Execute in shell: 

        ```
        virtual . 
        ```
        On Ubuntu do the following:
        -----------------------------------
        Now using pip install :
        ```
	sudo pip install virtualenv virtualenvwrapper
	```

	Creating directory for our virtual environments

	```
	mkdir ~/.virtualenvs
	```

	Configuring bash to work with a virtualenvwrapper (add these lines to the end of ~/.bashrc )
	```
	export WORKON_HOME=$HOME/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh
	export PIP_VIRTUALENV_BASE=$WORKON_HOME
	```

	Done. You can work within virtual environments from now on 
	```
	mkvirtualenv myfirstenv
	```
	-----------------------------------------

	4. Execute in shell: 

        ```
        git clone "link sa github-a"
        ```* pip
    	
	 ```
    	pip install -r requirements.txt
        

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
