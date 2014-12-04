"""
.. module:: dust_batch_runner
   :synopsis: A useful module indeed.
"""

import dust_model
import os
import unittest
from StringIO import StringIO
import csv

# dust_obj = dust_model.dust(True, False, 'single',chemical_name, label_epa_reg_no, ar_lb, frac_pest_surface, dislodge_fol_res, bird_acute_oral_study, bird_study_add_comm,
#           low_bird_acute_ld50, test_bird_bw, mineau_scaling_factor, mamm_acute_derm_study, mamm_study_add_comm, mam_acute_derm_ld50, mam_acute_oral_ld50, test_mam_bw, None)

dust_obj = dust_model.dust(True, True, 'qaqc','Aliphatic Alcohols', '79038', '15.73', '0.3', '5', 'A304', 'NA',
          '4640', '1580', 1.15, 'B202', 'NA', '2000', '3920', '350', None)