"""
.. module:: superprzm_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def superprzmInputPage(request, model='', header='', formData=None):
    import superprzm_parameters
    
    # html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(superprzm_parameters.SuperprzmInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import superprzm_tooltips
        hasattr(superprzm_tooltips, 'tooltips')
        tooltips = superprzm_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html
