# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company_name: DF.Data | None
		email: DF.Data
		name1: DF.Data
		phone_number: DF.Phone | None
	# end: auto-generated types
	pass
