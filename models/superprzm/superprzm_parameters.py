# -*- coding: utf-8 -*-
"""
.. module:: ddm_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation

class SuperprzmInp(forms.Form):
    chemical_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}))
    body_weight_of_bird = forms.FloatField(required=True,label='NEED TO GET INPUTS.')
