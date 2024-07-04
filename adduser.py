import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://shebinn10:Krizzz%40123@cluster0.xvxphyq.mongodb.net')
db = client['Laboratory']
collection = db['users']

# Sample user data
username = 'wick'
password = 'admin'

# Hash the password
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Check if the user already exists
existing_user = collection.find_one({'username': username})

if existing_user:
    print('User already exists')
else:
    # Insert the new user into the database
    user_data = {'username': username, 'password': hashed_password}
    collection.insert_one(user_data)
    print('User added successfully')
