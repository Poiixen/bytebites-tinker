# Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

# Candidate Classes

## Customer
Represents a registered user of the app.
- **Attributes:** name, purchase history
- **Responsibilities:** store customer identity, maintain a record of past orders to verify real users

## MenuItem
Represents a single food or drink item available for purchase.
- **Attributes:** name, price, category, popularity rating
- **Responsibilities:** hold all metadata about a sellable item (e.g. "Spicy Burger", "Large Soda")

## Menu
Represents the full catalog of available items.
- **Attributes:** list of MenuItems
- **Responsibilities:** store all items, provide filtering by category (e.g. "Drinks", "Desserts")

## Order
Represents a single transaction when a customer checks out.
- **Attributes:** list of selected MenuItems
- **Responsibilities:** group chosen items together, compute the total cost
