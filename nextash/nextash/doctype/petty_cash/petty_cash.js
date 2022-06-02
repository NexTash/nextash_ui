// Copyright (c) 2022, Nextash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Petty Cash', {
	// item: () => {
		
	// },
	qty: function(frm){
		calc_amount(frm)
	},
	price: function(frm) {
		calc_amount(frm) 
	},
});

// functions

const calc_amount = (frm) => {
	const doc = frm.doc

	const price = doc.price
	const qty = doc.qty

	const amount = price * qty

	doc.amount = amount

	frm.refresh_field("amount")
}
