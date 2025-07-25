# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopLead(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link | None
		email: DF.Data
		full_name: DF.Data
		message: DF.TextEditor
		phone_number: DF.Phone | None
		shop: DF.Link
		status: DF.Literal["Contacted", "Rejected", "Rented", "Closed"]
	# end: auto-generated types
	pass
