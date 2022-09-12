import frappe
import json
import subprocess
from frappe import _
from frappe.utils import get_site_name


def exec_cmd(cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            cwd=".",
                            )

    return_ = proc.wait()
    if return_:
        frappe.throw(f"Error in creating site: {proc.stderr.readline()}")

# User


def validate_user_limit(self, method):
    request = frappe.local.request
    local = frappe.get_site_config()

    site = local.get("site_name") or request.headers.get(
        "X-Frappe-Site-Name") or get_site_name(request.host)
    active_users = int(local.get("active_users"))
    allowed_users = int(local.get("allowed_users"))

    active_users = validate_users(self, allowed_users)
    exec_cmd(f"bench --site {site} set-config  site_name {site}")
    exec_cmd(f"bench --site {site} set-config  active_users {active_users}")


def validate_users(self, allowed_users):
    '''
    Validates and returns active users
    Params:
    1. self
    2. allowed_users => (int) => maximum users allowed
    '''
    # allowed user value type check
    if type(allowed_users) is not int:
        frappe.throw(
            _("Invalid value for maximum User Allowed limit. it can be a whole number only."), frappe.ValidationError)

    # Fetching all active users list
    filters = {
        'enabled': 1,
        "name": ['!=', 'Guest']
    }

    active_users = frappe.db.count('User', filters)

    # Users limit validation
    if allowed_users != 0 and active_users >= allowed_users:
        if not frappe.db.exists("User", {'name': self.name}):
            frappe.throw('Only {} active users allowed and you have {}. Please disable users or to increase the limit please contact sales'. format(
                allowed_users, active_users))

    return active_users
