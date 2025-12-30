"""
Part 1: Hello Flask - Your First Web Server
============================================
This is the minimal Flask application - just 5 lines of essential code!

Learning Goals:
- Understand how to import and create a Flask app
- Learn what @app.route() decorator does
- See how to return a response to the browser
- Run your first web server

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

# Step 1: Import Flask class from the flask package
from flask import Flask

# Step 2: Create an instance of the Flask class
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)


# Step 3: Define a route using the @app.route() decorator
# '/' means this function handles the home page (root URL)
@app.route('/')
def home():
    """
    This function runs when someone visits http://localhost:5000/
    Whatever we return here gets displayed in the browser
    """
    return "Hello Flask! Welcome to my first web server!"


# Step 4: Run the application
# debug=True means:
#   - Server auto-restarts when you change code
#   - Shows detailed error messages in browser
if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# EXERCISES - Try these after running the basic app:
# =============================================================================
#
# Exercise 1.1: Change the return message
#   - Modify the return statement to say "Hello [Your Name]!"
#   - Save the file and refresh your browser (server auto-reloads!)
#
# Exercise 1.2: Return HTML instead of plain text
#   - Change the return to: return "<h1>Hello Flask!</h1><p>This is HTML</p>"
#   - Notice how the browser renders it as formatted HTML
#
# Exercise 1.3: Add a second route
#   - Add another function with @app.route('/about')
#   - Return something like "This is the about page"
#   - Visit http://localhost:5000/about in your browser
#
# =============================================================================
