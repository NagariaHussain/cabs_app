# Copyright (c) 2023, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def before_save(self):
		self.title = f"{self.make} {self.model}, {self.year}"
		# self.make + " " + self.model + ", " + self.year
