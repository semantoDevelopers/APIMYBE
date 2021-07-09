from flask import Blueprint,request,current_app,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
from utils.modelsUtils import allowed_file
from utils.checkheaders import check_headers,RequestType
from utils.errors import * 
from dotenv import load_dotenv
from .db_models import DatabaseModel
import os

models = Blueprint('models',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']

db_models = DatabaseModel()



@models.route('/<filename>',methods=['GET'])
def get_models(filename):
    return send_from_directory(current_app.config['UPLOAD_MEDIA_FOLDER'],filename)

@models.route('/',methods=['POST'])
def post_models():
    print(request.files)
    check_result = check_headers(request,secret_key,RequestType.FORM)
    print(check_result)
    if(check_result==200):
        if 'file' not in request.files:
            return error400
        file = request.files['file']
        if file.filename == '':
            return error400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pathToSave = os.path.join(current_app.config['UPLOAD_MODEL_FOLDER'], filename)
            file.save(pathToSave)
            return db_models.register_model(url_for('models.get_models',filename=filename),os.path.getsize(pathToSave))
    else:
        
        if check_result==403:
            return error403
        elif check_result==400:
            return error400