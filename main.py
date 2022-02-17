from flask import Flask

# ===== Routing =====
from routes.main_routes import data
from routes.api_routes import api_data


app = Flask(__name__)

# ===== Blueprints Registration =====
app.register_blueprint(data, url_prefix="/")
app.register_blueprint(api_data, url_prefix="/api")
