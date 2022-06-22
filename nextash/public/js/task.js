frappe.ui.form.on("Task", {
    // run first time only when page reload 
    setup(){
      frappe.require("/assets/erpnext/js/projects/timer.js");
    },
    // write code that you want to reload on evey refresh 
    refresh(frm) {
      let button = "Start Timer";
      $.each(frm.doc.time_logs || [], function (i, row) {
        if (row.from_time <= frappe.datetime.now_datetime() && !row.completed) {
          button = "Resume Timer";
        }
      });
  
      frm
        .add_custom_button(__(button), function () {
          var flag = true;
          $.each(frm.doc.time_logs || [], function (i, row) {
            // Fetch the row for which from_time is not present
            if (flag && row.activity_type && !row.from_time) {
              erpnext.timesheet.timer(frm, row);
              row.from_time = frappe.datetime.now_datetime();
              frm.refresh_fields("time_logs");
              frm.save();
              flag = false;
            }
            // Fetch the row for timer where activity is not completed and from_time is before now_time
            if (
              flag &&
              row.from_time <= frappe.datetime.now_datetime() &&
              !row.completed
            ) {
              let timestamp = moment(frappe.datetime.now_datetime()).diff(
                moment(row.from_time),
                "seconds"
              );
              erpnext.timesheet.timer(frm, row, timestamp);
              flag = false;
            }
          });
          // If no activities found to start a timer, create new
          if (flag) {
            erpnext.timesheet.timer(frm);
          }
        })
        .addClass("btn-primary");
    },
  });