// Copyright (c) 2024, us and contributors
// For license information, please see license.txt

frappe.ui.form.on("Item Borrowing", {
	refresh(frm) {
        if ( frm.doc.docstatus == 1 && frm.doc.status == "In Progress" ) {
            frm.add_custom_button(__(" Returned "), function(){
                frm.set_value("status", "Returned")
                frm.save("Update")
        });

        frm.add_custom_button(__(" Extend Borrowing "), function(){
            
            frappe.prompt({
                label: __("Please Enter Days"),
                fieldname: "days",
                fieldtype: "Int"
            }, (values) => {
                console.log(values)
            },);
            // frm.set_value("status", "Returned Period")
            frm.save("Update")
        });
        }
	},
},);
