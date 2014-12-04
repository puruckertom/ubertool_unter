from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def ddmOutputPage(request):
    import ddm_model
      

    ddm_obj = ddm_model.DDM("single")  

    return ddm_obj
    