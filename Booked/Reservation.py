#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:28:16 2017

@author: fabiano
"""

import urllib 

url = 'https://testes.fearp.usp.br/reserva2/Web/Services/Authentication/Authenticate'

values = {'username' : '5219009',
          'password' : 'M5v-szy-vbH-YEc' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
request = urllib.request.Request(url, data)
try:
    response = urllib.request.urlopen(request)
    print(response.read())
except urllib.error.HTTPError as e:
    print ('No kittez. Got an error code:', e)

#Request
#{
#  "accessories": [
#    {
#      "accessoryId": 1,
#      "quantityRequested": 2
#    }
#  ],
#  "customAttributes": [
#    {
#      "attributeId": 2,
#      "attributeValue": "some value"
#    }
#  ],
#  "description": "reservation description",
#  "endDateTime": "2017-12-07T07:47:17-0700",
#  "invitees": [
#    1,
#    2,
#    3
#  ],
#  "participants": [
#    1,
#    2
#  ],
#  "recurrenceRule": {
#    "type": "daily|monthly|none|weekly|yearly",
#    "interval": 3,
#    "monthlyType": "dayOfMonth|dayOfWeek|null",
#    "weekdays": [
#      0,
#      1,
#      2,
#      3,
#      4,
#      5,
#      6
#    ],
#    "repeatTerminationDate": "2017-12-07T07:47:17-0700"
#  },
#  "resourceId": 1,
#  "resources": [
#    2,
#    3
#  ],
#  "startDateTime": "2017-12-07T07:47:17-0700",
#  "title": "reservation title",
#  "userId": 1,
#  "startReminder": {
#    "value": 15,
#    "interval": "hours or minutes or days"
#  },
#  "endReminder": null
#}