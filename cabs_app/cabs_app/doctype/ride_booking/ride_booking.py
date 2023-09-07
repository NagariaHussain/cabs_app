# Copyright (c) 2023, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def on_update(self):
		doc_before_save = self.get_doc_before_save()
		if doc_before_save.audit_completed == 1 and self.audit_completed == 0:
			frappe.throw("You can't uncomplete an audit that has happened ")

