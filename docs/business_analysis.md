 # Business Process and Organisational Responsibilities Analysis

## Analysis of the business

It is a community initiative connecting local food producers with consumers within twenty miles of Bristol city centre. Forty small-to-medium producers currently struggle to reach customers beyond farmers' markets and farm gate sales. The digital marketplace is intended to remove that barrier. The network serves three customer segments:

        - Young professionals and families
        - Community groups 
        - Independent restaurants and cafes


## Analysis of Major Business Processes

### P1. Product Listing and Inventory Management

Producers submit product details, including product name, description, category, price, quantity, farm origin and seasonal availability. The marketplace validates the information before publishing the product. Organic certification claims may require external verification. Producers can update inventory and availability and products with zero stock must become unavailable for new orders.

##### Trigger
• P1a: a registered producer decides to list a new product.
• P1b: a producer changes a quantity or availability period; stock reaches zero or is replenished; a season opens or closes; an order reduces stock.

##### Main steps: P1a Listing and Validation
1. The producer submits name, description, category, price, quantity, availability period and farm origin, plus harvest date, allergens, organic certification and best-before date where relevant.
2. The platform checks that mandatory fields are present and valid. The producer corrects anything missing or invalid.
3. If the product is labelled organic, the platform sends the certification details to an external or simulated verification service.
4. When every check succeeds, the product is published to customers.

##### Main steps: P1b Inventory and Seasonal Availability
1. The producer updates quantity or availability dates. The platform rejects invalid values and asks for a correction.
2. The platform checks whether stock is above zero and today falls inside the availability period.
3. Zero stock makes the product unavailable for new orders. Restocking inside the season makes it available again.

##### Outcome
P1a produces a published product record carrying its traceability data. P1b produces a correct availability status for every product, so customers see accurate information.

##### Exceptions
Missing or invalid data; failed certification; verification service unavailable (the product is not published without successful verification); invalid quantity or dates; a stock change that conflicts with open orders.

### P2. Product Browsing and Discovery

Customers browse products by categories such as vegetables, dairy, bakery goods, preserves and seasonal specialities. Search functionality helps customers locate specific products. Product displays should communicate farm origin, harvest dates and seasonal availability where relevant.

##### Trigger
A customer visits the marketplace or enters a search.

##### Main steps
1. The customer browses categories (vegetables, dairy, bakery goods, preserves, seasonal specialities) or searches by keyword.
2. The platform returns matching products with availability status, farm origin, harvest date and seasonal indicator.
3. The customer opens a product to see price, allergens, organic status and best-before date.
4. The customer adds chosen items to a basket.

##### Outcome
A basket of available products from one or more producers.

##### Exceptions
No search results; a product becomes unavailable while it is in the basket (driven by P1b).

### P3. Order Processing

Customers place orders for products from one or more producers. The marketplace must support both single-vendor and multi-vendor orders while retaining the responsibilities and fulfilment arrangements associated with each supplier. Producers require sufficient preparation time, with a minimum of 48 hours' lead time for incoming orders.

##### Trigger
A customer proceeds to checkout.

##### Main steps
1. The platform re-checks stock and availability for every item.
2. It splits the basket by producer into sub-orders and keeps each supplier's responsibilities attached.
3. It shows the customer each supplier's delivery or collection arrangements.
4. It requests payment (P4, sandbox only).
5. On successful payment it confirms the order and notifies each producer, which starts P5.

##### Outcome
One confirmed order made of one or more producer sub-orders. Stock is reduced, which can trigger P1b.

##### Exceptions
Payment failure; an item sells out during checkout; only part of a multi-vendor basket is available.

### P4. Payment and Settlement

The marketplace processes payments for customer orders and calculates the network's five per cent commission. Payments must be allocated to the appropriate producers according to agreed arrangements, with weekly settlements and auditable financial records.

##### Trigger
A payment request from checkout; the weekly settlement cycle.

##### Main steps
1. The platform sends the payment to the payment service.
2. On confirmation it records the transaction.
3. It calculates the five percent commission and each producer's share per sub-order.
4. At the end of each week it totals each producer's completed orders (assumption: only fulfilled orders are settled).
5. It pays producers and issues a settlement statement with an audit trail suitable for tax and accounting.

##### Outcome
Producers are paid weekly with transparent statements, BRFN receives its commission, and financial records are auditable.

##### Exceptions
Declined payment; refund or disputed order (open question); failed payout.

### P5.Order Fulfilment

Producers prepare orders and fulfilment arrangements communicate how customers receive their purchases through delivery or collection. Multi-vendor orders require clear communication of individual suppliers' responsibilities and commitments.

##### Trigger
A confirmed order notifies a producer.

##### Main steps
1. The platform notifies the producer of the sub-order with at least 48 hours' lead time.
2. The producer confirms and prepares the products.
3. Delivery or collection takes place as arranged.
4. Completion is recorded, and the customer can see the status of each supplier's part.

##### Outcome
The customer receives the goods and a fulfilment status is recorded per producer. This releases the order for settlement.

##### Exceptions
Producer cannot fulfil; late delivery; missed collection; partial fulfilment of a multi-vendor order.

### P6. Quality and Traceability

The marketplace records relevant product information, including farm origin, organic certification status, allergen warnings and best-before dates. Records linking customers, products and producers support communication when quality issues or food safety concerns arise.

##### Trigger
Continuous, at listing and ordering (records are captured); an incident starts when a quality or food safety concern is reported.

##### Main steps
1. At listing, the platform stores origin, organic status, allergen warnings and best-before date.
2. At ordering, it links customer, product and producer.
3. When a concern is raised, the administrator identifies the affected product and producer.
4. The platform finds every customer who bought it from the order records.
5. Customers and the producer are notified, and the outcome is recorded. Regulators are informed where required (assumption).

##### Outcome:
A traceable record for every product sold and rapid, targeted communication during an incident.

##### Exceptions
Incomplete traceability data

### P7. Sustainability and Community Engagement

The platform supports postcode-based food miles calculations, surplus produce notifications and last-minute discounts to reduce food waste. Producers can also share seasonal recipes, storage guidance and farm stories.

##### Trigger
Order completion or a reporting period (food miles); a producer flags surplus stock (discounts); a producer submits content (recipes and stories).

##### Main steps
1. Food miles: the platform compares producer and customer postcodes through a distance service, records the distance per order and aggregates it for reporting.
2. Surplus: the producer flags surplus, sets a last-minute discount, interested customers are notified, and the sale goes through normal checkout.
3. Content: the producer submits a seasonal recipe, storage guidance or farm story, the administrator reviews it (assumption) and it is published.

##### Outcome
Food miles figures for the network, reduced food waste and educational content that strengthens community links.

##### Exceptions
Invalid postcode; distance service unavailable; discount conflicts with the 48-hour lead time

## Relationships Between Business Processes

The seven major business processes are interconnected through shared product information, order information, inventory updates and financial records. These relationships ensure that the marketplace can coordinate customer purchases, producer responsibilities and the supporting business activities.

#### Product Listing, Browsing and Inventory

Product listing and inventory management (P1) provides the product information and availability status used by product browsing and discovery (P2). Customers can only select products that are available for purchase. When stock reaches zero or a product's availability period ends, the listing must be updated so that the product cannot be ordered.

#### Browsing, Order Processing and Inventory

Product browsing and discovery (P2) enables customers to select products and create a basket. During order processing (P3), the marketplace checks stock and availability again because inventory may have changed since the customer first selected the items. A confirmed order reduces available stock, linking P3 back to P1. If an item is no longer available, the marketplace must communicate this to the customer before the order is confirmed.

#### Order Processing, Payment and Fulfilment

Order processing (P3) initiates the payment process (P4). Payment results determine whether the order can proceed according to the agreed business rules. For orders involving multiple producers, the marketplace separates the order into producer-specific sub-orders and notifies the relevant producers after confirmation. These notifications initiate order fulfilment (P5), where each producer prepares and fulfils their part of the order.

#### Fulfilment and Settlement

Order fulfilment (P5) records whether each producer's part of an order has been completed. This information can support the weekly settlement process in P4. However, the rule that only fulfilled orders are eligible for settlement must be confirmed with BRFN before it is treated as a final business requirement.

#### Product Information and Traceability

Product listing and inventory management (P1) captures product information such as farm origin, organic status, allergens and best-before dates where relevant. Quality and traceability (P6) uses this information alongside order records to identify products, producers and customers affected by a reported quality concern. Accurate and complete records are therefore important for effective incident investigation.

#### Sustainability and Community Engagement

Sustainability and community engagement (P7) complements the other processes. Food-miles reporting uses producer and customer postcode information associated with orders. Surplus produce offers can affect product listings, prices and customer purchasing decisions, while still following the agreed availability and ordering rules. Recipes, storage guidance and farm stories provide additional information to support community engagement.

Overall, these relationships demonstrate that changes in one process may affect other parts of the marketplace. The system must maintain consistent product availability, order status and relevant records across the connected processes.

### Organisational Responsibilities

Operating the BRFN digital marketplace requires coordination between producers, customers, BRFN administrators and the supporting software platform. Each participant has different responsibilities throughout the marketplace's business processes.

- **Producers:** Submit and maintain product information, update stock and availability, respond to incoming orders, prepare products and fulfil orders according to the agreed delivery or collection arrangements.
- **Customers:** Browse products, select items, provide the information required for ordering and payment, and receive their orders through the agreed fulfilment arrangements.
- **BRFN administrators:** Oversee marketplace operations, support the resolution of product or quality concerns, and manage content or operational decisions that require administrative approval.
- **Financial operations:** Oversee commission calculations, producer settlement arrangements and the maintenance of appropriate financial records. The precise allocation of these responsibilities within BRFN requires confirmation.
- **Marketplace platform:** Automates activities such as validating product information, displaying availability, checking stock at checkout, splitting orders by producer, recording transactions and maintaining traceability records.
- **External service providers:** Support specific activities such as certification verification, payment processing and postcode-based distance calculations.

The responsibilities of the business participants should be distinguished from the automated activities performed by the software. The platform supports the business processes, but accountability for business decisions and exceptions should be assigned to an appropriate business role.


## External Services and Dependencies

The marketplace relies on external or supporting services for certain activities.

- Organic certification verification: supports checking certification claims submitted during product listing or updates. The system must handle unsuccessful verification and service unavailability appropriately.
- Payment services: support transaction processing and the financial workflow. Development and testing must use sandbox or simulated payment environments rather than live payment systems.
- Postcode-based distance calculations: support environmental reporting by estimating food miles.

These dependencies should be considered when modelling interactions between the marketplace and external services.


## Implications for the Strategic BPMN

The strategic BPMN should represent the major business processes required to operate the Bristol Regional Food Network (BRFN) digital marketplace, including the main participants, activities, decisions and handovers between processes.

The process analysis identifies product listing and inventory management (P1) as the starting point for making products available to customers. Product browsing and discovery (P2) enables customers to identify products and create a basket. Order processing (P3) then checks product availability, separates orders by producer where necessary and initiates payment (P4). Once an order is confirmed, the relevant producer is notified so that order fulfilment (P5) can begin.

The model should also show how information is shared between processes. Inventory changes in P1 can affect product availability during P2 and checkout in P3. Payment confirmation is required before an order is confirmed, subject to the agreed payment rules. Fulfilment status may then determine when a producer's order becomes eligible for settlement, subject to confirmation of BRFN's settlement policy.

Quality and traceability (P6) support the marketplace by maintaining links between products, producers and customers. These records can be used to investigate quality concerns and identify affected customers. Sustainability and community engagement (P7) complement the core marketplace processes through food-miles calculations, surplus produce offers and educational content.

The strategic BPMN should identify the main business participants, including customers, producers and BRFN administrators, and show where the marketplace interacts with external services. These include organic certification verification, payment processing and postcode-based distance calculations. Exceptions such as unavailable stock, unsuccessful payments and failed external-service requests should be considered where they affect the overall business process.

The model should provide a high-level view of how BRFN operates rather than showing every detailed system interaction. Detailed validation rules, data fields and exception-handling steps can be elaborated in the relevant functional requirements and implementation models.