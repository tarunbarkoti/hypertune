from flask import Flask, render_template
from routes.dataset import dataset_bp
from routes.model import model_bp
from routes.evaluation import evaluation_bp
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")  # Ensure Flask loads templates
CORS(app)

# Register API routes
app.register_blueprint(dataset_bp, url_prefix="/dataset")
app.register_blueprint(model_bp, url_prefix="/model")
app.register_blueprint(evaluation_bp, url_prefix="/evaluation")

# Ensure UI loads correctly
@app.route("/")
def index():
    return render_template("index.html")  # This should match the correct file in templates/


# Route for the Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for the Plans Page
@app.route('/plans')
def plans():
    return render_template('plans.html')

# Route for the Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for the Updates Page
@app.route('/updates')
def updates():
    return render_template('updates.html')

# Route for the Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/analyse')
def analyse():
    return render_template('analyse.html')

if __name__ == "__main__":
    app.run(debug=True)
