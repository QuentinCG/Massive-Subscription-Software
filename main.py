#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Main software used to call functions for massive subscription

  Note: List_request.py must be filled with all request to send.
"""

__author__ = 'Quentin Comte-Gaz'
__email__ = "quentin@comte-gaz.com"
__license__ = "MIT License"
__copyright__ = "Copyright Quentin Comte-Gaz (2016)"
__python_version__ = "2.7+ and 3.+"
__version__ = "1.0 (2016/12/31)"
__status__ = "Usable for any project"

import logging, getopt, sys
import list_request, utils

def showHelp():
  print("Launch multiple subscription\r\n"
        +"\r\n"        
        +"Mandatory parameters:\r\n"
        +"-e or --email [email to spam]\r\n"
        +"\r\n"        
        +"Optional parameters:\r\n"
        +"-o or --pseudo [pseudo]\r\n"
        +"-s or --surname [surname]\r\n"
        +"-f or --forename [forename]\r\n"
        +"-p or --password [password]\r\n"
        +"-c or --postcode [postcode]\r\n"
        +"-d or --day [day]\r\n"
        +"-m or --month [month]\r\n"
        +"-y or --year [year]\r\n"
        +"\r\n"
        +"Get help:\r\n"
        +"-h or --help\r\n"
        +"\r\n")

def main():
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)

  email_initialized = False
  email = ""
  pseudo = "johndoe"
  surname = "Doe"
  forename = "John"
  password = "Azerty1234"
  postcode = "12345"
  day = "10"
  month = "10"
  year = "1980"

  # Get options
  try:
    opts = getopt.getopt(sys.argv[1:], "he:o:s:f:p:c:d:m:y:",
                         ["help", "email=", "pseudo=", "surname=", "forename=",
                          "password=", "postcode=", "day=", "month=",
                          "year="
                         ])[0]
  except getopt.GetoptError as err:
    logging.error(str(err))
    showHelp()
    sys.exit(1)

  # Show help (if requested)
  for o, a in opts:
    if o in ("-h", "--help"):
      showHelp()
      sys.exit(0)

  # Get parameters
  for o, a in opts:
    if o in ("-e", "--email"):
      logging.debug("Email: "+str(a))
      email = a
      email_initialized = True
      continue
    if o in ("-o", "--pseudo"):
      logging.debug("Pseudo: "+str(a))
      pseudo = a
      continue
    if o in ("-s", "--surname"):
      logging.debug("Surname: "+str(a))
      surname = a
      continue
    if o in ("-f", "--forename"):
      logging.debug("Forename: "+str(a))
      forename = a
      continue
    if o in ("-p", "--password"):
      logging.debug("Password: "+str(a))
      password = a
      continue
    if o in ("-c", "--postcode"):
      logging.debug("Postcode: "+str(a))
      postcode = a
      continue
    if o in ("-d", "--day"):
      logging.debug("Day: "+str(a))
      day = a
      continue
    if o in ("-m", "--month"):
      logging.debug("Month: "+str(a))
      month = a
      continue
    if o in ("-y", "--year"):
      logging.debug("Year: "+str(a))
      year = a
      continue

  if not email_initialized:
    logging.error("Email not initialized (--help for help)")
    sys.exit(2)

  for request in list_request.list_request:
    utils.sendRequest(request, email, pseudo, surname, forename,
                      postcode, password, day, month, year)

if __name__ == '__main__':
  main()
