# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

from ssl import Options
import frappe





def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data
def get_columns():
	columns = [ 
		{"fieldname": "employee_name", "label": "Full Name", "fieldtype": "Data"},
		{"fieldname": "employment_type", "label": "Employment Type", "fieldtype": "Select"},
		{"fieldname": "status", "label": "Status", "fieldtype": "Select"},
		{"fieldname": "date_of_birth", "label": "Date Of Birth", "fieldtype": "Date"},
		{"fieldname": "date_of_joining", "label": "Date Of Joining", "fieldtype": "Date"},
		{"fieldname": "employee_number", "label": "Employee Number", "fieldtype": "Date"},
		{"fieldname": "emergency_phone_number", "label": "Emergency Phone", "fieldtype": "Date"},


	]

	return columns
def get_conditions(filters):
	new_filters={}
	if filters.get("status==active"):
		new_filters['status']



		return new_filters



def get_data(filters):
	data=[]
	conditions=get_conditions(filters)
	field_name=['*']
	list_doc =frappe.db.get_list('Employee',filters=conditions,fields=field_name)
	for row in list_doc:
		data.append({
			"employee_name":row.employee_name,
			"employment_type":row.employment_type,
			"status":row.status,
			"date_of_birth":row.date_of_birth,
			"date_of_joining":row.date_of_joining,
			"employee_number":row.employee_number,
			"emergency_phone_number":row.emergency_phone_number,
		})
	return data