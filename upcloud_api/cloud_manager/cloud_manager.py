from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from upcloud_api.base import BaseAPI
from upcloud_api.cloud_manager import ServerManager
from upcloud_api.cloud_manager import IPManager
from upcloud_api.cloud_manager import StorageManager
from upcloud_api.cloud_manager import FirewallManager

import base64


class CloudManager(BaseAPI, ServerManager, IPManager, StorageManager, FirewallManager):
	"""
	CloudManager contains the core functionality of the upcloud API library.
	All other managers are mixed in so code can be organized in corresponding submanager classes.
	"""

	def __init__(self, username, password):
		self.token = "Basic " + base64.b64encode( (username + ":" + password).encode() ).decode()

	def authenticate(self):
		return self.get_account()

	def get_account(self):
		return self.get_request("/account")

	def get_zones(self):
		return self.get_request("/zone")

	def get_timezones(self):
		return self.get_request("/timezone")

	def get_prices(self):
		return self.get_request("/price")

	def get_server_sizes(self):
		return self.get_request("/server_size")
