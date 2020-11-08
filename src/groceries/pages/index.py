"""Index page"""

from groceries.app.base_app import app


@app.route('/')
def index():
    return """
    <p> Hello </p>
    <p><a href="/groceries">groceries</a></p>
    """