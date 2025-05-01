import yaml, json
from flask import Flask, render_template, abort


app = Flask(__name__)

with open("./static/projects.yaml", "r") as f:
    PROJECTS = yaml.safe_load(f)

@app.route('/articles/<slug>')
def article_detail(slug):
    return render_template('article_detail.html', slug=slug, article={'slug': slug})

@app.route("/projects/<project_name>")
def project_detail(project_name):
    project = PROJECTS.get(project_name)
    if not project:
        abort(404)
    return render_template("project_detail.html", project=project)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)

@app.route('/articles')
def articles():
    with open('static/pdfs/index.json') as f:
        articles = json.load(f)
    return render_template('articles.html', articles=articles)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
