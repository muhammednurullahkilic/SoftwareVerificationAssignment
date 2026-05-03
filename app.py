from flask import Flask, render_template, request
from validators import is_valid_name, is_valid_email, is_valid_password, is_valid_dob, passwords_match

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_account():
    errors = {}
    success = False

    if request.method == 'POST':
        first = request.form['first_name']
        last = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm_password']
        dob = request.form['dob']

        if not is_valid_name(first): errors['first_name'] = "Invalid first name"
        if not is_valid_name(last): errors['last_name'] = "Invalid last name"
        if not is_valid_email(email): errors['email'] = "Invalid email"
        if not is_valid_password(password): errors['password'] = "Weak password"
        if not passwords_match(password, confirm): errors['confirm'] = "Passwords do not match"
        if not is_valid_dob(dob): errors['dob'] = "You must be at least 18 years old"

        if not errors:
            success = True

    return render_template('form.html', errors=errors, success=success)

if __name__ == '__main__':
    app.run(debug=True)