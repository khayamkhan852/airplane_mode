# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
		from frappe.types import DF

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport_code: DF.Data
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		gate_number: DF.Data | None
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.Data
		status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types
	
	def validate(self):
		self.prevent_new_ticket_when_capaicity_is_full()

		unique_adon_items = set()
		for add_on in self.add_ons:	
			if add_on.airplane_ticket_add_on_type in unique_adon_items:
				frappe.throw("Duplicate add-on type found: {0}".format(add_on.airplane_ticket_add_on_type))
			
			unique_adon_items.add(add_on.airplane_ticket_add_on_type)

		total_add_on_amount = 0
		
		for add_on in self.add_ons:
			total_add_on_amount += add_on.amount

		self.total_amount = self.flight_price + total_add_on_amount

	def prevent_new_ticket_when_capaicity_is_full(self):
		total_tickets = frappe.db.count('Airplane Ticket', {'docstatus': '1', 'flight': self.flight})
		airplane_flight = frappe.get_doc('Airplane Flight', self.flight)
		airplane = frappe.get_doc('Airplane', airplane_flight.airplane)

		if total_tickets >= airplane.capacity:
			frappe.throw(_("Flight {0} is fully booked. Cannot create new ticket.".format(airplane_flight.name)))

	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw('You cannot board the flight unless the status is "Boarded".')
	
	def before_insert(self):
		pass
		# self.set_random_seat_number()

	def set_random_seat_number(self):
		number = random.randint(1, 99)
		letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{number}{letter}"


@frappe.whitelist()
def update_gate_number(flight_name, gate_number):
	tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight_name}, pluck="name")
	
	for ticket_name in tickets:
		ticket = frappe.get_doc("Airplane Ticket", ticket_name)
		ticket.gate_number = gate_number
		ticket.save()