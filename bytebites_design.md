# ByteBites UML Class Diagram (Final)

```
+-------------------------------+
|           Customer            |
+-------------------------------+
| - name: str                   |
| - purchase_history: list[Order]|
+-------------------------------+
| + verify_user(): bool         |
+-------------------------------+
              |
              | places (1 to many)
              v
+-------------------------------+
|            Order              |
+-------------------------------+
| - items: list[MenuItem]       |
+-------------------------------+
| + compute_total(): float      |
+-------------------------------+
              |
              | contains (1 to many)
              v
+-------------------------------+
|          MenuItem             |
+-------------------------------+
| - name: str                   |
| - price: float                |
| - category: str               |
| - popularity_rating: float    |
+-------------------------------+

+-------------------------------+
|            Menu               |
+-------------------------------+
| - items: list[MenuItem]       |
+-------------------------------+
| + filter_by_category(         |
|     category: str             |
|   ): list[MenuItem]           |
+-------------------------------+
              |
              | holds (1 to many)
              v
          MenuItem
```

## Class Descriptions

| Class      | Role                                                           |
|------------|----------------------------------------------------------------|
| Customer   | A registered user; tracks identity and order history           |
| MenuItem   | A single food/drink item with pricing and category metadata    |
| Menu       | The full catalog; supports filtering items by category         |
| Order      | A transaction grouping chosen items; computes the total cost   |

## Relationships

- **Customer → Order** (one-to-many): a customer accumulates past orders in `purchase_history`
- **Order → MenuItem** (one-to-many): an order holds the specific items selected by the customer
- **Menu → MenuItem** (one-to-many): the menu is the master catalog of all available items

## Design Decisions

- `Menu` and `Order` both reference `MenuItem` independently — `Menu` is the full catalog, `Order` is a point-in-time snapshot of what was selected.
- `popularity_rating` is a `float` to allow values like 4.5 out of 5.
- `verify_user()` on `Customer` uses `purchase_history` to confirm the customer has made at least one prior order.
