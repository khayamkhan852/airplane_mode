# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class ShopContract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link | None
		amended_from: DF.Link | None
		contract_template: DF.Link | None
		contract_terms: DF.TextEditor
		end_date: DF.Date
		is_signed: DF.Check
		party_user: DF.Link | None
		rent_amount: DF.Currency
		security_deposit: DF.Currency
		shop: DF.Link
		signed_by_company: DF.Link | None
		signed_on: DF.Datetime | None
		signee: DF.Data | None
		start_date: DF.Date
		status: DF.Literal["Unsigned", "Active", "Expired"]
		tenant: DF.Link
	# end: auto-generated types
	pass

	def on_submit(self):
		shop = frappe.get_doc("Shop", self.shop)
		shop.status = "Occupied"
		shop.save()	

	def validate(self):
		self.validate_dates()
		self.update_contract_status()

	def before_submit(self):
		self.signed_by_company = frappe.session.user

	def before_update_after_submit(self):
		self.update_contract_status()
		
	def validate_dates(self):
		if self.end_date and self.end_date < self.start_date:
			frappe.throw(_("End Date cannot be before Start Date."))

	def update_contract_status(self):
		if self.is_signed:
			self.status = get_status(self.start_date, self.end_date)
		else:
			self.status = "Unsigned"

def get_status(start_date, end_date):
	"""
	Get a Contract's status based on the start, current and end dates

	Args:
	        start_date (str): The start date of the contract
	        end_date (str): The end date of the contract

	Returns:
	        str: 'Active' if within range, otherwise 'Expired'
	"""

	if not end_date:
		return "Active"

	start_date = getdate(start_date)
	end_date = getdate(end_date)
	now_date = getdate(nowdate())

	return "Active" if start_date <= now_date <= end_date else "Expired"


def update_status_for_contracts():
	"""
	Run the daily hook to update the statuses for all signed
	and submitted Contracts
	"""

	contracts = frappe.get_all(
		"Shop Contract",
		filters={
			"is_signed": True, 
			"docstatus": 1,
			"status": ["!=", "Expired"]
		},
		fields=["name", "start_date", "end_date"],
	)

	for contract in contracts:
		status = get_status(contract.get("start_date"), contract.get("end_date"))

		frappe.db.set_value("Contract", contract.get("name"), "status", status)

def send_rent_payment_reminder():
	shop_settings = frappe.get_single("Shop Settings")
	
	if shop_settings.disable_rent_reminders:
		return
	
	today = getdate()

	contracts = frappe.get_all(
        "Shop Contract",
        filters={"status": "Active", "docstatus": 1},
        fields=["name", "tenant", "shop", "rent_amount", "end_date"]
    )

	for contract in contracts:
		if contract.end_date and getdate(contract.end_date) < today:
			continue

		tenant_email = frappe.db.get_value("Tenant", contract.tenant, "email")
	
		if not tenant_email:
			continue

		frappe.sendmail(
            recipients=[tenant_email],
            subject="Monthly Rent Reminder - Please Ignore If Already Paid",
            message=f"""
            	Dear {contract.tenant},<br><br>
            	This is a friendly reminder that your monthly rent of <b>{contract.rent_amount}</b> 
            	for <b>Shop {contract.shop}</b> is due for <b>{today}</b>.<br><br>

            	<b>If you have already paid, please ignore this message.</b><br><br>

            	Thank you for your cooperation.<br><br>
            	Best regards,<br>
            	Airport Shop Management Team
            """
        )