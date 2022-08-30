import frappe
from frappe import _, _dict
from frappe.utils.data import today, date_diff, get_datetime_str
import json


def successful_login(login_manager):
    """
    on_login verify if site is not expired
    """
    local = _dict(frappe.get_site_config())
    active_users = local.get("active_users")
    allowed_users = local.get("allowed_users")
    user = login_manager.user

    if allowed_users and active_users and active_users > allowed_users and user != "Administrator":
        frappe.throw(_("User limit exceeded, Please contact admin."),
                     frappe.AuthenticationError)
