// Custom scripts for Issue Panel
$(document).on("click", "#employee-checkin", function () {
  frappe.call({
    method: "nextash.nextash.events.employee_checkin.employee_checkin",
    args: {},
    callback: function (r) {
      if (!r.exc) {

        frappe.show_alert(
          {
            message: __("Your attendence has been Marked"),
            indicator: "green",
          },
          5
        );
        $("#employee-checkin").hide();
        $("#employee-checkout").show();
        

      }
    },
  });
    
});

$(document).on("click", "#employee-checkout", function () {
  frappe.call({
    method: "nextash.nextash.events.employee_checkin.employee_checkout",
    args: {},
    callback: function (r) {
      if (!r.exc) {
        frappe.show_alert(
          {
            message: __("Your attendence has been Marked"),
            indicator: "green",
          },
          5
        );
        $("#employee-checkin").show();
        $("#employee-checkout").hide();
      }
    },
  });
    

});

$(document).ready(function () {
  frappe.realtime.on("notification", () => {
    console.log("test1");
    frappe.show_alert(
      {
        message: __("Kindly Mark Your Attendance"),
        indicator: "green",
      },
      5
    );
    
})

  frappe.call({
    method: "nextash.events.employee_checkin.check_status",
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
 ;

});

