
frappe.ui.form.on('Employee Checkin', {
	setup: (frm) => {
		if(!frm.doc.time) {
			frm.set_value("time", frappe.datetime.now_datetime());
		}
	},


    before_save: (frm)=> {
        frappe.call({
            method: "nextash.nextash.events.employee_checkin.check_status",
            args: {},
            
            callback: function (r) {
              
            if (r.message == true) {
                $("#employee-checkin").hide();
                $("#employee-checkout").show();
              } else if (r.message == false) {
                $("#employee-checkin").show();
                $("#employee-checkout").hide();
              }else{
                $("#employee-checkin").hide();
                $("#employee-checkout").hide();
              }
            },
          });
    }
});
