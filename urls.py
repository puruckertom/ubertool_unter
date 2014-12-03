#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()


# All view functions here must be in '/views/views.py'
urlpatterns = patterns('views',
    # url(r'^docs/', include('docs.urls')),
    (r'^$', 'landing.unterLandingPage'),
    (r'^unter/?$', 'landing.unterLandingPage'),
    (r'^unter/(?P<model>.*?)/description/?$', 'description.descriptionPage'),
    (r'^unter/(?P<model>.*?)/input/?$', 'input.inputPage'),
    (r'^unter/(?P<model>.*?)/output/?$', 'output.outputPage'),
    (r'^unter/(?P<model>.*?)/algorithms/?$', 'algorithms.algorithmPage'),
    (r'^unter/(?P<model>.*?)/references/?$', 'references.referencesPage'),
    (r'^unter/(?P<model>.*?)/batchinput/?$', 'batch.batchInputPage'),
    (r'^unter/(?P<model>.*?)/batchoutput/?$', 'batch.batchOutputPage'),
    (r'^unter/(?P<model>.*?)/qaqc/?$', 'qaqc.qaqcPage'),
    (r'^unter/(?P<model>.*?)/history/?$', 'history.historyPage'),
    (r'^unter/.*?/history_revisit\.html$', 'history.historyPageRevist'),
    (r'^unter/(?P<model>.*?)/pdf/?$', 'generateReport.pdfReceiver'),
    (r'^unter/(?P<model>.*?)/html/?$', 'generateReport.htmlReceiver'),
    (r'^unter/docs/?$', 'misc.docsRedirect'),
    # (r'^unter/.*?/przm5_intermediate\.html', 'przm5_intermediate.przm5IntermediatePage'),
    (r'^unter/(?P<model>.*?)/?$', 'description.descriptionPage'),
    (r'^unter_index\.html$', 'landing.unterLandingPage'),                        #Legacy links
    (r'^(?P<model>.*?)_description\.html$', 'description.descriptionPage'),  #Legacy links
    (r'^(?P<model>.*?)_input\.html$', 'input.inputPage'),                    #Legacy links
    (r'^(?P<model>.*?)_output\.html$', 'output.outputPage'),                 #Legacy links
    (r'^(?P<model>.*?)_algorithms\.html$', 'algorithms.algorithmPage'),      #Legacy links
    (r'^(?P<model>.*?)_references\.html$', 'references.referencesPage'),     #Legacy links
    (r'^(?P<model>.*?)_batchinput\.html$', 'batch.batchInputPage'),          #Legacy links
    (r'^(?P<model>.*?)_batchoutput\.html$', 'batch.batchOutputPage'),        #Legacy links
    (r'^(?P<model>.*?)_qaqc\.html$', 'qaqc.qaqcPage'),                       #Legacy links
    (r'^(?P<model>.*?)_history\.html$', 'history.historyPage'),              #Legacy links
    # url(r'^admin/', include(admin.site.urls)),
)

# 404 Error view (file not found)
handler404 = 'views.misc.fileNotFound'
# 500 Error view (server error)
handler500 = 'views.misc.fileNotFound'
# 403 Error view (forbidden)
handler403 = 'views.misc.fileNotFound'

