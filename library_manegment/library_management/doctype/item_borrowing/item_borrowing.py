# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date, now



class ItemBorrowing(Document):
    def validate (self):
        pass

    def before_submit (self):

        # frappe.db.set_value("Item Borrowing", self.name, "status", "In Progress")
        day_no = frappe.get_value ( "Faculty Library Setting", self.company, "max_delay_period")
        self.date_of_borrowing = frappe.utils.nowdate()
        self.expected_retrieval_date = add_to_date(self.date_of_borrowing, days=day_no)

        library_setting = frappe.get_doc("Faculty Library Setting", self.company)
        available_books_no = library_setting.available_books_no

        maximum_no = 10

        for row in available_books_no:
            if row.role == self.role:
                maximum_no = row.max_books_no

        person_inprogress_borrowing = frappe.get_all ("Item Borrowing", filters = {
            "person": self.person, 
            "role": self.role,
            "status": "In Progress", 
            "docstatus": 1
        })

        if len(person_inprogress_borrowing) >= maximum_no:
            frappe.throw("تجاوز الحد المسموح")
        else:
            self.status = "In Progress"


