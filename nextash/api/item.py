import frappe
from requests.utils import requote_uri


def get_item_price(items):
    price_list = "Standard Selling"
    
    # Getting price details
    for row in items:
        item = frappe.db.get_all('Item Price', {
            'price_list': price_list,
            'selling': 1,
            'item_code': row['name']  
        }, [
            'item_code', 'item_name', 'item_description', 'price_list_rate',
            'currency'
        ])
        
        total=0
        if frappe.db.exists('Bin', {'item_code':row['name']}):
            bin=frappe.get_all('Bin', {'item_code':row['name']},['name'])
            for itm in bin:
                bin_doc = frappe.get_doc('Bin', itm.name)
                total+=bin_doc.actual_qty
            row['stock_qty']=total
        if item:
            item = item[0]
            row['sale_price'] = item['price_list_rate']
        
        # Getting Item Image
        if row.get('image'):
            row['image'] = requote_uri(row['image'])
    return items

@frappe.whitelist(allow_guest=True)
def get_items():
    """
    returns all items 
    """
    items_array = frappe.db.get_list('Item')
    items_array = get_item_price(items_array)
    return items_array

@frappe.whitelist(allow_guest=True)
def search_items(name=None):
    """
    returns all items from the database having permission to show in any website menu
    """
    items_array=''
    itm_filters={}
    if name:
        itm_filters['item_code'] = ['like', f'%{name}%']
    
        items_array = frappe.db.get_list('Item', itm_filters, ["*"])

        items_array = get_item_price(items_array)
    return items_array or '0'

