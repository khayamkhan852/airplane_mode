# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlightCrewMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		crew_member: DF.Link
		crew_type: DF.Link | None
		email: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		phone: DF.Phone | None
		remarks: DF.TextEditor | None
	# end: auto-generated types
	pass
