# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrewMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		crew_type: DF.Link
		email: DF.Data | None
		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		memeber_image: DF.AttachImage | None
		phone: DF.Phone | None
		status: DF.Literal["Available", "Assigned"]
	# end: auto-generated types
	pass

	def validate(self):
		if self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		else:
			self.full_name = self.first_name