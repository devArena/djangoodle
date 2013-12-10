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

Run it with:
    
    python manage.py runserver

Now you can open it on [http://localhost:8000/](http://localhost:8000/)
