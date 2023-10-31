frappe.ui.form.on('User', {
    refresh: function(frm) {
      frm.add_custom_button(__('Get User Email Address'), function(){
        frappe.msgprint(frm.doc.email);
    }, __("Utilities"));
  }
});