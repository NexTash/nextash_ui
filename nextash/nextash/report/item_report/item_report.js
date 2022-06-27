// Copyright (c) 2022, Nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Report"] = {
	"filters": [
		{
			"fieldname": "attribute",
			"label": __("Attribute"),
			"fieldtype": "Link",
			"options": "Item Attribute",
		},
		{
			"fieldname": "variant_of",
			"label": __("Variant Of"),
			"fieldtype": "Link",
			"options":"Item",
		},
	]
};
