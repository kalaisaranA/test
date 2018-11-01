from __future__ import unicode_literals
import frappe
import erpnext
from frappe.model.document import Document
from frappe.utils import flt


def qty(doc,method):
	
				
	for d in doc.supplied_items:
		rows  = 0
		data = frappe.db.sql('''select (qty)
				from `tabStock Entry` entry, `tabStock Entry Detail`detail
				where
					entry.purchase_order = %(name)s
					and entry.purpose = "Subcontract"
					and entry.docstatus = 1
					and detail.parent = entry.name
					and (detail.item_code = %(item)s or detail.original_item = %(item)s)''', {
						'name': doc.name,
						'item': d.rm_item_code
					})
		for i1 in data:
			for i2 in i1:
				result_data = i2

			result+= result_data	
			d.t_qty = result
	

		rows += rows 


