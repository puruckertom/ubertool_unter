"""
.. module:: ddm_tables
   :synopsis: A useful module indeed.
"""
from django.template import Context, Template
from django.utils.safestring import mark_safe
import time
import datetime
from django.template.loader import render_to_string
import ddm_parameters


def timestamp(ddm_obj="", batch_jid=""):
    if ddm_obj:
        st = datetime.datetime.strptime(ddm_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>Downstream Dilution Model (DDM) Beta<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_all(ddm_obj):
    html = """
        <table width="600" border="1">
          <tr>
          </tr>
        </table>
        <p>&nbsp;</p>                     
        """
    html = html + """
        <table width="600" border="1">
          <tr>
          </tr>          
        </table>
        """
    return html