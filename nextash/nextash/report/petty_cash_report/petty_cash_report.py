# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt


import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_columns():
    columns= [
        {"fieldname": "item", "label": "Item", "fieldtype": "Data"},
        {"fieldname": "qty", "label": "Quantity", "fieldtype": "Float"},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date"},
		{"fieldname": "price", "label": "Price", "fieldtype": "Currency"},
		{"fieldname": "reciept", "label": "Reciept", "fieldtype": "Attach image"},
		{"fieldname": "description", "label": "Description", "fieldtype": "Text"},
       
    ]
    return(columns)
    
def get_data(filters):
    new_filter={}
    data=[]
    if filters.get("from_date") and filters.get("to_date") :
        new_filter['date']=['between',[filters.get("from_date"),filters.get("to_date")]]
    list_doc =frappe.db.get_list('Petty Cash',filters=new_filter,fields=['name'])
    
    for row in list_doc:
        petty_doc=frappe.get_doc('Petty Cash', row.name)
        data.append({
            "qty":petty_doc.qty,
            "item":petty_doc.item,
            "date":petty_doc.date,
            "price":petty_doc.price,
            "reciept":petty_doc.receipt,
            "description":petty_doc.description,
        })
    
    return(data)