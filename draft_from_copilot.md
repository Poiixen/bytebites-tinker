# ByteBites UML Class Diagram (Draft)

```
+------------------+
|    Customer      |
+------------------+
| - name: str      |
| - purchase_history: list[Order] |
+------------------+
| + verify_user()  |
+------------------+
        |
        | places
        v
+------------------+
|     Order        |
+------------------+
| - items: list[MenuItem] |
+------------------+
| + compute_total(): float |
+------------------+
        |
        | contains
        v
+------------------+
|    MenuItem      |
+------------------+
| - name: str      |
| - price: float   |
| - category: str  |
| - popularity_rating: float |
+------------------+

+------------------+
|      Menu        |
+------------------+
| - items: list[MenuItem] |
+------------------+
| + filter_by_category(category: str): list[MenuItem] |
+------------------+
        |
        | holds
        v
    MenuItem
```

## Relationships

- **Customer → Order**: A customer has a list of past orders (one-to-many)
- **Order → MenuItem**: An order contains one or more menu items (one-to-many)
- **Menu → MenuItem**: The menu holds all available menu items (one-to-many)

## Notes / Questions to Verify

- Does `purchase_history` belong on `Customer`, or should `Order` store a reference back to the customer?
- Should `popularity_rating` be a float (e.g. 4.5 out of 5) or an integer rank?
- `Menu` and `Order` both reference `MenuItem` but serve different purposes — `Menu` is the catalog, `Order` is a snapshot of what was selected.
