#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  List of request to send (must be edited)
"""

import utils

list_request = []

# Example of request to add
list_request.append({
  utils.CONST_REQUEST_TYPE: utils.TYPE_POST,
  utils.CONST_POST_PAGE: 'http://www.example.com/subscribe.php',
  utils.CONST_POST_PSEUDO: 'pseudo',
  utils.CONST_POST_EMAIL_NAME: 'email_address',
  utils.CONST_POST_PASSWORD: 'password',
  utils.CONST_POST_ADDITIONAL_DATA: {'dummy_param': '27', 'sex': 'male', 'description_of_yourself': 'blablabla', 'action': 'subscribe'}
})

# For each request, here is the full list of parameter you may add:
# Mandatory fields: CONST_REQUEST_TYPE, CONST_POST_PAGE, CONST_POST_EMAIL_NAME
# Optional fields: CONST_SIGNUP_PAGE, CONST_POST_CONFIRM_EMAIL_NAME, CONST_POST_PSEUDO, CONST_POST_SURNAME,
#                  CONST_POST_FORENAME, CONST_POST_POSTCODE, CONST_POST_PASSWORD, CONST_POST_CONFIRM_PASSWORD,
#                  CONST_POST_DAY, CONST_POST_MONTH, CONST_POST_YEAR
# Optional field used to add other fields: CONST_POST_ADDITIONAL_DATA
