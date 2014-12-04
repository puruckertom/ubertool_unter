"""
.. module:: sam_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('SAM Model')
import os
import requests
from collections import OrderedDict
import datetime

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


def get_jid(run_type):
    """
    Generate job ID and send inputs to JSON-RPC model server
    """
    all_dic = {}
    # data = json.dumps(all_dic)
    # logger.info(data)
    jid = rest_funcs.gen_jid()
    # jid = "TEMP0000"
    # url=url_part1 + '/sam/' + jid 

    # response = requests.post(url=url, data=data, headers=http_headers, timeout=60)
    # output_val = json.loads(response.content)['result']
    output_val = ""
    return(jid, output_val)

# Dummy class

class DDM(object):
	def __init__(self, run_type):
		self.run_type = run_type

		# self.final_res = get_jid(self.run_type)

  #       self.jid = self.final_res[0]

  		self.jid = get_jid(self.run_type)[0]