# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

    columns = get_columns()

    data = get_data(filters)

    return columns, data

def get_columns():
	return [
        {
			'label': 'Airport', 
			'fieldname': 'airport', 
			'fieldtype': 'Link', 
			'options': 'Airport', 
			'width': 200
		},
        {
			'label': 'Total Shops', 
			'fieldname': 'total_shops', 
			'fieldtype': 'Int', 
			'width': 150
		},
        {
			'label': 'Occupied', 
			'fieldname': 'occupied_shops', 
			'fieldtype': 'Int', 
			'width': 150
		},
        {
			'label': 'Available', 
			'fieldname': 'available_shops', 
			'fieldtype': 'Int', 
			'width': 150
		},
	]

def get_data(filters):
	conditions = {}

	if filters.get('airport'):
		conditions['name'] = filters.get('airport')  

	airports = frappe.get_all('Airport', filters=conditions)

	data = []

	for a in airports:

		total_shops = frappe.db.count('Shop', {'airport':  a.name})
		occupied_shops = frappe.db.count('Shop', {'airport':  a.name, 'status': 'Occupied'})
		available_shops = frappe.db.count('Shop', {'airport':  a.name, 'status': 'Available'})

		data.append({
			'airport': a.name,
			'total_shops': total_shops,
			'occupied_shops': occupied_shops,
			'available_shops': available_shops
		})
        
	return data		