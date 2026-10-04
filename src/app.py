def calculate_discount(price, discount_percent):
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid price or discount, please enter the correct values")

    discount = price * (discount_percent / 100)
    return round(price - discount, 2)


def main():
    products = [
        {"name": "Laptop", "price": 80000, "discount": 10},
        {"name": "Keyboard", "price": 3000, "discount": 15},
        {"name": "Mouse", "price": 1500, "discount": 5},
    ]

    total = 0

    for product in products:
        final_price = calculate_discount(product["price"], product["discount"])
        
        print(f"{product['name']}: ₹{final_price}")
        total+= final_price

    print(f"\nTotal : ₹{total}")

if __name__ == "__main__":
    main()