# This file is the entry point for the Flask application when run with a WSGI server.
# It imports the Flask app instance from app.py and runs it if executed directly.   

from app import app

if __name__ == "__main__":
    app.run()
