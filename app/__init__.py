from flask import Flask

import os
from instance.config import app_config
from app.api.V1.views.product_views import product
from app.api.V1.views.sale_views import sale

def create_app(config_name="development"):
    '''configuring the Flask App'''
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])


    app.register_blueprint(product)
    app.register_blueprint(sale)
  
    return app

