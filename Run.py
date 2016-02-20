import sys
import os
import bottle
from bottle import request, response
from bottle import route, run, template
from bottle import static_file,redirect



@route('/hello')
def index():
    #return template('<b>Hello World!!</b>')
    return template('index.tpl')


@route('/upload',method='POST')
def get_image():
    category=request.forms.get('category')
    upload=request.files.get('upload')
    #print upload.filename
    name, ext= os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'
    #save the image to directory which can be processed by our function
    saveto=os.getcwd()+'/views/';
    
    print "----",saveto
    upload.save(saveto,overwrite=True) #this function automatically appends the filename
    #call function with filename
    #vehicle=get_number(upload.filename)
    #vehicle stores the req vehicle no. in string form
    #save the region extracted  images as upload.filename+plate_region
    #also save the 
    #upload='img_20150614_191323.jpg'
    #show_image(upload.filename)
    #redirect("/show")
    image_name=upload.filename
    return template('magic.tpl',image=image_name)
    #return 'OK your image is being processed'


'''@route('/show/<image>')
def show_image(image):
    #image_name='img_20150614_191323.jpg'
    return template('magic.tpl',image)'''

@route(os.getcwd()+'/views/<image>')
def serve_images(image):
    return static_file(image,root=os.getcwd()+'/views/')



run(host='localhost',port=8080,debug=True)

