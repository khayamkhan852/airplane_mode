# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_flight_crew_member.airplane_flight_crew_member import AirplaneFlightCrewMember
		from frappe.types import DF

		airplane: DF.Link
		amended_from: DF.Link | None
		date_of_departure: DF.Date
		destination_airport: DF.Link
		destination_airport_code: DF.Data | None
		duration: DF.Duration
		gate_number: DF.Data
		is_published: DF.Check
		members: DF.Table[AirplaneFlightCrewMember]
		route: DF.Data | None
		source_airport: DF.Link
		source_airport_code: DF.Data | None
		status: DF.Literal["Scheduled", "Completed", "Cancelled"]
		time_of_departure: DF.Time
	# end: auto-generated types
	
	def on_submit(self):
		self.status = "Completed"
		crew_members_change_status(self.members, "Assigned")

	def on_update_after_submit(self):
		if self.has_value_changed('gate_number'):
			frappe.enqueue(
				"airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.update_gate_number",
				queue='short',
				flight_name=self.name, 
				gate_number=self.gate_number
			)		


	def on_update(self):
		if self.has_value_changed('gate_number'):
			frappe.enqueue(
				"airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.update_gate_number",
				queue='short',
				flight_name=self.name, 
				gate_number=self.gate_number
			)		

	def on_cancel(self):
		self.status = "Cancelled"
		crew_members_change_status(self.members, "Available")


def crew_members_change_status(members, status):
	if status not in ["Assigned", "Available"]:
		frappe.throw(f"Invalid status: {status}")

	for member in members:
		crew_member = frappe.get_doc("Crew Member", member.crew_member)
		if crew_member.status != status:
			crew_member.status = status
			crew_member.save()
			