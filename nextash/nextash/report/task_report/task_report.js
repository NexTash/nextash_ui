// Copyright (c) 2022, Nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Task Report"] = {
	"filters": [
				{
					"fieldname": "from_date",
					"label": __("From Date"),
					"fieldtype": "Date"
				},
				{
					"fieldname": "to_date",
					"label": __("To Date"),
					"fieldtype": "Date"
				},
				{
					"fieldname": "priority",
					"label": __("Priority"),
					"fieldtype": "Select",
					"options": ["", "Low", "Medium", "High", "Urgent"]
				},
				{
					"fieldname": "status",
					"label": __("Status"),
					"fieldtype": "Select",
					"options": ["", "Open", "Working","Pending Review","Overdue","Completed"]
				},
			],
	
};
