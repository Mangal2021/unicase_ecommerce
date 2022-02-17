import frappe

def get_context(context):
    x = frappe.form_dict.docname;
    # print(f"\n\n\n\n{frappe.form_dict.docname}\n\n\n\n")
    context.member = frappe.get_doc("Member",x)
    return context

