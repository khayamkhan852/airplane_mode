# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		default_shop_rent_amount: DF.Currency
		disable_rent_reminders: DF.Check
	# end: auto-generated types
	pass
