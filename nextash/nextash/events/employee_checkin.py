from pickle import FALSE
from pydoc import Doc
import frappe
from frappe.utils import today


@frappe.whitelist()
def employee_checkin():
    """
    This function will mark the attendence of the employee. It will not receive any
    parameter.
    """

    # Getting session user

    user = frappe.session.user

    # Getting user roles
    roles = frappe.get_roles(frappe.session.user)

    # If User doesnot have Employee role OR He is and Administrator the sytem will show message.
    if "Employee" not in roles or "Administrator" in roles:
        frappe.throw("This is not an Employee")

    employee_name = frappe.db.get_value("Employee", {"user_id": user}, "name")
    emp_checkin_doc = frappe.get_doc(
        {
            "doctype": "Employee Checkin",
            "employee": employee_name,
            "log_type": "IN",
        }
    )
    emp_checkin_doc.insert()

    return emp_checkin_doc


@frappe.whitelist()
def employee_checkout():
    """
    This function will mark the attendence of the employee. It will not receive any
    parameter.
    """

    # Getting session user
    user = frappe.session.user

    # Getting user roles
    roles = frappe.get_roles(frappe.session.user)

    # If User doesnot have Employee role OR He is and Administrator the sytem will show message.
    if "Employee" not in roles or "Administrator" in roles:
        frappe.throw("This is not an Employee")

    employee_name = frappe.db.get_value("Employee", {"user_id": user}, "name")
    emp_checkin_doc = frappe.get_doc(
        {
            "doctype": "Employee Checkin",
            "employee": employee_name,
            "log_type": "OUT",
        }
    )
    emp_checkin_doc.insert()

    return emp_checkin_doc


@frappe.whitelist()
def check_status():
    # Getting session user

    user = frappe.session.user

    # Getting user roles
    roles = frappe.get_roles(frappe.session.user)

    # If User doesnot have Employee role OR He is and Administrator the sytem will show message.
    if "Employee" not in roles or "Administrator" in roles:
        return "employee not found"

    employee_name = frappe.db.get_value("Employee", {"user_id": user}, "name")
    employee_checkin = frappe.db.exists("Employee Checkin", {"employee": employee_name})

    if employee_checkin:
        check_in = frappe.get_all("Employee Checkin", {"employee": employee_name})
        check_in = check_in[-1]

        check_in = frappe.get_doc("Employee Checkin", check_in.name)

        if check_in.log_type == "IN":
            return True
        else:
            return False
    return False


@frappe.whitelist()
def check_daily():
    employee = frappe.db.get_list("Employee")

    for row in employee:
        employee_checkin = frappe.db.exists("Employee Checkin", {"employee": row.name})

        if employee_checkin:
            check_in = frappe.get_all(
                "Employee Checkin", {"employee": row.name}, ["log_type", "date"]
            )
            check_in = check_in[-1]
            if check_in.log_type == "OUT" and check_in.date == today():
                break
            else:
                emp_checkin_doc = frappe.get_doc(
                    {
                        "doctype": "Employee Checkin",
                        "employee": row.name,
                        "log_type": "OUT",
                    }
                )
                emp_checkin_doc.insert()
    frappe.db.commit()
