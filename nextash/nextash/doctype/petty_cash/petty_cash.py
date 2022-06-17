# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PettyCash(Document):
	def on_submit(self):
		
		if self.amount>self.total_amount:
			frappe.throw("Amount increased kindly contact with admin to allow you more petty")
		
		doc = frappe.get_doc( 'Generate Petty Cash',  self.petty_document)
		remaining=self.total_amount-self.amount

		if remaining<0:
			frappe.throw("You have Not Enough Petty Amount")
		doc.db_set('remaining_amount', remaining)	
		doc.save()