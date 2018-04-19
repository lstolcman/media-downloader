from app import app

if __name__ == "__main__":

    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'],
            port=app.config['PORT'],
            ssl_context=app.config['SSL_CONTEXT'])

