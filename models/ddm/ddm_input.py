"""
.. module:: ddm_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def ddmInputPage(request, model='', header='', formData=None):
    import ddm_parameters

    # html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(ddm_parameters.DdmInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import ddm_tooltips
        hasattr(ddm_tooltips, 'tooltips')
        tooltips = ddm_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html