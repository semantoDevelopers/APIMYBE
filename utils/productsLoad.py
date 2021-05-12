def listOfMapProduct(data):
    products = []
    for prod in data:
        products.append({"id":prod[0],"name":prod[1],"price":prod[2],"category_id":prod[3],"model_id":prod[4],"vendor_id":prod[3],"media_id":prod[4],"is_available":prod[5],"is_stocked":prod[6],"stock_quantity":prod[7]})
    return products