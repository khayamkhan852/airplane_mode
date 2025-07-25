// Copyright (c) 2025, khayam khan and contributors
// For license information, please see license.txt

frappe.query_reports["Airport Shop Availability"] = {
	"filters": [
		{
			"fieldname": "airport",
			"label": __("Airport"),
			"fieldtype": "Link",
			"options": "Airport",
		}
	]
};
