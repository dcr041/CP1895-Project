from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import csv
import os

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route("/view_recipes")
def view_recipes():
    recipe_list = read_from_csv()
    return render_template('view_recipes.html', recipe_list=recipe_list, title='View Recipes')


app.config['UPLOAD_PATH'] = 'static/images'
IMAGE_TYPES = {"png", "jpg", "jpeg"}


@app.route("/add_recipes", methods=["GET", "POST"])
@login_required
def add_recipes():
    if request.method == "POST":

        recipe_name = request.form.get("recipe_name")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        servings = request.form.get("servings")
        uploaded_file = request.files["image_upload"]
        file_upload_type = uploaded_file.filename.split(".")[-1]
        if uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], uploaded_file.filename))
            columns = ['Name', 'Ingredients', 'Instructions', 'Servings', 'File']
            all_recipes = read_from_csv()
            recipe = {'Name': recipe_name, 'Ingredients': ingredients, 'Instructions': instructions,
                      'Servings': servings, 'File': uploaded_file.filename}
            all_recipes.append(recipe)
            write_to_csv(all_recipes, columns)
            print(all_recipes)
        elif file_upload_type not in IMAGE_TYPES:
            flash("Image upload must be of type jpg, jpeg, or png")
            return render_template('add_recipes.html', title='Add Recipes')

        return redirect(url_for("home"))
    else:
        return render_template('add_recipes.html', title='Add Recipes')


@app.route("/delete_recipe", methods=["POST", "GET"])
@login_required
def delete_recipe():
    recipe_list = read_from_csv()
    columns = ['Name', 'Ingredients', 'Instructions', 'Servings', 'File']
    print(recipe_list)
    if request.method == "POST":
        recipe_name = request.form['delete_select']
        for i in range(len(recipe_list)):
            if recipe_list[i]['Name'] == recipe_name:
                image = recipe_list[i]['File']
                path = 'static/images'
                file = os.path.join(path, image)
                os.remove(file)
                del recipe_list[i]
                break
        flash("Recipe successfully deleted.")
        write_to_csv(recipe_list, columns)
    return render_template('delete_recipe.html', recipe_list=recipe_list, title='Delete Recipe')


def write_to_csv(all_recipes, columns):
    with open("recipes.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for key in all_recipes:
            writer.writerow(key)
    print("Writing to csv complete.")


def read_from_csv():
    recipes = []
    with open('recipes.csv') as datafile:
        data_reader = csv.DictReader(datafile)
        for row in data_reader:
            recipes.append(row)
    return recipes


if __name__ == "__main__":
    app.run(debug=True)