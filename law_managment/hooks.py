app_name = "law_managment"
app_title = "law managment"
app_publisher = "Asymptotes"
app_description = "it\'s an app to manage law cases "
app_email = "hussainqa4@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/law_managment/css/law_managment.css"
# app_include_js = "/assets/law_managment/js/law_managment.js"

# include js, css files in header of web template
# web_include_css = "/assets/law_managment/css/law_managment.css"
# web_include_js = "/assets/law_managment/js/law_managment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "law_managment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "law_managment/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "law_managment.utils.jinja_methods",
#	"filters": "law_managment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "law_managment.install.before_install"
# after_install = "law_managment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "law_managment.uninstall.before_uninstall"
# after_uninstall = "law_managment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "law_managment.utils.before_app_install"
# after_app_install = "law_managment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "law_managment.utils.before_app_uninstall"
# after_app_uninstall = "law_managment.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "law_managment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"law_managment.tasks.all"
#	],
#	"daily": [
#		"law_managment.tasks.daily"
#	],
#	"hourly": [
#		"law_managment.tasks.hourly"
#	],
#	"weekly": [
#		"law_managment.tasks.weekly"
#	],
#	"monthly": [
#		"law_managment.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "law_managment.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "law_managment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "law_managment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["law_managment.utils.before_request"]
# after_request = ["law_managment.utils.after_request"]

# Job Events
# ----------
# before_job = ["law_managment.utils.before_job"]
# after_job = ["law_managment.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"law_managment.auth.validate"
# ]

fixtures = [

    "Custom HTML Block",
   
    "Workspace",
    {
        "dt": "Custom Field",
        "filters": [
            [
                "dt", "=", "law cases"  # Use "%" as a wildcard to include all doctypes

            ]
        ]
    }
]
