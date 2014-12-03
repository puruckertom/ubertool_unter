from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft
import os


def descriptionPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/'+model+'/'+model+'_text.txt'),'r')
    xx = text_file2.read()
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' Description'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'description'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': header+' Overview',
            'text_paragraph':xx})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''}) 
    
    response = HttpResponse()
    response.write(html)
    return response
