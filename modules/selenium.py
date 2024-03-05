import selenium

def get_selenium_version():
    try:
        version = selenium.__version__
        return version
    except Exception as e:
        print("An error occurred:", e)
        return None