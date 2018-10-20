from flask import Flask
import os
from instance.config import app_config


app = Flask(__name__, instance_relative_config=True)