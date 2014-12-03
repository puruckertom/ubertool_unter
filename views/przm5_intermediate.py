import json
import logging
logger = logging.getLogger('PRZM5_int_Model')
from REST import rest_funcs
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import linksLeft
import os

@require_POST
def przm5IntermediatePage(request):
    data_all = json.loads(request.body)
    data_html = data_all["data_html"]
    logger.info(data_html)
    jid = str(data_all["jid"])
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'PRZM5'+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html',  {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':'przm5',
            'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {})
    html = html + data_html
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.update_html(html, jid, 'przm5')
    response = HttpResponse()
    response.write(html)
    return response
