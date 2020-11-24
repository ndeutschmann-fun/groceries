"""Index page"""

from groceries.app.base_app import app


@app.route('/')
def index():
    # @todo: already have the possibility to add to the grocery list.
    return """
    <p> Hello </p>
    <p><a href="/groceries">Update the grocery list</a></p>
    <p><a href="/going_shopping">Let's go shopping!</a></p>
    """