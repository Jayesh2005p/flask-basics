"""
Part 2: Templates - Rendering HTML Files
=========================================
Instead of returning HTML strings, we'll use separate HTML files!

Learning Goals:
- Understand why we use templates (separation of concerns)
- Learn about the templates/ folder convention
- Use render_template() to serve HTML files

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

# Import render_template along with Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Instead of returning a string, we return render_template()
    Flask automatically looks in the 'templates/' folder for the HTML file
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Another route that renders a different template
    """
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# FOLDER STRUCTURE FOR THIS PART:
# =============================================================================
#
# part-2/
# ├── app.py              <- You are here
# └── templates/          <- Flask looks here for HTML files
#     ├── index.html      <- Home page template
#     └── about.html      <- About page template
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 2.1: Modify the templates
#   - Edit index.html and add more content
#   - Refresh browser to see changes
#
# Exercise 2.2: Create a new page
#   - Create templates/contact.html
#   - Add a new route @app.route('/contact')
#   - Return render_template('contact.html')
#
# Exercise 2.3: Add navigation
#   - Add <a href="/"> and <a href="/about"> links to both pages
#   - Test clicking between pages
#
# =============================================================================
