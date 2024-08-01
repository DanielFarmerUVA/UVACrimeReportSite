# UVA Crime Report
## This project is the result of a semester long group assignment to create a whistleblower interface for UVA students for the Advanced Software Development course. We built this using Django, deployed it one heroku, and utilized Amazon for S3 storage. Beyond that we utilized google login and google maps for interactive location reporting of crimes. 

#### If you want to see the final project you can view the deployed version [here](https://project-a-03-uva-d449ae8204db.herokuapp.com/). 

**Steps to run it yourself (though the host login credentials and AWS credentials are missing you can still view most aspects of the site)**

1. Clone this repo.
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver
5. In your browser navigate to http://127.0.0.1:8000/anon-login

   *It is important to note that the API key for google maps is expired and the location feature for crime reports will no longer work, this is intentional as the class is over and we did not want to continue to pay.*
