import json

menu = {}  # Dictionary to store dish details
orders = {}  # Dictionary to store order details
order_count = 0  # Variable to track the total number of orders placed

# Function to save menu and order data to a file
def save_data():
    data = {
        "menu": menu,
        "orders": orders,
        "order_count": order_count
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
    print("Data saved successfully!\n")

# Function to load menu and order data from a file
def load_data():
    global menu, orders, order_count
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            menu = data.get("menu", {})
            orders = data.get("orders", {})
            order_count = data.get("order_count", 0)
        print("Data loaded successfully!\n")
    except FileNotFoundError:
        print("No previous data found.\n")

# Function to add a new dish to the menu
def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available (yes/no)? ").lower() == "yes"
    menu[dish_id] = {
        "dish_name": dish_name,
        "price": price,
        "availability": availability
    }
    print(f"Dish '{dish_name}' added to the menu!\n")

# Function to remove a dish from the menu
def remove_dish():
    dish_id = input("Enter the dish ID: ")
    if dish_id in menu:
        dish_name = menu[dish_id]["dish_name"]
        del menu[dish_id]
        print(f"Dish '{dish_name}' removed from the menu!\n")
    else:
        print("Invalid dish ID. Dish does not exist!\n")

# Function to update the availability of a dish
def update_availability():
    dish_id = input("Enter the dish ID: ")
    if dish_id in menu:
        availability = input("Is the dish available (yes/no)? ").lower() == "yes"
        menu[dish_id]["availability"] = availability
        print(f"Dish availability updated successfully!\n")
    else:
        print("Invalid dish ID. Dish does not exist!\n")

# Function to display the menu
def display_menu():
    if menu:
        print("Menu:")
        for dish_id, dish_info in menu.items():
            availability = "Available" if dish_info["availability"] else "Not available"
            print(f"ID: {dish_id}, Dish: {dish_info['dish_name']}, Price: {dish_info['price']}, Availability: {availability}")
    else:
        print("Menu is empty!\n")

# Function to place a new order
def place_order():
    global order_count
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
    order_dishes = []
    total_price = 0.0
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]["availability"]:
            dish_info = menu[dish_id]
            order_dishes.append(dish_info["dish_name"])
            total_price += dish_info["price"]
        else:
            print(f"Invalid dish ID: {dish_id}. Dish does not exist or is not available!")
            return

    order_count += 1
    order_id = f"ORD-{order_count}"
    orders[order_id] = {
        "customer_name": customer_name,
        "dishes": order_dishes,
        "status": "received",
        "total_price": total_price
    }
    print(f"Order '{order_id}' placed successfully!\n")

# Function to update the status of an order
def update_order_status():
    order_id = input("Enter the order ID: ")
    if order_id in orders:
        status = input("Enter the new status: ")
        orders[order_id]["status"] = status
        print(f"Order status updated successfully!\n")
    else:
        print("Invalid order ID. Order does not exist!\n")

# Function to display all orders
def display_orders():
    if orders:
        print("All Orders:")
        for order_id, order_info in orders.items():
            print(f"Order ID: {order_id}, Customer Name: {order_info['customer_name']}, Dishes: {', '.join(order_info['dishes'])}, Status: {order_info['status']}, Total Price: {order_info['total_price']}")
    else:
        print("No orders found!\n")

# Function to display orders with a specific status
def display_orders_by_status():
    status = input("Enter the order status to filter by: ")
    filtered_orders = {order_id: order_info for order_id, order_info in orders.items() if order_info["status"] == status}
    if filtered_orders:
        print(f"Orders with status '{status}':")
        for order_id, order_info in filtered_orders.items():
            print(f"Order ID: {order_id}, Customer Name: {order_info['customer_name']}, Dishes: {', '.join(order_info['dishes'])}, Status: {order_info['status']}, Total Price: {order_info['total_price']}")
    else:
        print(f"No orders found with status '{status}'!\n")

# Main loop to handle user input
while True:
    print("Welcome to Zesty Zomato Food Delivery Management System")
    print("1. Add a new dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update the availability of a dish")
    print("4. Display the menu")
    print("5. Place a new order")
    print("6. Update the status of an order")
    print("7. Display all orders")
    print("8. Display orders by status")
    print("9. Save data")
    print("10. Load data")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == "1":
        add_dish()
    elif choice == "2":
        remove_dish()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        display_menu()
    elif choice == "5":
        place_order()
    elif choice == "6":
        update_order_status()
    elif choice == "7":
        display_orders()
    elif choice == "8":
        display_orders_by_status()
    elif choice == "9":
        save_data()
    elif choice == "10":
        load_data()
    elif choice == "11":
        print("Thank you for using Zesty Zomato Food Delivery Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
