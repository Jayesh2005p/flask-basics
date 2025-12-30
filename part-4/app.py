"""
Part 4: Dynamic Routes - URL Parameters
========================================
Learn how to capture values from URLs and use them in your app!

Learning Goals:
- Create dynamic routes with <variable> syntax
- Use type converters (string, int, float)
- Build flexible URLs that respond to user input
- Understand URL building with url_for()

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    """Home page with links to demonstrate dynamic routes"""
    return render_template('index.html')


# =============================================================================
# DYNAMIC ROUTE WITH STRING PARAMETER
# =============================================================================
@app.route('/user/<username>')
def user_profile(username):
    """
    <username> captures any text from the URL
    Visit: /user/Alice, /user/Bob, /user/YourName
    """
    return render_template('user.html', username=username)


# =============================================================================
# DYNAMIC ROUTE WITH INTEGER PARAMETER
# =============================================================================
@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    <int:post_id> captures only integers from the URL
    Visit: /post/1, /post/42, /post/100
    /post/abc will return 404 (not found)
    """
    # Simulated post data (in real apps, this comes from a database)
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }

    # Get the post or None if not found
    post = posts.get(post_id)

    return render_template('post.html', post_id=post_id, post=post)


# =============================================================================
# MULTIPLE PARAMETERS IN ONE ROUTE
# =============================================================================
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    """
    Multiple dynamic segments in one URL
    Visit: /user/Alice/post/1
    """
    return render_template('user_post.html', username=username, post_id=post_id)


# =============================================================================
# ROUTE WITH OPTIONAL TRAILING SLASH
# =============================================================================
@app.route('/about/')
def about():
    """
    The trailing slash means both /about and /about/ work
    Without trailing slash, only /about works
    """
    return render_template('about.html')


# =============================================================================
# DEMONSTRATING url_for()
# =============================================================================
@app.route('/links')
def show_links():
    """
    url_for() generates URLs for your routes dynamically
    This is better than hardcoding URLs!
    """
    # Generate URLs using url_for
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================
