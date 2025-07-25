// Copyright (c) 2025, khayam khan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Contract", {
    contract_template: function (frm) {
        if (frm.doc.contract_template) {
			frappe.call({
				method: "airplane_mode.shop_managment.doctype.contract_template.contract_template.get_contract_template",
				args: {
					template_name: frm.doc.contract_template,
					doc: frm.doc,
				},
				callback: function (r) {
					if (r && r.message) {
						frm.set_value("contract_terms", r.message.contract_terms);
					}
				},
			});
		}
    },
	onload: function(frm) {
        frappe.db.get_single_value('Shop Settings', 'default_shop_rent_amount')
            .then(value => {
                if (value && !frm.doc.rent_amount) {
                    frm.set_value('rent_amount', value);
                }
            });
    },
});
