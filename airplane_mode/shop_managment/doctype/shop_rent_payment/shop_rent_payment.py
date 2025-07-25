# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class ShopRentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		payment_method: DF.Link | None
		posting_date: DF.Date
		rent_amount: DF.Currency
		rent_from: DF.Date
		rent_to: DF.Date
		shop: DF.Link
		shop_contract: DF.Link
		tenant: DF.Link
	# end: auto-generated types
	pass

	def validate(self):
		if self.rent_to < self.rent_from:
			frappe.throw(_("Rent To Date cannot be before Rent From Date."))


		overlapping = frappe.get_all(
        	"Shop Rent Payment",
        	filters={
            	"shop_contract": self.shop_contract,
            	"name": ["!=", self.name],
            	"rent_from": ["<=", self.rent_to],
            	"rent_to": [">=", self.rent_from],
        	},
        	pluck="name"
    	)

		if overlapping:
			frappe.throw("There is already a rent payment overlapping with this date range.")