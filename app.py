"""
 Importing Packages
"""
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from extension import db
from routes.user_routes import user_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/devDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(user_routes, url_prefix='/users')

if __name__ == "__main__":
    app.run(debug=True)
