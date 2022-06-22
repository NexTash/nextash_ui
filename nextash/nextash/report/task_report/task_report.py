# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from dataclasses import fields
import frappe
from frappe.utils import date_diff, nowdate


def execute(filters=None):
    columns, data = get_columns(), get_data(filters)

    return columns, data


# her report m  2 chizain hoti hain columns or data
def get_columns():
    columns = [
        {
            "fieldname": "name",
            "fieldtype": "Link",
            "label": "Task",
            "options": "Task",
            "width": 150,
        },
        {"fieldname": "subject", "fieldtype": "Data", "label": "Subject", "width": 200},
        {"fieldname": "status", "fieldtype": "Data", "label": "Status", "width": 100},
        {
            "fieldname": "priority",
            "fieldtype": "Data",
            "label": "Priority",
            "width": 80,
        },
        {
            "fieldname": "progress",
            "fieldtype": "Data",
            "label": "Progress (%)",
            "width": 120,
        },
        {
            "fieldname": "exp_start_date",
            "fieldtype": "Date",
            "label": "Expected Start Date",
            "width": 150,
        },
        {
            "fieldname": "exp_end_date",
            "fieldtype": "Date",
            "label": "Expected End Date",
            "width": 150,
        },
        {
            "fieldname": "completed_on",
            "fieldtype": "Date",
            "label": "Actual End Date",
            "width": 130,
        },
        {"fieldname": "type", "fieldtype": "link", "label": "Type", "width": 120},
        {
            "fieldname": "task_weight",
            "fieldtype": "float",
            "label": "Weight",
            "width": 120,
        },
        {
            "fieldname": "parent_task",
            "fieldtype": "link",
            "label": "Parent Task",
            "width": 120,
        },
    ]
    return columns


def get_data(filters):
    conditions = get_conditions(filters)
    data = []
    field_name = ['*']
    tasks = frappe.get_list(
        "Task", filters=filters, fields=field_name, order_by="creation"
    )
    for row in tasks:
        data.append(
            {
                "subjects": row.subjects,
                "type": row.type,
                "task_weight": row.task_weight,
                "parent_task": row.parnt_task,
                "exp_start_date": row.exp_start_date,
                "exp_end_date": row.exp_end_date,
                "status": row.status,
                "priority": row.priority,
                "completed_on": row.completed_on,
                "progress": row.progress,
            }
        )
    return data


def get_conditions(filters):
    field_name = ['*']
    task = frappe.get_list(
        "Task", filters=filters, fields=field_name, order_by="creation"
    )
    # if task.exp_end_date:
    #     if task.completed_on:
    #         task.delay = date_diff(task.completed_on, task.exp_end_date)
    #     elif task.status == "Completed":
    #         # task is completed but completed on is not set (for older tasks)
    #         task.delay = 0
    #     else:
    #         # task not completed
    #         task.delay = date_diff(nowdate(), task.exp_end_date)
    # else:
    #     # task has no end date, hence no delay
    #     task.delay = 0
