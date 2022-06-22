// Copyright (c) 2022, Nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Report"] = {
	"filters": [

						{
							"fieldname": "Status",
							"label": __("status"),
							"fieldtype": "Select"
						},
						
						{
							"fieldname": "employee_names",
							"label": __("Full Name"),
							"fieldtype": "Data"
						},
						
	]
};
