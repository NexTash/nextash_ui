# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PettyCash(Document):
	def validate(self):
		if self.amount > 1000:
			frappe.throw("amount can not be greater than 1000")
		
		self.amount = self.amount * 2