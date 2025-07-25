import frappe

def execute():
    print("Populating seats for existing airplane tickets...")

    airplane_tickets = frappe.get_all("Airplane Ticket", filters={"seat": ""}, fields=["name"])

    for airplane_ticket in airplane_tickets:
        ticket_doc = frappe.get_doc("Airplane Ticket", airplane_ticket.name)
        ticket_doc.set_random_seat_number()
        ticket_doc.save()

    frappe.db.commit()
    print("Seat population completed.")