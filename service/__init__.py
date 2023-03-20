from flask import Flask
from service import routes
from .extensions import mail
 
def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)
  
    methods = ['GET', 'POST']

    app.add_url_rule("/", view_func=routes.foo)
    app.add_url_rule("/email", view_func=routes.email, methods = methods)

  
    app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '15948b25a40464'
    app.config['MAIL_PASSWORD'] = '3791137de16d49'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    
    mail.init_app(app)
    
    return app
