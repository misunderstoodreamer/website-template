from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=False)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            # TODO: add mail checker
            flash(message="Email must be greater than 4 characters", category='error')
        elif len(first_name) < 2:
            flash(message="First name must be greater than 1 characters", category='error')
        elif password1 != password2:
            flash(message="Passwords must be matched", category='error')
        elif len(password1) < 7:
            # TODO: add strong password checker
            flash(message="Password must be greater than 7 characters", category='error')
        else:
            flash(message='Account created', category='success')

    return render_template("sign_up.html")
