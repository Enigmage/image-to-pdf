import imghdr 
from app import app

# Validating file type
def allowed_extensions(filename):
    return '.' in filename and filename.split(".")[-1].lower() in app.config['SAFE_EXTENSIONS'] # Make more secure

# Validating file content
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    img_format = imghdr.what(None, header)
    if not img_format:
        return None
    return f"{img_format if img_format !='jpeg' else 'jpg'}" # Return .extension jpeg uses .jpg so is an exception

