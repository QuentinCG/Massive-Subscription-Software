#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Utility functions for massive subscription software
"""

__author__ = 'Quentin Comte-Gaz'
__email__ = "quentin@comte-gaz.com"
__license__ = "MIT License"
__copyright__ = "Copyright Quentin Comte-Gaz (2016)"
__python_version__ = "2.7+ and 3.+"
__version__ = "1.0 (2016/12/31)"
__status__ = "Usable for any project"

import logging
import requests

TYPE_POST = "post"
TYPE_GET = "get"

# Mandatory fields
CONST_REQUEST_TYPE = "request_type"
CONST_POST_PAGE = "post_page"
CONST_POST_EMAIL_NAME = "email_name"

# Optional fields
CONST_SIGNUP_PAGE = "signup_page"
CONST_POST_CONFIRM_EMAIL_NAME = "confirm_email_name"
CONST_POST_PSEUDO = "pseudo"
CONST_POST_SURNAME = "surname"
CONST_POST_FORENAME = "forename"
CONST_POST_POSTCODE = "postcode"
CONST_POST_PASSWORD = "password"
CONST_POST_CONFIRM_PASSWORD = "confirm_password"
CONST_POST_ADDITIONAL_DATA = "data"
CONST_POST_DAY = "day"
CONST_POST_MONTH = "month"
CONST_POST_YEAR = "year"

def sendRequest(request, email_name, pseudo="johndoe", surname="Doe", forename="John",
                postcode="123456", password="azerty123", day="10", month="10", year="1985"):
  """Send post/get request
  Keyword arguments:
    request -- (dict) All info for the request
  """
  _data = {}

  # Mandatory fields
  _data[request[CONST_POST_EMAIL_NAME]] = email_name
  # Optional fields
  keys = request.keys()
  if CONST_SIGNUP_PAGE in keys:
    logging.debug("Signup page: " + request[CONST_SIGNUP_PAGE])
  if CONST_POST_ADDITIONAL_DATA in keys:
    _data.update(request[CONST_POST_ADDITIONAL_DATA])
  if CONST_POST_PSEUDO in keys:
    _data[request[CONST_POST_PSEUDO]] = pseudo
  if CONST_POST_SURNAME in keys:
    _data[request[CONST_POST_SURNAME]] = surname
  if CONST_POST_FORENAME in keys:
    _data[request[CONST_POST_FORENAME]] = forename
  if CONST_POST_POSTCODE in keys:
    _data[request[CONST_POST_POSTCODE]] = postcode
  if CONST_POST_CONFIRM_EMAIL_NAME in keys:
    _data[request[CONST_POST_CONFIRM_EMAIL_NAME]] = email_name
  if CONST_POST_PASSWORD in keys:
    _data[request[CONST_POST_PASSWORD]] = password
  if CONST_POST_CONFIRM_PASSWORD in keys:
    _data[request[CONST_POST_CONFIRM_PASSWORD]] = password
  if CONST_POST_DAY in keys:
    _data[request[CONST_POST_DAY]] = day
  if CONST_POST_MONTH in keys:
    _data[request[CONST_POST_MONTH]] = month
  if CONST_POST_YEAR in keys:
    _data[request[CONST_POST_YEAR]] = year

  logging.debug("Data to send: " + str(_data))

  if request[CONST_REQUEST_TYPE] == TYPE_POST:
    r = requests.post(request[CONST_POST_PAGE], data = _data)
    logging.debug("Result: " + str(r.status_code) + " " + str(r.reason))
    logging.debug("Page result: " + r.text[:10000])
  elif request[CONST_REQUEST_TYPE] == TYPE_GET:
    r = requests.get(request[CONST_POST_PAGE], params = _data)
    logging.debug("Result: " + str(r.status_code) + " " + str(r.reason))
    logging.debug("Page result: " + r.text)
  else:
    logging.error("[sendRequest] WRONG TYPE: " + str(request_type))
