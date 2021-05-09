# Stutor-Tutor_Nearby
A django project created for finding the tutor near by your area. Project for FROSTHACK 2021.

## Theme 
* Education

## Problem Statement
Finding a good tutor can prove to be quite tricky, especially, if you are new in a city. When you are searching for a tutor you have to take into account such as the teacher’s subject he/she teaches, review about the tutor, fees etc. Sometimes you have to ask your friends about the best tutor in their area. Still don’t know if this will satisfy you or not. This is the social problem that we all generally faced 

## Proposed Solution
Finding the answer to the above problem can sometimes be stressful when you are not able to find a tutor at an affordable price and upto our mark. So we came up with the idea to create a webapp in which a tutor can register his/her details like what subjects they can teach, fees per subject, number of teachers in their center, etc. To do this task we require a database that stores all information of the tutor. This webapp filters the data on the basis of location nearby you. Our main aim is to make the app more compatible to use. So that any teacher or student can easily use 

## Tech Stack
Basically our whole application is made on Django, a python web Framework. Its model-template-view (MTV) architectural pattern. Since it is suitable for both frontend and backend. We choose this for our web application. Basically we use models to store data in SQL format. We create our own templates that use models to view all the content. It takes care of much of the hassle of Web development, so that we can focus on writing our app without needing to reinvent the wheel.

## Use Case and Future Scope
This project will be quite useful for those students who are unable to get quality education due to lack of finding good teachers. Many times we want to learn but due to unavailability of resources we couldn't do it. So, we will provide a platform where both students and tutors will meet their needs. 
Also in future we will try to implement digital live classes, where students can learn from their tutor online.


## Available Scripts

1. First fork this repo and then Clone it
2. Run `cd sms` - to move into the directory 
3. Install virtualenv using command - `pip install virtualenv`. In linux - `sudo pip3 install virtualenv`.
3. Now activate the virtual environment using command - `virtualenv env`
4. Now activate the virtual env using command - `.\env\Scripts\activate` . This will activate the virtual environment. For linux and Mac try - `source env/bin/activate`
5. Install all requirements by - `pip install -r requirements.txt`. In linux - `pip3 install -r requirements.txt`
6. Now to migrate the models run - `python manage.py migrate`. In linux - `python3 manage.py migrate`
7. Now to activate the localhost server run - `python manage.py runserver`. In linux - `python3 manage.py runserver`<br />
<pre>
	Runs the app in the development mode.<br />
	Open (http://localhost:8000) to view it in the browser.
</pre>