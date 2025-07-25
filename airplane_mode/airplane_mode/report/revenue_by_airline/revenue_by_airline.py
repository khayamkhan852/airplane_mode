# Copyright (c) 2025, khayam khan and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart(data)

	total_revenue = sum([x['revenue'] for x in data])

	report_summary = [
    	{"label":"Total Revenue", "value": frappe.format(total_revenue, {'fieldtype': 'Currency'}), 'indicator':'Green'},
	]
	return columns, data, None, chart, report_summary

def get_columns():
	columns = [
		{
			"label": "Airline",
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 200,
		},
		{
			"label": "Revenue",
			"fieldname": "revenue",
			"fieldtype": "Currency",
			"width": 200,
		},
	]
	return columns

def get_chart(data):
	chart =  {
		"data": {
			"labels": [x["airline"] for x in data],
			"datasets": [
				{
					"values": [x["revenue"] for x in data],
				}
			]
		},
		"type": "donut",
	}

	return chart

def get_data(filters=None):
	airlines = frappe.get_all('Airline', fields=['name'])

	# dictionay comprehension to initialize each airline's revenue to 0
	# resuslt will be like {'AirBlue': 0, 'PIA': 0, 'AirAsia': 0}
	revenue_data = {airline['name']: 0 for airline in airlines}

	tickets = frappe.get_all(
        'Airplane Ticket', 
        fields=['total_amount', 'flight'],
        filters={
			'flight': [
				'in', 
			  	[flight['name'] for flight in frappe.get_all('Airplane Flight', fields=['name', 'airplane'])]
			]
		}
    )

	for ticket in tickets:
		flight = frappe.get_doc('Airplane Flight', ticket['flight'])
        
		airplane = frappe.get_doc('Airplane', flight.airplane)
        
		airline = airplane.airline
        
		revenue_data[airline] += ticket['total_amount']

	data = []

	for airline, revenue in revenue_data.items():
		data.append({
            'airline': airline,
            'revenue': revenue
        })

	return data