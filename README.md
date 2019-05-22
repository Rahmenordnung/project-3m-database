# Cookbook Milestone Project (Tudor George Pascu)

## Mongo db, Flask, Python, Data centric development 

### Name

Belly convent, the project name was chosen because the user as he enters the page will be converted, for the while he visits the page, to a world of superiour cuisine aplied in various locations all over the world. Sometime will be the case that is a high class cuisine, other that will be a very famour recipe that represents so well a type of cuisine and it tastes so well that gain its own place among the Belly cuisine.

#### User Stories

* A mother staying at home bored, because she doesn't know how to get a superior recipes page, or very popular ones. Because she whants to impress her friends and get some good impressions and somehow climb up in the social scale.

* Anybody interrested in improving their cooking level, chefs, students, and they need a fast and quick selection of recipes sorted in different ways.

* A person that looks for some good ranked recipes but needs some specifications about some of the most comun allergens because of their health contions.



### Features

### Existing Features

* Navbar - Consists of the Bely Convent logo which returns the user to the "Home" page of the application. There is also links to the "Recipes", "Add (recipes)", "Cuisines" and Graphs. The navbar will appear on all pages.

#### __Belly Convent__  
 
* Or Recipes is a __list of recipes__ that at the same time is the Home page. This consist of the recipes list containing  the recipe name and their food group shown in a __acordeon__ that if *clicked* will display a small intro acout the recipe. Before each recipe name there are __two options__, one is for **editing** the recipe and one is for **viewing the full recipe**, preceded by some **glyphicons**.
    * The __editing button__ edites the recipe in all the fields that are available in the database.
    * The __green arrow__ redirects the user to the recipe __full detail__, differentiated from the small preview present in the accordeon. This full detailed page consits of all the data present in the database, image, name, prep-time, etc
* __Sorting dropdown__ above the list, delievers different parameters to order the recipe list.
* __The Search box__ offers the user the function of searching by words in the data-base
* __Pagination__ is present in the Recipe list and in the searching results if required by the results
FOOTER
* __Add Recipe__ is a green button that redirects the user to the add recipe page

#### __Add Recipe__ 

 Contains a formular that takes data in different fiels and saves it into the Mongo Db database. This Fields are: 
* Cuisine Category
* Chef Selection
* Course Selection
* Food group
* Food facts
* Food name
* Food description
* Celiacs(checkbox)
* Gluten free(checkbox)
* Cooking Time(slidebar)
* Preparation time(slidebar)
* Recipe Url

In this formular I didn't added the upvotes function, that is only available in the __recipes detail view__

#### __Cuisines__

Presents a list of the cuisines types and also it integrates two small buttons _edit_ and _delete_. But this time the buttons edit / delete the cuisine type and not the recipe.

AUTHOR
FOOD GROUP
COURSE

#### __Graphics__
 Five diagrams that reflect in a statistical maner different relation between different variables between the recipes database. That allows the user to easily diferenciate between authors and type of cuisine, for instance and many other different relationships. They are realized with dc.js, crossfilter, queue, and d3.js. 






Navbar - Consists of the DADDY DOES DINNER logo which returns the user to the "Home" page of the application. There is also links to the "Recipes", "My Recipes", "Login / Dashboard" and Contact forms. The navbar will appear on all pages.
Home - The home page consists of 4 sample recipes along with some information on contacting the webmaster and a link to the contact us page of the site.
All Recipes - Directs the user to the "All Recipes" page which displays ALL recipes from ALL users which have been entered on the site. The user can then filter or browse through the recipes. The can view more information on each recipe by selectign the "See Recipe" link which delivers the user to the "Recipe Detail" page.
Recipe Detail - Provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, base ingredients, ingredients, instructions, author and date posted.
My Recipes - Provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.
Login/Dashboard - When first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database. Once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 3 data charts depicting the number of base ingredients, meal types and food flavours associated with the recipes which have been added.
Contact - Delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). Their are also 4 social media buttons so that the user may interact on social networks. (Links NOT LIVE current social media pages for this project as this is not a real business)
Social Links - Provides users with links to the website social media pages and also shortcuts to the "All Recipes" & "My Recipes" pages.(Links NOT LIVE current social media pages for this project as this is not a real business).

*  Above the recipe list the page displays a menu  with the name of the restaurant. And options for Recipes, add recipe, cuisine and Graphics.


* The sorting and search function will search by word among the recipes and sort the recipes in different ways, and criterium
* The edit button will take you to edit the recipe as the user desires. Selecting cusine, author, predominant group of food, food course, allergens like Gluten free and celiacs. Also one ca select  in a range selector the preparation and the cooking time set by minutes, the foor ingredients, description, contect( that is small introduction) and finally the name.
* The arrow next to the Edit recipe button will display fully the recipe with all the fiels(food ingredients, author name, gluten free, etc) available and with an image assigend by _html_. There is also a delete button that, when clicked will guide you to a modal dialogue that will ensure that the user is aware of the complet deletion of the recipe.
* 
_pagination_ ...........

* Add recipe. Here the user will be able to ad a recipe.

* Cuisine_author_, _predominant.........     etc_  a page where one can see all the cuisine list, edit them and delete them as well

* Graphic a serie of five graphichs displayed with the help of d3, crossfilter that help the user see in an easy and graphic way the relation bethween for instance time of cooking and cuisine type. 








#### Working Features

This is a web application which allows users to store and easily access cooking recipes. It is a full stack web application (**_frontend and backend_**) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted and available on Heroku platform as a service. Here users can :

1. **Create** or ad a recipe to the Mongo Db database with the inclusion of different fields, such as time of preparation, food description, gluten free friendly, etc.
2. **Read** from the data base the files there founded, and retrieve them to the app in a variaty of details. With this I mean that the user can see a list of the recipes, ##_sorted by pagination yet to be implemented_**........, or can select each recipe in a unique page and inspect it with all the specifications available. Also is retrived a list with the types of cuisines **_authors, predominant groups, upvotes_**
3. **Update** the recipes cuisines, and their properties in a easy quick way by the users needs and likes
4. **Delete** a recipe or a cuisine type,**_author, group,etc_.......** , alway after a modal security question that informs the user that he is going to delete forever the file.

5. **Dashboard** displays a graphic relation between cooking time, preparation tyme, cuisine name, author name and food groups
6. **Search and sort** function allow the user to search by word among the database, and the sort function orders the list under different criteria such as author, predominant group, etc.
 


#### Features Left to Implement

1. Upvotes
2. Login
3. Pagination
4. Fix Search functionality
5. Add author, food group in cathegories, etc
6. Images upload available
7. Export to PDF, download a recipe.






### Technologies Used

* **_HTML, CSS, JaveScript_** with the help of jQuery fot the front end code

* **_Materialize, Front awsome_** for the display, templates and icons

* **_Python, Flask, Mongo Db_** worked to connect the backend database to the frontend

* **_Heroku_**  Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

* **_TravisCl_** used to test the code

* **_Flask_testing_** used to test framework functionality and its coninuous integration to Flask app and database (SQL or NON SQL)

* **_Unittest_** was used to build the testing framework.





### Testing 

### Responsive Testing

 ***********The app was tested on Samsung S8, Apple iPhone 6, etc,(all the deviced served in the Chrome developer tools) and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. There were many issues founded most of them with the css sidevar/ navbar not resizing, card etc. Also this tool is usefull ,using their console, in founding java errors,retrieving the raw data from the data base, and proving the flask sessions reliability. 
 ***********














### Challenges

* Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store. I saw that a good organized database gives powers to a novel programmer like me.

* Managing routes and URL's with Flask was also very interesting and I learned a powerful feature from reading the documentation around Flask and MongoDB. This feature gives speed and facilitate the work of a programmer.

* Implementing, or trying to extra features, such as pagination, user login that have taught me a parallel way of learning out of the course box, that I think I will be using in all my future carrer.





 
