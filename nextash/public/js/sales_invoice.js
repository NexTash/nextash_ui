frappe.ui.form.on("Sales Invoice", {
    // frm passed as the first parameter
    refresh(frm) {   
        console.log('working');
        frm.set_df_property('project', 'reqd',  )
    }
})