# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		is_published: DF.Check
		route: DF.Data | None
		shop_area: DF.Float
		shop_name: DF.Data
		shop_number: DF.Data
		shop_type: DF.Link
		status: DF.Literal["Available", "Occupied"]
	# end: auto-generated types
	
	def get_context(self, context):
		context.shop_type = frappe.db.get_value(
            "Shop Type", self.shop_type, "type", as_dict=True
        )
		# e8853e870bc75b6