# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Srudent(Document):
    # def onload(self):
        # doc = frappe.get_doc("Student", "St001")
        # doc.cls = "10th"
        # doc.save()

   def before_insert(self):
      if self.name == "St004":
            doc = frappe.get_doc("Student", "St004")
            doc.cls = "10th"
            doc.save()