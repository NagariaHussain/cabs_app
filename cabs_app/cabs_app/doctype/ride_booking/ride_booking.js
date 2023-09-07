// Copyright (c) 2023, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        if (frm.doc.status != "Rejected") {
            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")
        }

        if (frm.doc.status != "Accepted" && frm.doc.status != "Rejected") {
            frm.add_custom_button("Accept", () => {
                // show a dialog 
                const d = new frappe.ui.Dialog({
                    title: "Create a ride",
                    fields: [
                        {
                            label: "Driver",
                            fieldname: "driver",
                            fieldtype: "Link",
                            options: "Driver",
                            reqd: 1
                        }
                    ],
                    primary_action_label: "Create",
                    primary_action: (data) => {
                        frm.set_value("status", "Accepted");
                        frm.save();
                        
                        const driver_name = data.driver
                        const vehicle_name = frm.doc.vehicle

                        frappe.new_doc("Ride", {
                            "driver": driver_name,
                            "vehicle": vehicle_name
                        })

                        d.hide()
                    }
                })

                d.show()
                // that will prompt the user to select a driver
                // after the driver is selected, create a new "Ride"


                
            }, "Actions")
        }


	},
});
