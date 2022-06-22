# Copyright (c) 2022, Nextash and contributors
# For license information, please see license.txt


from multiprocessing import Condition
from warnings import filters
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data,


def get_columns():
    columns= [
        {"fieldname": "item", "label": "Item", "fieldtype": "Data"},
        {"fieldname": "qty", "label": "Quantity", "fieldtype": "Float"},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date"},
		{"fieldname": "price", "label": "Price", "fieldtype": "Currency"},
        {"fieldname": "total_amount", "label": "Total Amount", "fieldtype": "link"},
		{"fieldname": "reciept", "label": "Reciept", "fieldtype": "Attach image"},
		{"fieldname": "description", "label": "Description", "fieldtype": "Text"},
       
    ]
    return columns
    
# def get_data(filters):
#     new_filter={}
#     data=[]
#     if filters.get("from_date") and filters.get("to_date") :
#         new_filter['date']=['between',[filters.get("from_date"),filters.get("to_date")]]
#     list_doc =frappe.db.get_list('Petty Cash',filters=new_filter,fields=['name'])
    
#     for row in list_doc:
#         row=frappe.get_doc('Petty Cash', row.name)
#         data.append({
#             "qty":row.qty,
#             "item":row.item,
#             "date":row.date,
#             "price":row.price,
#             "total_amount":row.total_amount,
#             "reciept":row.receipt,
#             "description":row.description,
#         })
    
    # return(data)
def get_condition(c_filter):
    new_filter={}
    
    if c_filter.get("from_date") and c_filter.get("to_date"):
        new_filter['date']=['between', [c_filter.get("from_date"),c_filter.get("to_date")]]
    return new_filter
def get_data(d_filter):
    data = []
    condition=get_condition(d_filter)
    field_name=['*']
    list_doc =frappe.db.get_list('Petty Cash',filters=condition,fields=field_name)
    for row in list_doc:
        data.append({
            "qty":row.qty,
            "item":row.item,
            "date":row.date,
            "price":row.price,
            "total_amount":row.total_amount,
            "reciept":row.receipt,
            "description":row.description,
        })
    
    return data