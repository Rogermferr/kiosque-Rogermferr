from menu import products


def get_product_by_id(product_id: int) -> dict | str:
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    try:
        for product in products:
            if product["_id"] == product_id:
                return product

        return {}
    except TypeError as err:
        return err


def get_products_by_type(type_search: str) -> list | str:
    if not isinstance(type_search, str):
        raise TypeError("product type must be a str")

    try:
        return [product for product in products if product["type"] == type_search]

    except TypeError as err:
        return err


def add_product(menu: list, **kwargs: list) -> dict | str:
    product = {}
    list_id = []

    if len(menu) > 0:
        for item in menu:
            list_id.append(item["_id"])
    else:
        list_id.append(0)

    for key, value in kwargs.items():
        product["_id"] = max(list_id) + 1
        product[key] = value

    menu.append(product)

    return product


def menu_report():
    product_count = len(products)
    list_price = []
    most_common_type = []

    for product in products:
        list_price.append(product["price"])
        most_common_type.append(product["type"])

        average_price = (sum(list_price)) / len(list_price)

    return (
        f"Products Count: {product_count} "
        f"- Average Price: ${average_price:.1f} "
        f"- Most Common Type: {max(most_common_type, key=most_common_type.count)}"
    )


def add_product_extra(menu, *required_keys, **kwargs):
    product = {}
    list_id = []
    keys_to_remove = []
    keys_is_required = []

    if len(menu) > 0:
        for item in menu:
            list_id.append(item["_id"])
    else:
        list_id.append(0)

    for key, value in kwargs.items():
        product["_id"] = max(list_id) + 1
        keys_is_required.append(key)
        if key not in required_keys:
            keys_to_remove.append(key)
        elif required_keys not in keys_is_required:
            print(required_keys)
            print(keys_is_required)

            # raise KeyError(f"field {key} is required")
        else:
            product[key] = value

    for key in keys_to_remove:
        del kwargs[key]

    menu.append(product)

    try:
        return product
    except KeyError as err:
        return err
