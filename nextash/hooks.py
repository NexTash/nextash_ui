from . import __version__ as app_version

app_name = "Nextash"
app_title = "Nextash"
app_publisher = "Nextash"
app_description = "Nextash"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@nextash.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_logo_url = "/assets/nextash/images/nextash-logo.png"
website_context = {
    "favicon": "/assets/nextash/images/nextash.png",
    "splash_image": "/assets/nextash/images/nextash.png",
}
# include js, css files in header of desk.html
# app_include_css = "/assets/nextash/css/nextash.css"
# app_include_js = "/assets/nextash/js/nextash.js"
app_include_css = "/assets/nextash/css/theme.css"
app_include_js = ["/assets/js/nextash.min.js"]
# include js, css files in header of web template
# web_include_css = "/assets/nextash/css/nextash.css"
# web_include_js = "/assets/nextash/js/redirect.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nextash/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page

# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice": "public/js/sales_invoice.js",
    "Task": "public/js/task.js",
    "employee_checkin":"public/js/employee_checkin.js"
}
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
on_session_creation = 'nextash.events.employee_checkin.employee_checkin'
on_logout='nextash.events.employee_checkin.employee_checkout'
# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nextash.install.before_install"
# after_install = "nextash.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nextash.uninstall.before_uninstall"
# after_uninstall = "nextash.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nextash.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     'User': {
#         'validate': 'nextash.quota.validate_user_limit',
#     },
# }
# Scheduled Tasks
# # ---------------

scheduler_events = {
    "cron": {
        "0/1 * * * *": [
            "nextash.events.employee_checkin.cron_each_five",
        ],
    },
    "daily": ["nextash.events.employee_checkin.check_daily"]
    # 	"hourly": [
    # 		"nextash.tasks.hourly"
    # 	],
    # 	"weekly": [
    # 		"nextash.tasks.weekly"
    # 	]
    # 	"monthly": [
    # 		"nextash.tasks.monthly"
    # 	]
}

fixtures = [
    {"dt": "Custom Field", "filters": [["name", "in", ["Employee Checkin-date"]]]},
]

# Testing
# -------

# before_tests = "nextash.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nextash.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nextash.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {"doctype": "{doctype_4}"},
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nextash.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
