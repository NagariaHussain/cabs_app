# Copyright (c) 2023, BWH and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	rides = frappe.get_all("Ride", fields=["vehicle.make as make", "total_amount"])

	revenue_by_make = {}

	for ride in rides:
		if ride.make in revenue_by_make:
			revenue_by_make[ride.make] = revenue_by_make[ride.make] + ride.total_amount
		else:
			revenue_by_make[ride.make] = ride.total_amount

	columns = [
		{"label": "Make", "fieldname": "make", "fieldtype": "Data"},
		{"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"},
	]

	# {BMW: 27392} => {"make": "BMW", "amount": 27392}
	data = []

	for make, revenue in revenue_by_make.items():
		data.append({"make": make, "revenue": revenue})

	chart = {
		"type": "pie",
		"data": {
			"labels": [d["make"] for d in data],
			"datasets": [{"name": "Revenue By Make","values": [d["revenue"] for d in data]}],
		},
	}

	return columns, data, None, chart, None
