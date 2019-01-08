from flask import Flask, render_template,request, flash, redirect, url_for
from utils.db_queries import get_records
from webapp.model import *
from utils.last_sunday import last_sunday
from webapp.forms import LoginForm
from flask_login import LoginManager, current_user, login_required, login_user, logout_user


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @ app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            data = request.form.to_dict()
            day = data['day']
            month = data['month']
            year = data['year']
            sunday = last_sunday(f"{year}-{month}-{day}")
            days, years, current_top_us, current_top_uk = get_records(sunday)
            return render_template('index.html', days=days, years=years, date=sunday,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)
        else:
            latest_date_uk = (UkChart.query.get(db.session.query(db.func.max(UkChart.id)).first()[0])).date
            latest_date_us = (UsChart.query.get(db.session.query(db.func.max(UsChart.id)).first()[0])).date
            days, years, current_top_us, current_top_uk = get_records(latest_date_uk)
            return render_template('index.html', days=days, years=years, date=latest_date_uk,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        login_form = LoginForm()
        return render_template('login.html', form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(user_name=form.user_name.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Welcome!')
                return redirect(url_for('index'))

        flash('Wrong credentials, please try again.')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash("You're logged out now!")
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Hey admin"
        else:
            return "You're not admin!"

    @app.route("/signup")
    def signup():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template("signup.html")
        #signup_form = SignupForm()
        #return render_template("signup.html", form=signup_form)

    @app.route("/about")
    def about():
        return render_template('about.html')

    return app
