from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']= 'mongo "mongodb+srv://root:r00tUser@myfirstclusterc-cfglx.mongodb.net/cooking_book?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def index():
    return '''
        form method="POST" action="/create" enctype="multipart/form-data">
           <input type="text" name="username">
           <input type="file" name="profile_image">
           <input type="submit">
        
        </form>
        '''
