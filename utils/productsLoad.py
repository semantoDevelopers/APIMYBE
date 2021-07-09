def listOfMapProduct(data):
    products = []
    for prod in data:
        products.append({"id":prod[0],"name":prod[1],"price":prod[2],"category_id":prod[3],"model_id":prod[4],"vendor_id":prod[5],"media_id":prod[6],"is_available":prod[7],"is_stocked":prod[8],"stock_quantity":prod[9]})
    return products