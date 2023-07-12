from menu import products


def calculate_tab(table: list) -> dict:

    list_value = []

    for product in products:
        for item in table:
            if product["_id"] == item["_id"]:
                multiply_values = product["price"] * item["amount"]
                list_value.append(multiply_values)

    total_value = sum(list_value)

    return {"subtotal": f"${total_value:.2f}".rstrip("0")}
