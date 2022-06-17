# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GeneratePettyCash(Document):
	def on_submit(self):
		doc = frappe.get_doc( 'Generate Petty Cash',  self.name)
		doc.db_set('remaining_amount',doc.amount1)
		doc.save