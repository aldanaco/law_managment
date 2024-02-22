// Copyright (c) 2024, Asymptotes and contributors
// For license information, please see license.txt

frappe.ui.form.on('rivals', {
    onload: function(frm) {
        // List of fields contributing to rival_name_view
        var fieldsToWatch1 = ['first_name', 'father_name', 'grandfather_name', 'fourth_name'];

        // Attach onchange event to multiple fields
        fieldsToWatch1.forEach(function(field1) {
            cur_frm.cscript[field1] = function(doc, cdt, cdn) {
                updateFullName(doc);
            };
        });
        var fieldsToWatch = ['full_name', 'trade_name'];

        // Attach onchange event to multiple fields
        fieldsToWatch.forEach(function(field) {
            cur_frm.cscript[field] = function(doc, cdt, cdn) {
                updateRivalNameView(doc);
            };
        });
    }
});

function updateRivalNameView(doc) {
    // Set the value of rival_name_view based on multiple fields
    var individualRival = doc.full_name;
    var companyRival = doc.trade_name;
    var rivalName;

    if (individualRival !== null && individualRival !== undefined && individualRival !== '') {
        rivalName = individualRival;
    } else {
        rivalName = companyRival;
    }

    cur_frm.set_value('rival_name_view', rivalName);
}

function updateFullName(doc) {
    // Set the value of full_name based on multiple fields
   var fullName = '';

    // Check each field's value before appending
    if (doc.first_name) {
        fullName += doc.first_name + ' ';
    }
    if (doc.father_name) {
        fullName += doc.father_name + ' ';
    }
    if (doc.grandfather_name) {
        fullName += doc.grandfather_name + ' ';
    }
    if (doc.fourth_name) {
        fullName += doc.fourth_name + ' ';
    }

    // Trim the trailing space
    fullName = fullName.trim();
    cur_frm.set_value('full_name', fullName);
}
