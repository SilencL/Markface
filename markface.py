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
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(),'static','uploads')  # 文件储存地址
app.config['UPLOADED_PHOTOS_DEST'] = 'C:\Users\Silance\PycharmProjects\markFace\static\uploads'  # 文件储存地址
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join('static','uploads')  # 文件储存地址

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # 文件大小限制，默认为16MB


@app.route('/markapi', methods=['POST'])
def upload_file():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        # print filename
        file_url = photos.url(filename)
        # infile_path = os.path.join(os.getcwd(),'static','uploads',filename)
        infile_path = r'C:/Users/Silance/PycharmProjects/markFace/static/uploads/'+ filename
        # outfile_path = os.path.join(os.getcwd(),'static','markface',filename)
        outfile_path = r'C:/Users/Silance/PycharmProjects/markFace/static/markface/'+ filename

        tool_output_landmarks_image.main(infile_path,outfile_path)

        # return send_file('static/uploads/'+filename,mimetype='image/jpeg')
        return send_file(os.path.join('static','markface',filename),mimetype='image/jpeg')

    else:
        return u'参数错误'


if __name__ == '__main__':
    app.run()