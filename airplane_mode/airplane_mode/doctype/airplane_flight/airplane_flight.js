// Copyright (c) 2025, khayam khan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {

	},
    setup: function(frm) {
        frm.set_query('crew_member', 'members',  (doc) => {
            return {
                filters: {
                    status: 'Available'
                }
            }
        });
    }
});