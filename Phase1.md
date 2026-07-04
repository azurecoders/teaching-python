# Python Fundamentals: A Practical Guide with Real-World Examples

Let me explain these core Python concepts using real-world scenarios that you'll actually encounter as a developer.

## 1. Variables

**What they are:** Containers for storing data values. Think of them as labeled boxes where you keep information.

**Real-World Example: A Customer Profile System**

```python
# Storing customer information
customer_name = "Sarah Johnson"
customer_age = 34
customer_email = "sarah.j@email.com"
is_premium_member = True
total_purchases = 1247.50

# Variables can change (they're "variable"!)
customer_age = 35  # Sarah had a birthday
total_purchases = total_purchases + 89.99  # New purchase

# Multiple assignments
first_name, last_name = "John", "Smith"
x = y = z = 0  # Multiple variables with same value

# Dynamic typing - Python figures out the type
user_input = "42"  # String
user_input = 42     # Now it's an integer
```

**Common variable types:**

- `int`: Whole numbers (age, quantity)
- `float`: Decimal numbers (price, temperature)
- `str`: Text (name, address)
- `bool`: True/False (is_active, has_paid)

---

## 2. Loops

**What they are:** Repeating blocks of code. Like a checkout process scanning multiple items.

### For Loops - When you know how many times to repeat

**Real-World Example: Processing a Shopping Cart**

```python
# Shopping cart items
cart_items = ["laptop", "mouse", "keyboard", "monitor", "headphones"]

# 1. Process each item in the cart
print("=== Processing Cart ===")
for item in cart_items:
    print(f"Adding {item} to order...")

# 2. Calculate total with quantities and prices
products = [
    {"name": "Laptop", "price": 1200, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 2},
    {"name": "Keyboard", "price": 80, "quantity": 1}
]

total = 0
for product in products:
    subtotal = product["price"] * product["quantity"]
    total += subtotal
    print(f"{product['name']}: ${subtotal:.2f}")

print(f"Total: ${total:.2f}")

# 3. Range loop - repeat a specific number of times
for i in range(5):
    print(f"Processing order #{i+1}")

# 4. Working with dictionaries
customer = {"name": "Alice", "age": 28, "city": "NYC"}
for key, value in customer.items():
    print(f"{key}: {value}")
```

### While Loops - When you don't know how many times

**Real-World Example: ATM Withdrawal System**

```python
# ATM PIN validation - keeps asking until correct
correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_pin = input("Enter your PIN: ")
    if user_pin == correct_pin:
        print("✅ PIN accepted. Welcome!")
        break  # Exit the loop
    else:
        attempts += 1
        print(f"❌ Incorrect PIN. {max_attempts - attempts} attempts remaining.")
else:
    print("🔒 Account locked. Too many failed attempts.")

# Stock inventory management
inventory = 10
while inventory > 0:
    print(f"📦 Items remaining: {inventory}")
    inventory -= 1  # Remove one item
    # In real scenario: sell item, update database, etc.
print("📭 Out of stock!")

# Processing user input until they choose to quit
while True:
    command = input("Enter command (or 'quit' to exit): ")
    if command.lower() == 'quit':
        print("Shutting down...")
        break
    print(f"Processing: {command}")
```

---

## 3. Input-Output

**What they are:** Getting data from users (input) and showing results (output). Like a cash register - you enter items and see the total.

**Real-World Example: Restaurant Order System**

```python
# === INPUT ===
# Getting data from the user
customer_name = input("Enter customer name: ")
table_number = int(input("Enter table number: "))
order_items = []

print("Enter items (type 'done' when finished):")
while True:
    item = input("Item name: ")
    if item.lower() == 'done':
        break
    price = float(input("Price: $"))
    quantity = int(input("Quantity: "))
    order_items.append({"item": item, "price": price, "quantity": quantity})

# === OUTPUT ===
# Displaying information in different formats

# 1. Simple string concatenation
print("Order received for: " + customer_name)

# 2. f-strings (modern and clean) - RECOMMENDED
print(f"Customer: {customer_name} | Table: {table_number}")

# 3. String formatting with .format()
print("Order items: {}".format(order_items))

# 4. Building a receipt
print("\n" + "="*40)
print(f"📋 RECEIPT - Table {table_number}")
print("="*40)
print(f"Customer: {customer_name}")
print("-"*40)
print(f"{'Item':<20} {'Qty':>5} {'Price':>8} {'Subtotal':>10}")
print("-"*40)

total = 0
for item in order_items:
    subtotal = item['price'] * item['quantity']
    total += subtotal
    print(f"{item['item']:<20} {item['quantity']:>5} ${item['price']:>7.2f} ${subtotal:>9.2f}")

print("-"*40)
print(f"{'TOTAL':>35} ${total:>9.2f}")
print("="*40)
print("Thank you for dining with us! 🍽️")

# === FORMATTED OUTPUT TIPS ===
# Different formatting options
price = 19.99
quantity = 3
print(f"Price: ${price:.2f}")  # 2 decimal places: $19.99
print(f"Quantity: {quantity:03d}")  # Pad with zeros: 003
print(f"Percentage: {0.25:.1%}")  # Percentage: 25.0%
```

---

## 4. Functions

**What they are:** Reusable blocks of code that perform specific tasks. Like a recipe - follow the steps, get the result.

**Real-World Example: E-commerce System**

```python
# === BASIC FUNCTIONS ===

def calculate_discount(price, discount_percent):
    """Calculate discounted price."""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Using the function
original_price = 100
discounted = calculate_discount(original_price, 20)
print(f"Original: ${original_price}, After 20% off: ${discounted:.2f}")

# === FUNCTION WITH DEFAULT PARAMETERS ===

def create_order(customer_name, items, tax_rate=0.08, shipping_cost=5.99):
    """Create an order with default tax and shipping."""
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping_cost

    return {
        "customer": customer_name,
        "items": items,
        "subtotal": subtotal,
        "tax": tax,
        "shipping": shipping_cost,
        "total": total
    }

# Can override defaults
order1 = create_order("Alice", [{"price": 50, "quantity": 2}])  # Uses default tax
order2 = create_order("Bob", [{"price": 30, "quantity": 1}], tax_rate=0.10)  # Override tax

# === FUNCTION WITH MULTIPLE RETURN VALUES ===

def process_payment(amount, payment_type):
    """Process payment and return status and transaction ID."""
    if payment_type == "credit":
        # Simulate credit card processing
        success = True
        transaction_id = f"CR-{int(amount)}{hash(str(amount))%10000:04d}"
    elif payment_type == "paypal":
        success = True
        transaction_id = f"PP-{int(amount)}{hash(str(amount))%10000:04d}"
    else:
        success = False
        transaction_id = None

    return success, transaction_id, amount

# Unpack multiple return values
payment_success, trans_id, charged_amount = process_payment(150.50, "credit")
if payment_success:
    print(f"✅ Payment approved! Transaction: {trans_id}")
    print(f"Charged: ${charged_amount:.2f}")

# === FUNCTION WITH *args (variable arguments) ===

def calculate_shipping(*weights, base_cost=5.00, cost_per_kg=2.50):
    """Calculate shipping cost for multiple packages."""
    total_weight = sum(weights)
    total_cost = base_cost + (total_weight * cost_per_kg)
    return total_cost

shipping1 = calculate_shipping(2.5)  # One package
shipping2 = calculate_shipping(1.0, 3.0, 2.5)  # Three packages
print(f"Shipping for one package: ${shipping1:.2f}")
print(f"Shipping for three packages: ${shipping2:.2f}")

# === FUNCTION WITH **kwargs (keyword arguments) ===

def update_product(product_id, **kwargs):
    """Update product attributes using keyword arguments."""
    print(f"Updating product {product_id}:")
    for key, value in kwargs.items():
        print(f"  - {key}: {value}")
    # In real code: update database
    return kwargs

# Pass any number of keyword arguments
update_product("P123", name="Gaming Mouse", price=59.99, stock=45, category="Accessories")

# === LAMBDA FUNCTIONS (one-line functions) ===

# Sort products by price
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 350}
]
sorted_products = sorted(products, key=lambda x: x['price'])
print("Cheapest to most expensive:", sorted_products)

# Filter with lambda
expensive_items = list(filter(lambda x: x['price'] > 100, products))
print("Items over $100:", expensive_items)

# Map with lambda
prices = [100, 200, 300]
discounted_prices = list(map(lambda x: x * 0.9, prices))
print("10% off prices:", discounted_prices)

# === DOCUMENTATION ===

def process_refund(order_id, reason="", refund_percent=100):
    """
    Process a refund for a customer order.

    Args:
        order_id (str): The order identifier
        reason (str): Why the refund is being processed
        refund_percent (float): Percentage to refund (0-100)

    Returns:
        dict: Refund details including amount and status

    Raises:
        ValueError: If refund_percent is not between 0 and 100

    Example:
        >>> process_refund("ORD-123", "Damaged item", 50)
        {'order_id': 'ORD-123', 'amount': 50.0, 'status': 'approved'}
    """
    if not 0 <= refund_percent <= 100:
        raise ValueError("Refund percent must be between 0 and 100")

    # Simulate refund processing
    return {
        "order_id": order_id,
        "amount": 100 * (refund_percent / 100),  # Assuming order was $100
        "status": "approved"
    }
```

---

## 5. Conditions

**What they are:** Making decisions in code. Like a traffic light - if green go, if red stop.

**Real-World Example: Hotel Booking System**

```python
# === BASIC IF-ELSE ===

# Room availability check
available_rooms = 5
requested_rooms = 3

if requested_rooms <= available_rooms:
    print(f"✅ {requested_rooms} rooms available. Booking confirmed!")
else:
    print(f"❌ Only {available_rooms} rooms available.")

# === IF-ELIF-ELSE (multiple conditions) ===

# Room pricing based on room type
room_type = "suite"  # Could be "standard", "deluxe", "suite"

if room_type == "standard":
    price_per_night = 150
    includes_breakfast = False
elif room_type == "deluxe":
    price_per_night = 250
    includes_breakfast = True
elif room_type == "suite":
    price_per_night = 400
    includes_breakfast = True
else:
    price_per_night = 0
    print("❌ Invalid room type")

print(f"Room: {room_type}, Price: ${price_per_night}")

# === NESTED CONDITIONS ===

def check_room_availability(room_type, check_in, check_out, guests):
    """Check if a room is available with nested conditions."""
    # Check if dates are valid
    if check_in < "2024-01-01" or check_out > "2024-12-31":
        print("❌ Invalid dates")
        return False

    # Check room type
    if room_type not in ["standard", "deluxe", "suite"]:
        print("❌ Invalid room type")
        return False

    # Check guest capacity
    if room_type == "standard" and guests > 2:
        print("❌ Standard room max 2 guests")
        return False
    elif room_type == "deluxe" and guests > 4:
        print("❌ Deluxe room max 4 guests")
        return False
    elif room_type == "suite" and guests > 6:
        print("❌ Suite max 6 guests")
        return False

    # Additional check for availability (simplified)
    if room_type == "suite" and check_in == "2024-07-04":  # Holiday weekend
        print("⚠️ High demand - checking waitlist...")
        return False  # In real scenario, would check actual availability

    print(f"✅ {room_type} room available for {guests} guests")
    return True

# Test the function
check_room_availability("suite", "2024-06-15", "2024-06-18", 4)

# === LOGICAL OPERATORS ===

# AND, OR, NOT
age = 25
has_id = True
has_reservation = True

# AND - both conditions must be true
if age >= 18 and has_id:
    print("✅ Can enter the hotel lounge")

# OR - at least one condition must be true
if has_reservation or has_id:
    print("✅ Access granted to check-in counter")

# NOT - negates a condition
if not has_reservation:
    print("⚠️ Please make a reservation first")

# === TERNARY OPERATOR (one-line if-else) ===

# Simple if-else in one line
status = "Available" if available_rooms > 0 else "Fully Booked"
print(f"Status: {status}")

# === COMPLEX CONDITIONAL LOGIC ===

def process_booking(customer_age, is_premium, credit_score, balance, payment_type, room_price):
    """Process a hotel booking with multiple conditions."""

    # Check minimum age
    if customer_age < 18:
        return "Rejected: Must be 18 or older"

    # Check payment options
    if payment_type == "credit":
        if credit_score < 650:
            return "Rejected: Credit score too low"
    elif payment_type == "debit":
        if balance < room_price:
            return f"Rejected: Insufficient balance (Need ${room_price})"
    elif payment_type == "cash":
        print("Cash payment accepted")
    else:
        return "Invalid payment method"

    # Premium members get special treatment
    if is_premium:
        print("✨ Premium member - priority processing")
        if customer_age >= 65:
            print("🎯 Senior discount applied")

    # Additional conditions
    if room_price > 500 and not is_premium:
        return "Rejected: Please contact reservations for premium rooms"

    # If all conditions pass
    return "Booking approved!"

# Test different scenarios
booking1 = process_booking(25, False, 720, 5000, "credit", 300)
booking2 = process_booking(16, False, 650, 1000, "debit", 150)
booking3 = process_booking(30, True, 800, 10000, "credit", 600)

print("Booking 1:", booking1)
print("Booking 2:", booking2)
print("Booking 3:", booking3)

# === COMBINING WITH LOOPS ===

# Dynamic discount system
def apply_discounts(cart_items):
    """Apply different discounts based on conditions."""
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    discounts = []

    # Check for bulk discount
    total_items = sum(item['quantity'] for item in cart_items)
    if total_items >= 10:
        discount = total * 0.15  # 15% off
        discounts.append(("Bulk discount", discount))
        total -= discount

    # Check for specific product discount
    for item in cart_items:
        if item['name'] == 'Laptop' and item['quantity'] >= 2:
            discount = item['price'] * 0.1  # 10% off each laptop
            discounts.append(("Laptop bundle", discount))
            total -= discount

    # Check premium membership
    is_premium = True
    if is_premium:
        discount = total * 0.05  # Additional 5% for premium
        discounts.append(("Premium member", discount))
        total -= discount

    return total, discounts

# Example usage
cart = [
    {"name": "Laptop", "price": 1000, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 3},
    {"name": "Keyboard", "price": 80, "quantity": 5}
]

final_total, applied_discounts = apply_discounts(cart)
print(f"Final total: ${final_total:.2f}")
for discount_name, discount_amount in applied_discounts:
    print(f"  {discount_name}: -${discount_amount:.2f}")
```

---

## Putting It All Together: Complete Real-World Example

Here's a complete restaurant ordering system that uses ALL the concepts:

```python
import datetime

class RestaurantOrderSystem:
    def __init__(self):
        self.menu = {
            "burger": {"price": 12.99, "category": "main"},
            "pizza": {"price": 15.99, "category": "main"},
            "salad": {"price": 9.99, "category": "side"},
            "fries": {"price": 4.99, "category": "side"},
            "soda": {"price": 2.99, "category": "drink"}
        }
        self.orders = []

    def display_menu(self):
        """Display the menu with categories."""
        print("\n" + "="*40)
        print("🍽️  MENU")
        print("="*40)
        for category in ["main", "side", "drink"]:
            print(f"\n{category.upper()}:")
            for item, details in self.menu.items():
                if details["category"] == category:
                    print(f"  {item.capitalize():<10} ${details['price']:.2f}")

    def take_order(self, customer_name, is_member=False):
        """Take a customer's order."""
        print(f"\n🛎️  Taking order for {customer_name}")
        order = {
            "customer": customer_name,
            "items": [],
            "total": 0,
            "member": is_member,
            "timestamp": datetime.datetime.now()
        }

        while True:
            self.display_menu()
            item = input("\nEnter item (or 'done' to finish): ").lower()

            if item == 'done':
                break
            elif item not in self.menu:
                print("❌ Item not found. Please try again.")
                continue

            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("⚠️  Quantity must be positive")
                    continue
            except ValueError:
                print("⚠️  Please enter a number")
                continue

            subtotal = self.menu[item]["price"] * quantity
            order["items"].append({
                "name": item,
                "quantity": quantity,
                "price": self.menu[item]["price"],
                "subtotal": subtotal
            })
            order["total"] += subtotal

        # Apply discounts
        if is_member:
            order["discount"] = order["total"] * 0.1
            order["total"] -= order["discount"]
        else:
            order["discount"] = 0

        self.orders.append(order)
        return order

    def print_receipt(self, order):
        """Print a formatted receipt."""
        print("\n" + "="*50)
        print("🧾  RECEIPT")
        print("="*50)
        print(f"Customer: {order['customer']}")
        print(f"Time: {order['timestamp'].strftime('%Y-%m-%d %H:%M')}")
        print("-"*50)
        print(f"{'Item':<15} {'Qty':>5} {'Price':>8} {'Subtotal':>10}")
        print("-"*50)

        for item in order["items"]:
            print(f"{item['name'].capitalize():<15} {item['quantity']:>5} ${item['price']:>7.2f} ${item['subtotal']:>9.2f}")

        print("-"*50)
        if order["discount"] > 0:
            print(f"{'Member Discount':<35} -${order['discount']:>8.2f}")
        print(f"{'TOTAL':<35} ${order['total']:>9.2f}")
        print("="*50)
        print("Thank you for dining with us! 🍴")

    def daily_summary(self):
        """Show summary of all orders."""
        if not self.orders:
            print("No orders today")
            return

        print("\n📊 DAILY SUMMARY")
        print("="*40)
        total_orders = len(self.orders)
        total_revenue = sum(order["total"] for order in self.orders)
        total_discounts = sum(order["discount"] for order in self.orders)

        print(f"Orders: {total_orders}")
        print(f"Revenue: ${total_revenue:.2f}")
        print(f"Discounts given: ${total_discounts:.2f}")

        # Most popular items
        item_counts = {}
        for order in self.orders:
            for item in order["items"]:
                item_counts[item["name"]] = item_counts.get(item["name"], 0) + item["quantity"]

        print("\nTop 3 items:")
        sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (item, count) in enumerate(sorted_items[:3], 1):
            print(f"  {i}. {item.capitalize()}: {count}")

# === RUN THE SYSTEM ===
def main():
    restaurant = RestaurantOrderSystem()

    while True:
        print("\n🏪  RESTAURANT ORDER SYSTEM")
        print("1. Place order")
        print("2. View daily summary")
        print("3. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            name = input("Customer name: ")
            member = input("Member? (yes/no): ").lower() == "yes"
            order = restaurant.take_order(name, member)
            restaurant.print_receipt(order)
        elif choice == "2":
            restaurant.daily_summary()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
```

---

## Quick Reference Card

| Concept          | Key Points                                   | When to Use                                    |
| ---------------- | -------------------------------------------- | ---------------------------------------------- |
| **Variables**    | Store values, can change, dynamic typing     | For any data you need to store and use later   |
| **Loops**        | `for` (known count), `while` (unknown count) | Repeating tasks, iterating through collections |
| **Input/Output** | `input()`, `print()`, f-strings              | Getting user input, showing results            |
| **Functions**    | Reusable code, parameters, return values     | When you need to repeat logic, organize code   |
| **Conditions**   | `if-elif-else`, logical operators            | Making decisions based on data                 |
18
**Remember:** Practice is key! Start with small programs and gradually add complexity. Every professional developer started exactly where you are now. Happy coding! 🚀
