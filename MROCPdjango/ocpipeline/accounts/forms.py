#!/usr/bin/python

# forms.py
# Created by Disa Mhembere on 2013-03-19.
# Email: dmhembe1@jhu.edu
# Copyright (c) 2013. All rights reserved.

# File to hold forms associated with authentication

from django import forms
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationForm

attrs_dict = {'class': 'required'}

class MROCPRegistrationForm(RegistrationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    firstname = forms.RegexField(regex=r'^[A-Za-z]+(\-[A-Za-z])*$',
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Firstname"),
                                error_messages={'invalid': _("This value may contain only letters and the - character.")})

    lastname = forms.RegexField(regex=r'^[A-Za-z]+(\-[A-Za-z])*$',
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Lastname"),
                                error_messages={'invalid': _("This value may contain only letters and the - character.")})
