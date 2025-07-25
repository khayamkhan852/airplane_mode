// Copyright (c) 2025, khayam khan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button(__('Assign Seat'), () => {
            let d = new frappe.ui.Dialog({
                title: 'Select Seat',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data'
                    },
                ],
                size: 'large',
                primary_action_label: 'Assign',
                primary_action(values) {
                    if (values.seat_number) {
                        frm.set_value('seat', values.seat_number).then(() => {
                            frm.save();
                        });
                        d.hide();
                    } else {
                        frappe.msgprint(__('Please enter a seat number'));
                    }

                    // frm.set_value('seat', values.seat_number)
                    d.hide();
                }
            });
            
            d.show();
        }, __('Actions'));

        frm.trigger("calculate_total_amount");
	},

    flight_price(frm) {
        frm.trigger("calculate_total_amount");
    },

    calculate_total_amount(frm) {
        let total_add_on_amount = 0;

        frm.doc.add_ons.forEach(add_on => {
            total_add_on_amount += add_on.amount;
        });

        let total_amount = frm.doc.flight_price + total_add_on_amount;

        frm.set_value("total_amount", total_amount);
    }
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
    amount(frm) {
        frm.trigger("calculate_total_amount");
    },
    airplane_ticket_add_on_type(frm, cdt, cdn) {
        let current_child = locals[cdt][cdn];

        if (!current_child.airplane_ticket_add_on_type) return;

        let duplicate_found = false;

        frm.doc.add_ons.forEach(add_on => {
            if (
                add_on.airplane_ticket_add_on_type === current_child.airplane_ticket_add_on_type &&
                add_on.name !== current_child.name
            ) {
                duplicate_found = true;
            }
        });

        if (duplicate_found) {
            frappe.msgprint({
                title: __('Duplicated Item'),
                indicator: 'red',
                message: __('The Add-on Type you added already exist in the table.')
            });

            frm.get_field('add_ons').grid.grid_rows_by_docname[cdn].remove();
            frm.refresh_field('add_ons');
            return false;
        }

    },
    add_ons_add(frm, cdt, cdn) {
        frm.trigger("calculate_total_amount");
    },
    add_ons_remove(frm) {
        frm.trigger("calculate_total_amount");
    },
});
