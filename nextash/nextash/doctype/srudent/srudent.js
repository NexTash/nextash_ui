// Copyright (c) 2022, Nextash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Srudent', {

	bio_marks: function (frm) {
		cal_marks(frm)
	},
	math_marks: function (frm) {
		cal_marks(frm)
	}
});

const cal_marks = (frm) => {
	const doc = frm.doc
	const bio = doc.bio_marks
	const math = doc.math_marks
	const total = bio + math
	doc.total_marks = total
	frm.refresh_field("total_marks")
}
