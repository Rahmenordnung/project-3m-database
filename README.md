# Bely Convent 

Tudor George Pascu  /student at Code Institute in Dublin, Ireland, 2019

Third Milestone project, Flask , external Databases, Python

## <a name="Name"></a> Name  ##

Belly convent, the project name was chosen because the user as he enters the page will be converted, for a litlle while , to a world of superiour cuisine aplied in various locations all over the world. Sometime will be the case that is a high class cuisine, other that will be a very famour recipe that represents so well a type of cuisine and it tastes so well that gain its own place among the Belly cuisine.


## Sumary
* [Name](#Name)
* [User Stories](#User_Stories)
* [Features](#Features)
    - [Existing Features](#Existing_Features)
         - [Belly Convent](#Belly_Convent)
         - [Add Recipe](#Add_Recipe)
         - [Graphics](#Graphics)
         - [Preferences](#Preferences)
             - [Cuisines](#Cuisines)
             - [Chefs](#Chefs)
             - [Courses](#Courses)
             - [Food group](#Food_group)
     - [Features Left to Implement](#Features_Left_to_Implement)
* [Database](#Database) 
* [Functionality](#Functionality)
* [Technologies Used](#Technologies_Used)
* [Testing](#Testing)
* * [Responsive Testing](#Responsive_Testing)
* [Getting started](#Getting_started)
* [Deployment](#Deployment)
* [Demo](#Demo)
* [Media](#Media)
* [Challenges](#Challenges)

----------------------

## <a name="User_Stories"></a> User Stories ##

For example:

* A mother staying at home bored, because she doesn't know how to get a superior recipes page, or very popular ones. Because she whants to impress her friends and get some good impressions and somehow climb up in the social scale.

* Anybody interrested in improving their cooking level, chefs, students, and they need a fast and quick selection of recipes sorted in different ways.

* A person that looks for some good ranked recipes but needs some specifications about the most comun allergens because of their health contions.

---------------------
## <a name="Features"></a> Features ##

### <a name=" Existing_Features"></a>Existing Features ###

* __Navbar__ - Consists of the __Bely Convent__ logo which returns the user to the Home page of the application. There is also links to the **Recipes**, **Add (recipes)**, **Graphs**, **Preferences** that contains a _dropdown_ with **Cuisine**, **Chefs**, **Courses**, **Food Group**. The navbar will appear on all pages.

#### <a name="Belly_Convent"></a>Belly Convent  ####

* Or Recipes is a __list of recipes__ that at the same time is the Home page. This consist of the recipes list containing  the recipe name and their food group shown in a __acordeon__ that if *clicked* will display a small intro acout the recipe. Before each recipe name there are __two options__, one is for **editing** the recipe and one is for **viewing the full recipe**, preceded by a **glyphicon**.
    * The __editing button__ edites the recipe in all the fields that are available in the database.
    * The __red arrow__ redirects the user to the recipe __full detail__, differentiated from the small preview present in the accordeon. This full detailed page consits of all the data present in the database, image, name, prep-time, etc
* __Sorting dropdown__ above the list, delievers different parameters to order the recipe list.
* __The Search box__ offers the user the function of searching by words in the data-base
* __Pagination__ is present in the Recipe list and in the searching results if required by the results number
* __Add Recipe__ is a green button that redirects the user to the add recipe page
* __Footer__ contains a copyright text, a link to a restaurant with the same name, and social media icons to different cooking pages.

#### <a name="Add_Recipe"></a>__Add Recipe__ ####

 Contains a formular that takes data in different fiels and saves it into the Mongo Db database. This Fields are: 
* Cuisine Category
* Chef Selection
* Course Selection
* Food group
* Food facts
* Food name
* Food description
* Celiacs (checkbox)
* Gluten free (checkbox)
* Cooking Time(slidebar)
* Preparation time(slidebar)
* Recipe image Url

#### <a name="Graphics"></a>__Graphics__ ####
Five diagrams that reflect in a statistical manner different relations between different variables among the recipes database. That allows the user to easily diferenciate between authors and type of cuisine, for instance and many other different relationships. They are realized with dc.js, crossfilter, queue, and d3.js. 

In this formular I didn't added the upvotes function, that is only available in the __recipes detail view__

## <a name="Preferences"></a> Preferences ##

#### <a name="Cuisines"></a>__Cuisines__ ####

Presents a list of the cuisines types and also it integrates two small buttons _edit_ and _delete_. But this time the buttons edit / delete the cuisine type and not the recipe.

#### <a name="Chefs"></a> __Chefs__ ####

Presents a list of the chefs and also it integrates the posibility of editing, deleting and adding new ones. 

#### <a name="Courses"></a>__Courses__ ####

Our food is sorted by different courses presented in a list that contans the possibillity of modifing the register as the user decides.

#### <a name="Food_group"></a>__Food Group__ ####

 A list of the most important food group present in the daily nutrition. It integrates as in the rest of prefences the posibility of editing, deleting and adding new ones.

*  Above the recipe list the page displays a menu  with the name of the restaurant. And options for Recipes, add recipe, cuisine and Graphics.
* The sorting and search function will search by word among the recipes and sort the recipes in different ways, and criterium
* The edit button will take you to edit the recipe as the user desires. Selecting cusine, author, predominant group of food, food course, allergens like Gluten free and celiacs. Also one ca select  in a range selector the preparation and the cooking time set by minutes, the foor ingredients, description, contect( that is small introduction) and finally the name.
* The arrow next to the Edit recipe button will display fully the recipe with all the fiels(food ingredients, author name, gluten free, etc) available and with an image assigend by _html_. There is also a delete button that, when clicked will guide you to a modal dialogue that will ensure that the user is aware of the complet deletion of the recipe.
* 
_pagination_ The pagination is allowing the user to move easily and quick through the list of recipes. It was implemented 

* Add recipe. Here the user will be able to ad a recipe.

* Cuisine_author_, _predominant.........     etc_  a page where one can see all the cuisine list, edit them and delete them as well

* Graphic a serie of five graphichs displayed with the help of d3, crossfilter that help the user see in an easy and graphic way the relation bethween for instance time of cooking and cuisine type. 

**********************
### <a name="Features_Left_to_Implement"></a>Features Left to Implement ###

1. Export to PDF, download a recipe.
2. Expand the recipes with videos, more alergens and probably the option of buying a cooking book.
2. Improve the recipes presentation.
3. Improve the search function.
4. Asign each recipe to an user and have a record about that

**********************
## <a name="Database"></a>Database ##

[MongoDB](https://www.mongodb.com/) is a document-oriented NoSQL database written in the C ++ programming language. Because the database is document-oriented, it can manage collections of JSON-like documents.

## <a name="Functionality"></a>Functionality ##

This is a web application which allows users to store and easily access cooking recipes. It is a full stack web application (**_frontend and backend_**) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted and available on Heroku platform as a service. Here users can :

1. **Create** or ad a recipe to the Mongo Db database with the inclusion of different fields, such as time of preparation, food description, gluten free friendly, etc.
2. **Read** from the data base the files there founded, and retrieve them to the app in a variaty of details. With this I mean that the user can see a list of the recipes, sorted by _pagination_, or can select each recipe in a unique page and inspect it with all the specifications available. Also is retrived a list with the types of cuisines **_authors, predominant groups, upvotes_**
3. **Update** the recipes cuisines, and their properties in a easy quick way by the users needs and likes
4. **Delete** a recipe or a cuisine type,**_author, group,etc_.......** , alway after a modal security question that informs the user that he is going to delete forever the file.

5. **Dashboard** displays a graphic relation between cooking time, preparation tyme, cuisine name, author name and food groups
6. **Search and sort** function allow the user to search by word among the database, and the sort function orders the list under different criteria such as author, predominant group, etc.
7. Also contains a dc.js **Interactive Graphic** made with java, dc.js... 
8. Some **modal dialogues** used to advert the user that is going to delete a record, 
9. **Pagination** that allows the user to move through the web page. 
10. For the images added in the data base I used a simple url input as Mongo dosn´t allow storring of image file as so.
11. In addition I tried to implement a simple __log in__ function that it works .
 
***********************

## <a name="Technologies_Used"></a>Technologies Used ####

* **_HTML, CSS, JaveScript_** with the help of jQuery fot the front end code

* **_Materialize, Front awsome_** for the display, templates and icons

* __Python__ This project uses Python, for general-purpose programming and used to write the logic of this game, which is included within .py files
 
*  **_Flask_** worked to connect the backend database to the frontend

* **_Mongo Db_** a not SQl database non-relational approach. These datastores do not require fixed table schemas and try to avoid joins.

* **_Heroku_**  Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

* **_TravisCl_** continuous integration service used to build and test software projects hosted at GitHub.

* **_Flask_testing_** used to test framework functionality and its coninuous integration to Flask app and database (SQL or NON SQL)

* **_Unittest_** was used to build the testing framework.

* **__Werkzeug__** Werkzeug is a comprehensive WSGI web application library.I used to hash and encript the users passwords.

*********************

### <a name="Testing"></a>Testing ##

- The app was tested on Mobile, all the mobile, tablet, laptop, desktop etc,(all the deviced served in the Chrome developer tools) and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. There were many issues founded and the most critical for me was in the search function and in connection that with the main app and creation of sessions.

- The CRUD functionality has been test in relation with the database,to see if they comunicate and the records from the database are send, updated, deleted, etc with help of GET , POST methods

- The login/logout functuanality works by creating a new record in the Users collection from the database and that the pashword is hashed correctly thanks to __Flask and Werkzeug__ tools.

- The Search input searchs among the recipes by words in the available records.

- The pagination updates withing the count of the recipes available in the database

### <a name="Responsive_Testing"></a>Responsive Testing ##

**********************************
## <a name="Getting_started"></a>Getting started ## 
1. Clone the repository and cd into the project directory.
2. Ensure that you have Python 3 and MongoDB_URL(URI) saved in an envoirment variable and your credentials are introduced in the URI.  
3. Create a virtual environment and activate it.
4. Install dependencies: pip install -r requirements.txt.

## <a name="Deployment"></a> Deployment ##

Create Heroku App, after having registered in Heroku. In my case I am using a non Sql database that can´t be selected in Heroku, it needs only to be added to the settings.
In the CLI toolbelt :
*  __login to heroku (Heroku login)__ 
*  __git init__
* __connect git to heroku (heroku git remote -a )__ 
*  __git add .__
*  __git commit -m ""__
*  Before pushing all the changes to git and Heroku there are two requirements
*    1--requirements.txt create file by comand: __(sudo) pip3 freeze --local requirements.txt__  (lists all the dependecies needed to run the app)
*    2--Procfile create file: __echo web: python app.py > Procfile__                             (shows heroku which is the app that is used to run correctly the programm)
*  __git push heroku master__
*  __heroku ps:scale web=1__    (will scale your app to one running dyno)

In heroku app settings set the config vars to add __DATABASE_URI__, __IP__ and __PORT__. It is very important in the case of using an external database to configure the database Url or in my case database Uri.

## <a name="Demo"></a>Demo
A demo of this web application is available [here](https://bely-convent.herokuapp.com/get_tasks).

************

## <a name="Media"></a>Media ##


**********

### <a name="Challenges"></a>Challenges ##

* Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store. I saw that a good organized database gives powers to a novel programmer like me.

* Managing routes and URL's with Flask was also very interesting and I learned a powerful feature from reading the documentation around Flask and MongoDB. This feature gives speed and facilitate the work of a programmer.

* Implementing, or trying to extra features, such as pagination, user login that have taught me a parallel way of learning out of the course box, that I think I will be using in all my future carrer.


##____a-jjj___##


 
