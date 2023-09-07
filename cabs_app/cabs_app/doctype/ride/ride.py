# Copyright (c) 2023, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Ride(Document):
	def before_save(self):
		t = 0

		if self.items:
			for item in self.items:
				t += item.distance_in_km
			self.total_km = t
			self.total_amount = t * self.price_per_km



