# Cookbook Milestone Project

## Mongo db, Flask, Python, Data centric development 

### Name

Belly convent ,the project name was chosen because the user as he enterese the page will be converted, for the while he visits the page, to a world of superiour cuisine aplied in various locations all over the world. Sometime will be the case that is a high class cuisine, other that will be a very famour recipe that represents so well a type of cuisine and it tastes so well that gain its own place among the Belly cuisine.

### Features

#### Working Features

This is a web application which allows users to store and easily access cooking recipes. It is a full stack web application (**_frontend and backend_**) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted and available on Heroku platform as a service. Here users can :

1. **Create** or ad a recipe to the Mongo Db database with the inclusion of different fields, such as time of preparation, food description, gluten free friendly, etc.
2. **Read** from the data base the files there founded, and retrieve them to the app in a variaty of details. With this I mean that the user can see a list of the recipes, ##_sorted by pagination yet to be implemented_**........, or can select each recipe in a unique page and inspect it with all the specifications available. Also is retrived a list with the types of cuisines **_authors, predominant groups, upvotes_**
3. **Update** the recipes cuisines, and their properties in a easy quick way by the users needs and likes
4. **Delete** a recipe or a cuisine type,**_author, group,etc_.......** , alway after a modal security question that informs the user that he is going to delete forever the file.

5. **Dashboard** displays a graphic relation between cooking time, preparation tyme, cuisine name, author name and food groups
6. **Search and sort** function allow the user to search by word among the database, and the sort function orders the list under different criteria such as author, predominant group, etc 

#### Features Left to Implement

1. Upvotes
2. Login
3. Pagination
4. Fix Search functionality
5. Add author, food group in cathegories, etc
6. Images upload available
7. Export to PDF, download a recipe.

#### User Stories

* The first thing that the user will see is the recipes list containing  the recipe name and their food group shown in a  acordeon that if clicked will display a small intro acout the recipe. Before each recipe name there are two option, one is for editing the recipe and one is for viewing the full recipe. Above the recipe list the page displays a menu  with the name of the restaurant. And options for Recipes, add recipe, cuisine and Graphics.


* The sorting and search function will search by word among the recipes and sort the recipes in different ways, and criterium
* The edit button will take you to edit the recipe as the user desires. Selecting cusine, author, predominant group of food, food course, allergens like Gluten free and celiacs. Also one ca select  in a range selector the preparation and the cooking time set by minutes, the foor ingredients, description, contect( that is small introduction) and finally the name.
* The arrow next to the Edit recipe button will display fully the recipe with all the fiels(food ingredients, author name, gluten free, etc) available and with an image assigend by _html_. There is also a delete button that, when clicked will guide you to a modal dialogue that will ensure that the user is aware of the complet deletion of the recipe.

_pagination_ ...........

* Add recipe. Here the user will be able to ad a recipe.

* Cuisine_author_, _predominant.........     etc_  a page where one can see all the cuisine list, edit them and delete them as well

* Graphic a serie of five graphichs displayed with the help of d3, crossfilter that help the user see in an easy and graphic way the relation bethween for instance time of cooking and cuisine type. 

### Technologies Used

* **_HTML, CSS, JaveScript_** with the help of jQuery fot the front end code

* **_Materialize, Front awsome_** for the display, templates and icons

* **_Python, Flask, Mongo Db_** worked to connect the backend database to the frontend

* **_Heroku_**  Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

* **_TravisCl_** used to test the code














### Challenges

* Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store. I saw that a good organized database gives powers to a novel programmer like me

* Managing routes and URL's with Flask was also very interesting and I learned a powerful feature from reading the documentation around Flask and MongoDB. This feature gives speed and facilitate the work of a programmer.

* Implementing, or trying to extra features, such as pagination, user login that have taught me a parallel way of learning out of the course box, that I think I will be using in all my future carrer.





 
