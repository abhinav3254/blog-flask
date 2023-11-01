from flask import Flask, request, jsonify
import database.DatabaseConfig as dbConfig
import classes.User as User
import user.SignUp as signUp
import user.LogInUser as login

app = Flask(__name__)

# This method is for testing purpose
# to check if connection with database is successful or not
@app.route("/")
def get_test_data():
    connection = dbConfig.create_db_connection();
    cursor = connection.cursor()
    cursor.execute("select * from public.test;")
    rows = cursor.fetchall()
    return jsonify({'data': rows})



@app.route("/register", methods=['POST'])
def register_user():
    user_data = request.json
    name = user_data.get('name')
    email = user_data.get('email')
    password = user_data.get('password')
    new_user = User.User(name, email, password)  # Create a new user
    ans = signUp.signUpUser(new_user)  # Sign up the new user
    if ans:
        return jsonify({'success': ans}), 201
    else:
        return jsonify({'unsuccessful': 'already registered with this email'}), 412


@app.route("/login", methods=['POST'])
def login_user():
    user_data = request.json
    email = user_data.get('email')
    password = user_data.get('password')
    print(email+'  '+password)
    new_user = User.User(0,email,password)
    ans = login.logInUser(email,password)
    # ans = True
    if ans:
        return 'correct cred'
    else:
        return 'incorrect'


if __name__ == "__main__":
    app.run(debug=True, port=5001)
