import frappe
import random
import json

@frappe.whitelist(allow_guest=True)
def custom_generate_keys(user):
    """
    generate api key and api secret

    :param user: str
    """
    frappe.only_for("System Manager")
    user_details =frappe.get_doc("User", user)
    api_secret = frappe.generate_hash(length=15)
    # if api key is not set generate api key
    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key
    user_details.api_secret = api_secret
    user_details.save()

    return {"api_secret": api_secret,
            "api_key": user_details.api_key
            }

@frappe.whitelist(allow_guest=True)
def get_current_session():
    frappe.response["message"] = frappe.session