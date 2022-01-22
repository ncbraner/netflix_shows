Thank you for taking the time to review this challenge. I wanted to take a minute and 
review the requirements and explain the app.

For using this app, I relied on the FastAPI docs to run the endpoints at /docs

To start, you will need to register yourself with the resgister route.
any name and password will do, there are no requirements to it other than
uniqueness between records

You can then click the authorize button on the top right of the screen this will authorize
you to the api.

We have two routes for getting content. First you will want to use the getcontent route. This provides you with a slimed down list of movies/shows by year.  it also gives you a id to use in the next route

The route getwholerecord will build out a entire record for you.  As you look at the code, you will see how we seperated the csv into different concerns

One of the requirements was to update records.  If we follow the updatetitlebyid route, you can see that you can update the title of a show by providing the shows id and the new title

The last route we have an aggregation on the release year. of the content based on the amount of records we search
for

I also decided to shoot for some extra points as well.

Unit Testing

* I did create one unit test for demonstration on testing. That test will test the user creation logic

* This can be ran with the test_user_service.py in the root directory

Authentication
* I built out the Authentication to only allow authenticated users to use the API


The following is a copy of the challenge letter for your reference.

Congratulations! We are excited to extend this assignment 
to you so that you can share your 
skills in a more tangible fashion. 
The python project is a time for you to display 
your concrete  development skills. This project 
is meant to be broad and open ended so that you 
are capable  of displaying your strengths. 
Please feel free to reach out if you have any 
questions. 

Please Timeline 

● Please commit a date when it will be complete.

● Maximum - 1 week Data 

● Pick a Data Source of your choice 

● Optional: Netflix shows: https://www.kaggle.com/shivamb/netflix-shows/data 

OBJECTIVES 

● Create API/API documentation.  
● Rows of data with search, filter, sorting, and pagination 

● Aggregated summary data 

● Modify data in the database 

● Use Flask/FastAPI Python for any back-end code if necessary  

● Push data into a database of your choice 

● Check in the code to your personal GitHub account.  

● Deploy the application in Google Cloud (Use free tier with new account setup) ● Preferably you can use managed services (App Engine, Cloud Run, CloudSQL,  etc.)  

EXTRA POINTS 

● Unit Testing implemented 

● Continuous Integration/Continuous Deployment features set up (CI/CD) ● E.g. CircleCI, Travis, GCP Cloud Build, Github Actions, etc. 

● Authentication implemented so that only authenticated users are capable of accessing  the API.
