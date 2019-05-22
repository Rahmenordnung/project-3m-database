import os
import math

from flask import (Flask, render_template, redirect, request, url_for,
    send_from_directory,session, flash, jsonify,abort)
   
from functools import wraps
from flask_pymongo import PyMongo, pymongo 
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
import json

app = Flask(__name__)
app.secret_key = "Redbull gives you wings"
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

###pagination and sorting###

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


def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in first!!!')
            return redirect(url_for('login'))
    return wrap


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


@app.route('/')
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    print(request.args)
    procedures = get_paginated_list(**request.args.to_dict())
    print(procedures)
    return render_template("tasks.html", result=procedures)


@app.route('/upload', methods=['POST'])
def upload():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name' :profile_image.filename})

    return 'DonnnesQ!!'
    
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)
    
@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.users.find_one_or_404({'username' : username})
    return render_template("task1.html")
        
       
    
    

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('you\'re logging has been successful')
            return redirect(url_for('add_recipe'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('you\'re now logged out')
    return redirect(url_for('get_tasks'))
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisine=mongo.db.cuisine.find(),
        food_type=mongo.db.food_type.find(), 
        food_group=mongo.db.food_group.find(),
        recipe_author=mongo.db.recipe_author.find())
    
    
@app.route('/edit_recipe/<procedure_id>')
def edit_recipe(procedure_id):
    the_procedure = mongo.db.procedures.find_one({"_id": ObjectId(procedure_id)})
    all_cuisine = mongo.db.cuisine.find()
    all_food = mongo.db.food_type.find()
    all_groups = mongo.db.food_group.find()
    famous_chefs= mongo.db.recipe_author.find()
    return render_template('editrecipe.html', procedure=the_procedure, cuisine = all_cuisine, food_type = all_food, food_group = all_groups, recipe_author=famous_chefs    )
    
    
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
    

    
@app.route('/delete_recipe/<procedure_id>')
def delete_recipe(procedure_id):
    mongo.db.procedures.remove({'_id': ObjectId(procedure_id)})
    return redirect(url_for('get_tasks'))
    

@app.route('/see_recipe/<procedure_id>')
def see_recipe(procedure_id):
    procedure = mongo.db.procedures.find_one({"_id": ObjectId(procedure_id)})
    ##procedures_collection = cooking_book.procedures
    ##procedure_ids = procedures_collection.find({},{"_id":1})
    return render_template("recipe_view.html", procedure=procedure )


@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name':profile_image.filename})
    return 'Done!'    
        
    
@app.route('/insert_recipe', methods=['POST'])    
def insert_recipe():
    procedures=mongo.db.procedures
    procedures.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
    
    
@app.route('/get_cuisine')
def get_cuisine():
    return render_template('cuisine.html',
                           cuisine=mongo.db.cuisine.find())
                           
#@app.route('/get_author', methods=['GET'])
#def get_author():
    #return render_template('author_chef.html',
      #                     author_name=mongo.db.recipe_author.find())
                           

                               
                           

@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html', 
    cuisine=mongo.db.cuisine.find_one({'_id': ObjectId(cuisine_id)}))
    
#@app.route('/edit_author/<recipe_author_id>')
#def edit_author(recipe_author_id):
 #   return render_template('editcuisine.html', 
  #  author=mongo.db.recipe_author.find_one({'_id': ObjectId(recipe_author_id)}))     
    
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisine.update(
        {'_id': ObjectId(cuisine_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            'food_course':request.form.get('food_course')
            
        })
    return redirect(url_for('get_cuisine'))
    
#@app.route('/update_author/<recipe_author_id>', methods=['POST'])
#def update_author(recipe_author_id):
 #   mongo.db.recipe_author.update(
  #      {'_id': ObjectId(recipe_author_id)},
   #     {
    #        'author_name':request.form.get('author_name')
     #   })
    #return redirect(url_for('get_author'))    
    
    
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove(
        {'_id': ObjectId(cuisine_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            'food_course':request.form.get('food_course')
            
        })
    return redirect(url_for('get_cuisine'))
    
#@app.route('/delete_author/<recipe_author_id>')
#def delete_author(recipe_author_id):
    #mongo.db.recipe_author.remove(
        #{'_id': ObjectId(recipe_author_id)},
       # {
      #      'author_name':request.form.get('author_name')
     #   })
    #return redirect(url_for('get_author'))      
    
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine = mongo.db.cuisine
    cuisine_country = {'cuisine_name': request.form.get('cuisine_name'),
                        'food_course': request.form.get('food_course')}
    cuisine.insert_one(cuisine_country)
    return redirect(url_for('get_cuisine'))
    

#@app.route('/insert_author', methods=['POST'])    
#def insert_author():
 #   recipes_author=mongo.db.recipes_author
  #  recipes_author.insert_one(request.form.to_dict())
   # return redirect(url_for('get_author'))

    
@app.route('/new_cuisine')
def new_cuisine():
    return render_template('addcuisine.html')
    
#@app.route('/new_author')
#def new_author():
    return render_template('addcuisine.html')    
    
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
    
@app.route('/procedures')
def get_procedures():
    return get_recipes()
 
    
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