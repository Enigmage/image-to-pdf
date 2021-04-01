import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

if not os.path.exists(os.path.join(basedir, 'input')):
    os.makedirs(os.path.join(basedir, 'input'))
    
if not os.path.exists(os.path.join(basedir, 'output')):
    os.makedirs(os.path.join(basedir, 'output'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SAFE_EXTENSIONS = set(["jpg", "png", "jpeg"])
    MAX_CONTENT_LENGTH = 80*1024*1024
    UPLOAD_PATH = os.path.join(basedir, 'input')
    DOWNLOAD_PATH = os.path.join(basedir, 'output')


