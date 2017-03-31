#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2017/3/24 16:04
@author: Silence
'''
import os
from flask import Flask, request,send_file
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class
import tool_output_landmarks_image
import time

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'  # 文件储存地址

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # 文件大小限制，默认为16MB


@app.route('/', methods=['POST'])
def upload_file():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_url = photos.url(filename)

        tool_output_landmarks_image.main('static/uploads/'+filename,'static/markface/'+filename)

        return send_file('static/markface/'+filename, mimetype='image/jpg')



if __name__ == '__main__':
    app.run()