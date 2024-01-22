// Copyright (c) 2023, Asymptotes and contributors
// For license information, please see license.txt

frappe.ui.form.on('law cases', {
    onload: function(frm) {
        // Call the function initially to set the sum
        calculateAndSetSumPayment(frm);
        calculateAndSetSum(frm);
    },
});

frappe.ui.form.on('Law Case Payment', {
    form_render: function(frm) {
        // Triggered when the 'expensetable' child table is rendered
        calculateAndSetSumPayment(frm);
    },
    paymentamount: function(frm, cdt, cdn) {
        // Triggered when 'expenseamount' field in 'expensetable' is changed
        calculateAndSetSumPayment(frm);
    },
});

function calculateAndSetSumPayment(frm) {
    // initialize sum variable
    var totalAmountPayments = 0;

    // iterate through each row in the child table 'expensetable'
    $.each(frm.doc.paymenttable || [], function(x, itempayment) {
        // add the 'expenseamount' field value to the sum
        totalAmountPayments += flt(itempayment.paymentamount);
    });

    // set the sum in a field named 'expenses'
    frm.set_value('payments', totalAmountPayments);
}


frappe.ui.form.on('Law Case Expenses', {
    form_render: function(frm) {
        // Triggered when the 'expensetable' child table is rendered
        calculateAndSetSum(frm);
    },
    expenseamount: function(frm, cdt, cdn) {
        // Triggered when 'expenseamount' field in 'expensetable' is changed
        calculateAndSetSum(frm);
    },
});

function calculateAndSetSum(frm) {
    // initialize sum variable
    var totalAmount = 0;

    // iterate through each row in the child table 'expensetable'
    $.each(frm.doc.expensetable || [], function(i, item) {
        // add the 'expenseamount' field value to the sum
        totalAmount += flt(item.expenseamount);
    });

    // set the sum in a field named 'expenses'
    frm.set_value('expenses', totalAmount);
}
