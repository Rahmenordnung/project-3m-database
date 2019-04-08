import os
from flask import (Flask, render_template, redirect, request, url_for,
    send_from_directory,session, flash, jsonify)
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


def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in first!!!')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", procedure=mongo.db.procedures.find().sort('cooking_time', pymongo.ASCENDING))
    
    
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
    
    return '/file/<filename>'
       
    
    

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
        'food_ingredients': request.form.get('food_ingredients')
    })
    return redirect(url_for('get_tasks'))
    
@app.route('/delete_recipe/<procedure_id>')
def delete_recipe(procedure_id):
    mongo.db.procedures.remove({'_id': ObjectId(procedure_id)})
    return redirect(url_for('get_tasks'))
    

@app.route('/see_recipe/<procedure_id>')
def see_recipe(procedure_id):
    procedure = mongo.db.procedures.find_one({"_id": ObjectId(procedure_id)})
    return render_template("recipe_view.html", procedure=procedure, )

    
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
            'food_course':request.form.get('food_course')
            
        })
    return redirect(url_for('get_cuisine'))
    
    
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove(
        {'_id': ObjectId(cuisine_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            'food_course':request.form.get('food_course')
            
        })
    return redirect(url_for('get_cuisine'))  
    
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine = mongo.db.cuisine
    cuisine_country = {'cuisine_name': request.form.get('cuisine_name'),
                        'food_course': request.form.get('food_course')}
    cuisine.insert_one(cuisine_country)
    return redirect(url_for('get_cuisine'))

    
@app.route('/new_cuisine')
def new_cuisine():
    return render_template('addcuisine.html')
###---------------------------------------------    
@app.route('/recipes_time_desc')
def recipes_time_desc():
    tasks_sorted_desc = mongo.db.recipes.find(
        {"cooking-time": {"$gt": 0}}).sort([("cooking-time", -1)])
    return render_template("tasks.html",  procedure=mongo.db.procedures.find().sort('cooking_time', pymongo.DESCENDING))
    

# by Cooking-time ascending
@app.route('/recipes_time_asc')
def recipes_time_asc():
    tasks_sorted_asc = mongo.db.recipes.find(
        {"cooking-time": {"$gt": 0}}).sort([("cooking_time", 1)])
    return render_template("tasks.html",  procedure=mongo.db.procedures.find().sort('cooking_time', pymongo.ASCENDING))
###-----------------------------------  
@app.route('/graphic')
def graphic():
    return render_template('graphos.html')
    
    
@app.route('/procedures')
def get_procedures():
    json_procedures = []
    for procedure in mongo.db.procedures.find():
        json_procedures.append(procedure)
    json_procedures = json.dumps(json_procedures, default=json_util.default)
    return json_procedures
 
    
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
    
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)