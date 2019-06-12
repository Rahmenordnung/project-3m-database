import os
import math
import json
from flask import (Flask, render_template, redirect, request, url_for,
    send_from_directory,session, flash, jsonify,abort)
from functools import wraps
from flask_pymongo import PyMongo, pymongo 
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
##from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.secret_key = "b'\xf2\xe8\x1f\x93n\xedT\xbe\x88\xd1\xf7\xddL\x106EO\x89\x91Xf\xe3d\x0b'"
app.config["MONGO_DBNAME"] = 'cooking_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
MONGO_URI = os.getenv('MONGO_URI')
FIELDS = {
    'food_course': True,
    'author_name': True,
    'cooking_time': True,
    'predominant_group': True,
    'preparation_food': True,
    'cuisine_name': True,
    '_id': False
}

mongo = PyMongo(app)

###---pagination and sorting----###

PAGE_SIZE = 10
KEY_PAGE_SIZE = 'page_size'
KEY_PAGE_NUMBER = 'page_number'
KEY_TOTAL = 'total'
KEY_PAGE_COUNT = 'page_count'
KEY_ENTITIES = 'items'
KEY_NEXT = 'next_uri'
KEY_PREV = 'prev_uri'
KEY_SEARCH_TEXT = 'search_text'
KEY_ORDER_BY = 'order_by'
KEY_ORDER = 'order'

def get_paginated_list(**params):
    page_size = int(params.get(KEY_PAGE_SIZE, PAGE_SIZE))
    page_number = int(params.get(KEY_PAGE_NUMBER, 1))
    order_by = params.get(KEY_ORDER_BY, '_id')
    order = params.get(KEY_ORDER, 'asc')
    order = pymongo.ASCENDING if order == 'asc' else pymongo.DESCENDING
    if page_number < 1:
        page_number = 1
    offset = (page_number - 1) * page_size
    items = []
    search_text = ''
    if KEY_SEARCH_TEXT in params:
        search_text = params.get(KEY_SEARCH_TEXT)
        total_items = 0
        if len(search_text.split()) > 0:
            mongo.db.procedures.create_index([("$**", 'text')])
            result = mongo.db.procedures.find({'$text': {'$search': search_text}})
            total_items = result.count()
            items = result.sort(order_by, order).skip(offset).limit(page_size)
        else:
            total_items = mongo.db.procedures.count()
            items = mongo.db.procedures.find().sort(
                order_by, order
            ).skip(offset).limit(page_size)
    else:
        total_items = mongo.db.procedures.count()
        items = mongo.db.procedures.find().sort(order_by, order).skip(
            offset).limit(page_size)
    
    if page_size > total_items:
        page_size = total_items
    if page_number < 1:
        page_number = 1
    if page_size:
        page_count = math.ceil(total_items / page_size)
    else:
        page_count = 0

    if page_number > page_count:
        page_number = page_count
        
    next_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number + 1
    } if page_number < page_count else None
    prev_uri ={
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number - 1
    } if page_number > 1 else None

    return {
        KEY_TOTAL: total_items,
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_COUNT: page_count,
        KEY_PAGE_NUMBER: page_number,
        KEY_NEXT: next_uri,
        KEY_PREV: prev_uri,
        KEY_SEARCH_TEXT: search_text,
        KEY_ORDER_BY: order_by,
        KEY_ORDER: order,
        KEY_ENTITIES: items
    }



###-----------------main route/home-page
@app.route('/')
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    procedures = get_paginated_list(**request.args.to_dict())
    return render_template("tasks.html", result=procedures)


###-----------------Authentification--
# def login_required(f):
#     @wraps(f)
#     def wrap(*args,**kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Please log in first!!!')
#             return redirect(url_for('login'))
#     return wrap

        
     
# Route for handling the login page logic
@app.route('/login', methods=['GET'])

def login():

	# Check if user is not logged in already

	if 'user' in session:

		user_in_db = mongo.db.users.find_one({"username": session['user']})

		if user_in_db:

			# If so redirect user to his profile

			flash("You are logged in already!")

			return redirect(url_for('profile', user=user_in_db['username']))

	else:

		# Render the page for user to be able to log in

		return render_template("login.html")
    
    
@app.route('/user_check', methods=['POST'])

def user_check():

	form = request.form.to_dict()

	user_in_db = mongo.db.users.find_one({"username": form['username']})

	# Check for user in database

	if user_in_db:

		# If passwords match (hashed / real password)

		if check_password_hash(user_in_db['password'], form['pass']):

			# Log user in (add to session)

			session['user'] = form['username']

			# If the user is admin redirect him to admin area

			if session['user'] == "admin":

				return redirect(url_for('admin'))

			else:

				flash("You were logged in!")

				return redirect(url_for('profile', user=user_in_db['username']))

			

		else:

			flash("Wrong password or user name!")

			return redirect(url_for('login'))

	else:

		flash("You must be registered!")

		return redirect(url_for('register'))

@app.route('/logout')
#@login_required
def logout():
    session.clear()
    flash('you\'re now logged out')
    return redirect(url_for('get_tasks'))
    

@app.route('/profile/<user>')

def profile(user): 

	# Check if user is logged in

	if 'user' in session:

		# If so get the user and pass him to template for now

		user_in_db = mongo.db.users.find_one({"username": user})

		return render_template('profile.html', user=user_in_db)

	else:

		flash("You must be logged in!")

		return redirect(url_for('index'))    
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        form = request.form.to_dict()
        if form ['user_password'] == form ['user_password1']:
            user = mongo.db.users.find_one(
                {
                    'username':form['username']
                }
            )
            if user:
                error = "{request.form['username']} already exists!!!"
                flash ("{request.form['username']} already exists!!!")
                return redirect(url_for('register'))
            else:
                hash_pass = generate_password_hash(form['user_password'])
                mongo.db.users.insert_one(
                    {
                        'username': form['username'],
                        'email': form ['email'],
                        'password': hash_pass,
                        'recipes_user': [],
                    }
                )
                return redirect(url_for('login'))
                user_in_db = mongo.db.users.find_one({
                    "username": form['username']
                })
                if user_in_db:
                    session['profile_user'] = form['username']
                    flash ("you were registered as {form['username']}")
                    return redirect(url_for('tasks'))
                else:
                    flash ("Something went wrong during your registration, Please try again!")
                    return redirect(url_for('register'))
        else:
            flash("Passwords matching error. Try again!!!")
            return redirect(url_for('register'))
    return render_template("register.html")        
        
        
###-----------------Recipes--    
    
##add recipe--
@app.route('/add_recipe')
#@login_required
def add_recipe():
    return render_template('addrecipe.html',
        procedures=mongo.db.procedures,
        cuisine=mongo.db.cuisine.find(),
        food_type=mongo.db.food_type.find(), 
        food_group=mongo.db.food_group.find(),
        recipe_author=mongo.db.recipe_author.find())
        
##add an new recipe--
def insert_recipe_data(data):
    procedures=mongo.db.procedures
    return procedures.insert_one(data)

@app.route('/insert_recipe', methods=['POST'])    
def insert_recipe():
    insert_recipe_data(request.form.to_dict())
    return redirect(url_for('get_tasks'))        
    
##edit recipe--    
@app.route('/edit_recipe/<procedure_id>')
def edit_recipe(procedure_id):
    the_procedure = mongo.db.procedures.find_one({"_id": ObjectId(procedure_id)})
    all_cuisine = mongo.db.cuisine.find()
    all_food = mongo.db.food_type.find()
    all_groups = mongo.db.food_group.find()
    famous_chefs= mongo.db.recipe_author.find()
    return render_template('editrecipe.html', procedure=the_procedure, cuisine = all_cuisine, food_type = all_food, food_group = all_groups, recipe_author=famous_chefs)
    
# Check for for the records in database and updates them    
@app.route('/update_recipe/<procedure_id>', methods=["POST"])
def update_recipe(procedure_id):
    procedures = mongo.db.procedures
    procedures.update ({'_id': ObjectId (procedure_id)},
    {
        'food_name': request.form.get ('food_name'),
        'cuisine_name': request.form.get ('cuisine_name'),
        'food_course': request.form.get ('food_course'),
        'food_description': request.form.get ('food_description'),
        'celiacs': request.form.get ('celiacs'),
        'gluten_free': request.form.get ('gluten_free'),
        'preparation_food': request.form.get ('preparation_food'),
        'cooking_time': request.form.get('cooking_time'),
        'food_context': request.form.get('food_context'),
        'food_ingredients': request.form.get('food_ingredients'),
        'author_name': request.form.get('author_name'),
        'predominant_group': request.form.get('predominant_group'),
        'image':request.form.get('image')
    })
    return redirect(url_for('get_tasks'))
    
##removes a recipe--    
@app.route('/delete_recipe/<procedure_id>')
def delete_recipe(procedure_id):
    mongo.db.procedures.remove({'_id': ObjectId(procedure_id)})
    return redirect(url_for('get_tasks'))
    
## full recipe view-- 
@app.route('/see_recipe/<procedure_id>')
def see_recipe(procedure_id):
    procedure = mongo.db.procedures.find_one({"_id": ObjectId(procedure_id)})
    ##procedures_collection = cooking_book.procedures
    ##procedure_ids = procedures_collection.find({},{"_id":1})
    return render_template("recipe_view.html", procedure=procedure )





###-----------------Cuisine(CRUD Functionality)    
@app.route('/get_cuisine')
def get_cuisine():
    cuisine = get_paginated_list(**request.args.to_dict())
    return render_template('cuisine.html',
                           cuisine=mongo.db.cuisine.find(), result=cuisine)
                           
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html', 
    cuisine=mongo.db.cuisine.find_one({'_id': ObjectId(cuisine_id)}))
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisine.update(
        {'_id': ObjectId(cuisine_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            
        })
    return redirect(url_for('get_cuisine'))
    
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove(
        {'_id': ObjectId(cuisine_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            
        })
    return redirect(url_for('get_cuisine'))
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine = mongo.db.cuisine
    cuisine_country = {'cuisine_name': request.form.get('cuisine_name'),
                        }
    cuisine.insert_one(cuisine_country)
    return redirect(url_for('get_cuisine'))
    
@app.route('/new_cuisine')
def new_cuisine():
    return render_template('addcuisine.html')
    
###-----------------Chefs(Authors)CRUD Functionality
@app.route('/get_author')
def get_author():
    return render_template('author_chef.html',
                           recipe_author=mongo.db.recipe_author.find())
                           
@app.route('/edit_author/<recipe_author_id>')
def edit_author(recipe_author_id):
    return render_template('edit_author.html', 
    recipe_author=mongo.db.recipe_author.find_one({'_id': ObjectId(recipe_author_id)}))
    
@app.route('/update_author/<recipe_author_id>', methods=['POST'])
def update_author(recipe_author_id):
    mongo.db.recipe_author.update(
        {'_id': ObjectId(recipe_author_id)},
        {
            'author_name':request.form.get('author_name')
        })
    return redirect(url_for('get_author'))
    
@app.route('/delete_author/<recipe_author_id>')
def delete_author(recipe_author_id):
    mongo.db.recipe_author.remove(
        {'_id': ObjectId(recipe_author_id)},
        {
            'author_name':request.form.get('author_name')
        })
    return redirect(url_for('get_author'))
    
@app.route('/insert_author', methods=['POST'])    
def insert_author():
    recipe_author = mongo.db.recipe_author
    chef_world = {'author_name': request.form.get('author_name')}
    recipe_author.insert_one(chef_world)
    return redirect(url_for('get_author'))
    
@app.route('/new_author')
def new_author():
    return render_template('add_author.html')    

###-----------------food courses(CRUD Functionality)

@app.route('/get_food_type')
def get_food_type():
    return render_template('food_type.html',
                           food_type=mongo.db.food_type.find())
                           
@app.route('/edit_food_type/<food_type_id>')
def edit_food_type(food_type_id):
    return render_template('edit_food_course.html', 
    food_type=mongo.db.food_type.find_one({'_id': ObjectId(food_type_id)}))
    
@app.route('/update_food_type/<food_type_id>', methods=['POST'])
def update_food_type(food_type_id):
    mongo.db.food_type.update(
        {'_id': ObjectId(food_type_id)},
        {
            'food_course':request.form.get('food_course')
        })
    return redirect(url_for('get_food_type'))
    
@app.route('/delete_food_type/<food_type_id>')
def delete_food_type(food_type_id):
    mongo.db.food_type.remove(
        {'_id': ObjectId(food_type_id)},
        {
            'food_course':request.form.get('food_course')
        })
    return redirect(url_for('get_food_type'))
    
@app.route('/insert_food_type', methods=['POST'])    
def insert_food_type():
    food_type = mongo.db.food_type
    cuisines = {'food_course': request.form.get('food_course')}
    food_type.insert_one(cuisines)
    return redirect(url_for('get_food_type'))
    
@app.route('/new_course')
def new_course():
    return render_template('add_food_type.html')

###-----------------food-group(CRUD Functionality)

@app.route('/get_food_group')
def get_food_group():
    return render_template('food_group.html',
                           food_group=mongo.db.food_group.find())
                           
@app.route('/edit_food_group/<food_group_id>')
def edit_food_group(food_group_id):
    return render_template('edit_food_group.html', 
    food_group=mongo.db.food_group.find_one({'_id': ObjectId(food_group_id)}))
    
@app.route('/update_food_group/<food_group_id>', methods=['POST'])
def update_food_group(food_group_id):
    mongo.db.food_group.update(
        {'_id': ObjectId(food_group_id)},
        {
            'predominant_group':request.form.get('predominant_group')
        })
    return redirect(url_for('get_food_group'))
    
@app.route('/delete_food_group/<food_group_id>')
def delete_food_group(food_group_id):
    mongo.db.food_group.remove(
        {'_id': ObjectId(food_group_id)},
        {
            'predominant_group':request.form.get('predominant_group')
        })
    return redirect(url_for('get_food_group'))
    
@app.route('/insert_food_group', methods=['POST'])    
def insert_food_group():
    food_group = mongo.db.food_group
    calories = {'predominant_group': request.form.get('predominant_group')}
    food_group.insert_one(calories)
    return redirect(url_for('get_food_group'))
    
@app.route('/new_food_group')
def new_food_group():
    return render_template('add_food_group.html')                           
    
    
       
###-----------------Votes-users, etc
    # Voting:
# Upvote recipe
@app.route('/upvote_recipe/<procedure_id>', methods=["GET"])
def upvote_recipe(procedure_id):
    procedures = mongo.db.procedures
    procedures.update({
        '_id': ObjectId(procedure_id)
        }, {
            '$inc': {
                'votes': 1
            }
        }
    )
    return redirect(url_for('see_recipe', procedure_id=procedure_id))

# Downvote recipe
@app.route('/downvote_recipe/<procedure_id>', methods=["GET", "POST"])
def downvote_recipe(procedure_id):
    procedures = mongo.db.procedures
    procedures.update({'_id': ObjectId(procedure_id)},
                   {
        '$inc': {'votes': -1}
    }
    )
    return redirect(url_for('see_recipe', procedure_id=procedure_id))
    
###--------------------------grafic java---------  
def get_recipes():
    procedures = mongo.db.procedures.find()
    json_procedures = []
    for procedure in procedures:
        json_procedures.append(procedure)
    json_procedures = json.dumps(json_procedures, default=json_util.default)
    return json_procedures

@app.route('/graphic')
def graphic():
    return render_template('graphos.html', recipes=get_recipes())
    
@app.route("/cooking_book/procedures")
def donor_projects():
    #connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    # connection = MongoClient(MONGO_URI)
#This connection is required when hosted using a remote mongo db.
    # collection = connection['cooking_book']['procedures']
    procedures = mongo.db.procedures.find()
    json_procedures = []
    for procedure in procedures:
        json_procedures.append(procedure)
    json_procedures = json.dumps(json_procedures, default=json_util.default)
    # connection.close()
    return json_procedures
    
    
# Search  **********************************************************************
# Search term from search box
@app.route('/search_box/', methods=["POST"])
def search_box():
    search_term = request.form['search_text']
    if search_term:
        return redirect(url_for('search_results', search_text=search_term))
    else:
        return render_template("task.html", procedures=mongo.db.procedures.find())

    
# Search results route
@app.route('/search_results', methods=["POST"])
def search_results():
    return redirect(url_for('get_tasks', search_text=request.form['search_text']))
    
    
#Error handlers ---------------    
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html') 


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html') 


@app.errorhandler(403)
def method_not_allowed(error):
    return render_template('403.html')      


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)