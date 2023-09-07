import frappe


@frappe.whitelist(allow_guest=True)
def get_balance(driver_name):
	amounts = frappe.get_all(
		"Ride", 
	    filters={"driver": driver_name}, 
		pluck="total_amount"
	)
	return sum(amounts)


@frappe.whitelist()
def secret_func():
	pass