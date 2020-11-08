"""Server executable"""

from groceries.app import app
import logging
logger = app.logger
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
