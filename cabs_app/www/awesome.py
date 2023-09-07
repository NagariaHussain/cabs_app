import frappe

def get_context(context):
    rides = frappe.get_all("Ride", fields=["driver", "vehicle"])
    context.rides = rides