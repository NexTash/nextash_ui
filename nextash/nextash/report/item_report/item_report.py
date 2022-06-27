# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data
def get_columns(filters):
	columns=[ 
		{
			"fieldname": "item_code",
			"label": "Item Code",
			"fieldtype": "Link",
			"options":"Item"
		},
        {
			"fieldname": "item_name",
			"label": "Item Name",
			"fieldtype": "Data"
		},
		{
			"fieldname": "item_group",
			"label": "Item Group",
			"fieldtype": "Link",
			"options":"Item Group"
		},
		{
			"fieldname": "is_stock_item",
			"label": "Maintain Stock",
			"fieldtype": "Check"
		},
        {"fieldname": "stock_uom", "label": "UOM", "fieldtype":"Link", "options":"uom"},
        {"fieldname": "valuation_rate", "label": "Valuation Rate", "fieldtype": "Currency"},
        {"fieldname": "over_delivery_receipt_allowance", "label": "Over Delivery/Receipt Allowance (%)", "fieldtype": "Float"},
        {"fieldname": "over_billing_allowance", "label": "Over Billing Allowance (%)", "fieldtype": "Float"},
		{"fieldname": "variant_of", "label": "Variant Of", "fieldtype": "Link","options":"Item"},
		{"fieldname": "attribute", "label": "Attribute","fieldtype": "Link", "options": "Item Attribute"}
	]
	

	return columns

def get_data(filters):
	filter1={}
	data=[]
	field_name=['*']
	list_doc =frappe.db.get_list('Item',filters=filter1,fields=field_name)
	for row in list_doc:
		variants=[]
		attribute_filter={'parent':row.item_code}
		attributes=frappe.db.get_list('Item Variant Attribute',filters=attribute_filter,fields=field_name)
		for items in attributes:
			new_dic = row
			new_dic['varient_of'] = items.variant_of
			new_dic['attribute'] = items.attribute
			variants.append(new_dic)
		if variants==[]:
			del row['variant_of']
			variants.append(row)
		
		for varient in variants:
			if filters.get('attribute'):
				if varient.attribute!=filters.get('attribute'):
					continue
			if filters.get('variant_of'):
				if varient.variant_of!=filters.get('variant_of'):
					continue

			data.append({
				"item_code":varient.item_code,
				"item_name":varient.item_name,
				"item_group":varient.item_group,
				"stock_uom":varient.stock_uom,
				"valuation_rate":varient.valuation_rate,
				"over_delivery_receipt_allowance":varient.over_delivery_receipt_allowance,
				"over_billing_allowance":varient.over_billing_allowance,
				"variant_of":varient.variant_of,
				"attribute":varient.attribute,	
				"is_stock_item":varient.is_stock_item,	
			})
	return data