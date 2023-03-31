from __future__ import unicode_literals
import frappe
import json
from frappe.utils import floor, flt, today, cint
from frappe import _


def after_migrate():
    # Delete ERPNext Default Pages and Update Field labels
    delete_pages_and_update_field_references()


def delete_pages_and_update_field_references():
    """
    This function will 
        1. Remove default Home page and Blog Post created by erpnext
        2. Update label of section break in employee doctype
    """
    # Delete erpnext welcome page
    frappe.delete_doc_if_exists('Page', 'welcome-to-erpnext', force=1)

    # Update Welcome Blog Post
    if frappe.db.exists("Blog Post", "Welcome"):
        frappe.db.set_value("Blog Post", "Welcome", "content", "")

    if frappe.db.exists("Homepage", "Homepage"):
        frappe.db.set_value("Homepage", "Homepage", "description", "")

    q = """Update `tabDocField` set label='Employee User' where fieldname='erpnext_user' and parent='Employee'"""
    frappe.db.sql(q)