// Copyright (c) 2025, khayam khan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
	refresh(frm) {
        frm.set_query("shop_type",  () => {
            return {
                filters: {
                    "enabled": 1
                }
            };
        });
	},
});
