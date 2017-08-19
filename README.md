# weatherapi
API to know the current temp in a certain city and display it in google maps


Settings
--------------

MAPS_API_ID: Generate an API KEY in https://developers.google.com/maps/documentation/javascript/get-api-key?hl=ES&authuser=1#key and set the value in nearshore/consumer/consumer/settings.py


Quick start
------------------------------------------

Move to repository's root directory

    $ pip install -r consumer/requirements.txt

Starts first the API

    $ python weatherapi/manage.py 8002

Then initialize the consumer

    $ python consumer/manage.py 
    

