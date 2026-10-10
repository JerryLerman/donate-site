# Import the Flask class (the core application object) and render_template,
# to allow for rendering HTML files from the templates/ folder.
from flask import Flask, render_template

# Import the Config class (from config.py), which holds app settings like
# the donation URLs and wallet addresses, typically loaded from the .env file.
from config import Config

# Create the Flask application instance.
# __name__ tells Flask where this module lives so it can locate templates
# and static files relative to it.
app = Flask(__name__) # __name___ will either be "__main__" (if run directly) or 
                      # "app" (if imported as a module).

# Load configuration values from the Config class into the app.
# This copies attributes like KOFI_URL, BTC_ADDRESS, etc. into app.config,
# so they can be read later via app.config["NAME"].
app.config.from_object(Config)

# Register a route: when a browser requests the "/" URL (the site root),
# Flask calls the index() function below and uses its return value as the response.
@app.route("/")
def index():
    # Render the "index.html" template (found in templates/) and pass in the
    # values the page needs. Each keyword argument becomes a variable available
    # inside the template's Jinja2 placeholders, e.g. {{ kofi_url }}.
    return render_template(
        "index.html",
        # Donation / support links pulled from the app's config.
        kofi_url=app.config["KOFI_URL"],
        patreon_url=app.config["PATREON_URL"],
        liberapay_url=app.config["LIBERAPAY_URL"],
        stripe_url=app.config["STRIPE_PAYMENT_URL"],
        # Crypto wallet addresses pulled from config.
        btc_address=app.config["BTC_ADDRESS"],
        eth_address=app.config["ETH_ADDRESS"],
    )


# This block only runs when the file is executed directly (e.g. `python app.py`),
# NOT when it's imported as a module (e.g. by a WSGI server like gunicorn).
if __name__ == "__main__":
    # Start the development server:
    # host="0.0.0.0"  -> listen on all network interfaces, so it's reachable
    #                    from other machines (not just localhost).
    # port=5000       -> serve on port 5000.
    # debug=False     -> keep the debugger/reloader OFF (safe for a real server).
    app.run(host="0.0.0.0", port=5000, debug=False)
