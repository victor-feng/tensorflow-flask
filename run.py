# from tensor_mnist import create_app
# from config import APP_ENV
from tensor_mnist import app

if __name__ == '__main__':
    # app = create_app(APP_ENV)
    app.run(host='0.0.0.0', debug=True)
