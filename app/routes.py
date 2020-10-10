from flask import url_for, render_template, request, flash, redirect, send_file, current_app
from werkzeug.utils import secure_filename
import os
from app import app, utils, validators 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if(request.method == 'POST'):
        # If there are no files uploaded.
        if('files[]' not in request.files):
            flash(u'No files uploaded', 'nothing')
            return redirect(request.url)
        res_name = request.form['pdfname']
        images = request.files.getlist('files[]') # List containing each image wrapped in FileStorage Class
        filenames = [] # store filenames for later use (Deleting files etc)
        for img in images:
            if img and validators.allowed_extensions(img.filename) and \
                    img.filename.split(".")[-1] == validators.validate_image(img.stream):

                image_name = secure_filename(img.filename)
                img.save(os.path.join(app.config['UPLOAD_PATH'], image_name))
                filenames.append(image_name)

        try:
            utils.image_to_pdf_normal(filenames, res_name)
            utils.remove_files(filenames)
            return render_template('download.html', filename = f"{res_name}.pdf")
        except:
            return "There was some error in generating pdf!!" # Improve error handling


@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['DOWNLOAD_PATH'], filename)
    file_stream = open(file_path, 'rb')

    def stream_and_remove():
        yield from file_stream
        file_stream.close()
        os.remove(file_path)
        redirect('/')

    return current_app.response_class(
        stream_and_remove(),
        headers = {'Content-Disposition':'attachment', 'filename':filename}
    )
#    return send_file(os.path.join(app.config['DOWNLOAD_PATH'],filename), as_attachment=True)

