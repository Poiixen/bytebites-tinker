from models import Customer, MenuItem, Menu, Order


# --- Fixtures ---

def make_burger():
    return MenuItem("Spicy Burger", 8.99, "Burgers", 4.5)

def make_soda():
    return MenuItem("Large Soda", 2.49, "Drinks", 4.0)

def make_cake():
    return MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8)


# --- Order tests ---

def test_order_total_with_multiple_items():
    # An order with a burger ($8.99) and soda ($2.49) should total $11.48
    order = Order()
    order.add_item(make_burger())
    order.add_item(make_soda())
    assert round(order.compute_total(), 2) == 11.48

def test_order_total_is_zero_when_empty():
    # A new order with no items should have a total of $0
    order = Order()
    assert order.compute_total() == 0.0

def test_order_total_with_single_item():
    # An order with only one item should return that item's price exactly
    order = Order()
    order.add_item(make_cake())
    assert round(order.compute_total(), 2) == 4.99


# --- Menu filtering tests ---

def test_filter_by_category_returns_matching_items():
    # Filtering "Drinks" should return only the soda
    menu = Menu()
    menu.add_item(make_burger())
    menu.add_item(make_soda())
    menu.add_item(make_cake())
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"

def test_filter_by_category_returns_empty_for_unknown_category():
    # Filtering a category that doesn't exist should return an empty list
    menu = Menu()
    menu.add_item(make_burger())
    result = menu.filter_by_category("Sushi")
    assert result == []

def test_filter_by_category_does_not_return_other_categories():
    # Filtering "Desserts" should not include burgers or drinks
    menu = Menu()
    menu.add_item(make_burger())
    menu.add_item(make_soda())
    menu.add_item(make_cake())
    desserts = menu.filter_by_category("Desserts")
    names = [item.name for item in desserts]
    assert "Spicy Burger" not in names
    assert "Large Soda" not in names


# --- Customer verification tests ---

def test_verify_user_false_with_no_orders():
    # A brand-new customer with no orders should not be verified
    customer = Customer("Jorge")
    assert customer.verify_user() is False

def test_verify_user_true_after_adding_order():
    # A customer with at least one past order should be verified
    customer = Customer("Jorge")
    order = Order()
    order.add_item(make_burger())
    customer.add_order(order)
    assert customer.verify_user() is True
