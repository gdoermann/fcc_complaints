import datetime
import weakref

import os
from sodapy import Socrata
import phonenumbers

from fcc_complaints.config import parser

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version:
    VERSION = version.read()


class ApiFilter(object):

    def __init__(self, api, **filters):
        self.formatters = {
            'id': int,
            'ticket_created': self._floating_timestamp,
            'issue_date': self._floating_timestamp,
            'issue_time': self._time,
            'caller_id_number': self._phone_number,
            'advertiser_business_phone_number': self._phone_number,
        }
        self._api = weakref.ref(api)
        self.filters = filters

    def formatted(self):
        """
        Returns the properly formatted filters.
        :return: dict
        """
        filters = {}
        for k, v in self.filters.items():
            if k in self.formatters:
                v = self.formatters[k](v)
            filters[k] = v
        return filters

    @property
    def api(self):
        return self._api()

    def _floating_timestamp(self, ts):
        """
        Takes in a datetime.datetime object and formats it to 2016-05-25T09:33:48.000
        :param ts: Timestamp or datetime object
        :return: formatted timestamp
        """
        if isinstance(ts, datetime.datetime):
            ts = ts.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return str(ts)

    def _time(self, ts):
        """
        Takes in a datetime.datetime or a datetime.time object and formats it to 11:00 pm
        :param ts: Timestamp, datetime.time or datetime.datetime object
        :return: formatted timestamp
        """
        if isinstance(ts, datetime.datetime) or isinstance(ts, datetime.time):
            ts = ts.strftime('%H:%M %p').lower()
        return str(ts)

    def _phone_number(self, number):
        """
        The FCC data is formatted in NPA-NXX-YYYY.  This is not really a standard.
        The closest is the International format where we strip off the country code.

        :param number: A string of phonenumber.PhoneNumber object
        :return: formatted phone number (string)
        """
        if not isinstance(number, phonenumbers.PhoneNumber):
            number = phonenumbers.parse(number, self.api.region)
        return phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split()[-1]


class FccApi(object):
    """
    Wrapper for the FCC API.
    Docs: https://dev.socrata.com/foundry/opendata.fcc.gov/sr6c-syda
    """

    def __init__(self, app_token=None, username=None, password=None):
        self.app_token = app_token or parser['auth']['app_token'] or None
        self.username = username or parser['auth']['username'] or None
        self.password = password or parser['auth']['password'] or 'AFakePassword'
        if self.app_token:
            auth_details = {
                'username': self.username,
                'password': self.password,
            }
        else:
            auth_details = {}
        self.client = Socrata(parser['api']['DOMAIN'], self.app_token, **auth_details)
        self.resource = parser['api']['RESOURCE']
        self.region = parser['default']['REGION']

    def query(self, **kwargs):
        filter = ApiFilter(self, **kwargs)
        return self.client.get(self.resource, **filter.formatted())
