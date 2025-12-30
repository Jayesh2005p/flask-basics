"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
Now we'll make our templates DYNAMIC by passing variables!

Learning Goals:
- Pass variables from Python to HTML templates
- Use {{ variable }} syntax in Jinja2
- Pass multiple variables including lists and dictionaries
- Use Jinja2 loops and conditionals

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Passing a single variable to the template
    The syntax is: render_template('file.html', variable_name=value)
    """
    # This variable will be available in the template as {{ name }}
    student_name = "Alex"

    return render_template('index.html', name=student_name)


@app.route('/profile')
def profile():
    """
    Passing multiple variables to the template
    You can pass as many as you need!
    """
    # All these will be available in the template
    user_data = {
        'name': 'Sarah',
        'age': 22,
        'course': 'Web Development',
        'is_enrolled': True
    }

    # You can pass individual values or unpack a dictionary
    return render_template('profile.html',
                           name=user_data['name'],
                           age=user_data['age'],
                           course=user_data['course'],
                           is_enrolled=user_data['is_enrolled'])


@app.route('/skills')
def skills():
    """
    Passing a list to the template
    We can loop through it in Jinja2!
    """
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']

    return render_template('skills.html', skills=programming_skills)


@app.route('/projects')
def projects():
    """
    Passing a list of dictionaries (common pattern!)
    This is how you'd display data from a database
    """
    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]

    return render_template('projects.html', projects=project_list)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 3.1: Add more data
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html
#
# Exercise 3.2: Conditional display
#   - In profile.html, show "Enrolled" or "Not Enrolled" based on is_enrolled
#   - Use {% if is_enrolled %} ... {% else %} ... {% endif %}
#
# Exercise 3.3: Create a grades page
#   - Create a new route /grades
#   - Pass a dictionary of subjects and grades
#   - Display them in a table using a for loop
#
# =============================================================================
