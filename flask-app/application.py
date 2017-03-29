from app_name import get_app

# Get App
application = get_app(__name__)

if __name__ == "__main__":
    # Start App
    application.debug = True
    application.run()
