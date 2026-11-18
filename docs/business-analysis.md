 # Business Process and Organisational Responsibilities Analysis

## Analysis of the business

It is a community initiative connecting local food producers with consumers within twenty miles of Bristol city centre. Forty small-to-medium producers currently struggle to reach customers beyond farmers' markets and farm gate sales. The digital marketplace is intended to remove that barrier. The network serves three customer segments:

        - Young professionals and families
        - Community groups 
        - Independent restaurants and cafes


## Analysis of Major Business Processes

### P1. Product Listing and Inventory Management

Producers submit product information to the marketplace, which validates and maintains product listings. The marketplace also manages inventory and seasonal availability so customers can view current product information and availability.

##### Triggers

- A producer submits a request to list a new product.
- A producer requests an inventory or seasonal availability update.

##### Main steps:  Listing and Validation
1. The producer submits a product listing request containing the relevant product information.

2. The marketplace receives the request and validates the submitted information.

3. Where a product is labelled organic, the marketplace requests verification from the organic certification verification service.

4. The verification service returns a result to the marketplace.

5. The listing request is processed and the product catalogue is updated accordingly.

##### Main steps: Inventory and Seasonal Availability
1. The producer submits an inventory update request.

2. The marketplace receives the request and manages inventory and seasonal availability.

3. The product catalogue and inventory records are updated.

4. The inventory update process is completed.

##### Outcome
Product listing requests and inventory update requests are processed, allowing the marketplace to maintain product information and availability records.

##### Exceptions and Dependencies

- Missing or invalid product information.

- Unsuccessful organic certification verification.

- Organic certification verification service unavailability.

- Invalid inventory or seasonal availability information.

### P2. Product Browsing and Discovery

Customers use the marketplace to browse and search for available products. The marketplace retrieves product information from the product catalogue and inventory records and displays relevant information to customers.

##### Trigger
A customer requests product browsing or search.

##### Main steps
1. The marketplace receives a product browsing request.

2. The platform provides product browsing and search functionality.

3. Product information is retrieved from the product catalogue and inventory records.

4. Relevant product information is displayed to the customer.

##### Outcome
Customers can discover products and view the information made available through the marketplace.

##### Exceptions
- No matching products are available.

- Product information is missing or outdated.

- A product becomes unavailable before an order is placed.

### P3. Order Processing

The marketplace manages customer orders and coordinates the transition from checkout to payment and fulfilment. The process interacts with the product catalogue, inventory records, and order and payment records.

##### Trigger
A customer submits a checkout request.

##### Main steps
1. The marketplace receives the customer checkout request.

2. The marketplace manages the customer order using the relevant product, inventory, order and payment information.

3. The order proceeds to customer payment processing.

4. The marketplace evaluates the payment result.

5. If payment is successful, the marketplace proceeds to order fulfilment coordination.

6. If payment is unsuccessful, the marketplace handles the unsuccessful payment and the order is not confirmed.

##### Outcome
The marketplace coordinates the order process according to the payment result. Successful payment allows the order to proceed towards fulfilment, while unsuccessful payment is handled separately.

##### Exceptions
- Payment is declined or unsuccessful.

- Product availability changes before checkout is completed.

- The order cannot proceed because relevant product or inventory information is unavailable.

### P4. Payment and Settlement

The marketplace processes payments for customer orders and calculates the network's five per cent commission. Payments must be allocated to the appropriate producers according to agreed arrangements, with weekly settlements and auditable financial records.

##### Trigger
- A customer checkout request initiates payment processing.

- A weekly settlement timer triggers the producer settlement process.

##### Main Steps: Customer Payment

1. The marketplace processes the customer payment request.

2. The payment request is sent to the external payment service.

3. The external service returns the payment processing result.

4. The marketplace evaluates whether payment was successful.

5. If payment succeeds, the order proceeds towards fulfilment.

6. If payment fails, the marketplace handles the unsuccessful payment and the order is not confirmed.

##### Main Steps: Producer Settlements

1. The weekly settlement timer triggers the settlement process.

2. The marketplace manages producer settlements using the available order and payment records.

3. The settlement process is completed.

##### Outcome
Customer payment outcomes are handled by the marketplace and producer settlements are processed through a separate weekly settlement workflow.

##### Exceptions
- Declined or unsuccessful customer payment.

- Failed producer payout.

- Refunds or disputed orders.

- Incomplete or inaccurate financial records.

### P5.Order Fulfilment

Producers prepare orders and fulfilment arrangements communicate how customers receive their purchases through delivery or collection. Multi-vendor orders require clear communication of individual suppliers' responsibilities and commitments.

##### Trigger
The payment process indicates that the customer payment was successful.

##### Main steps
1. The marketplace proceeds from the successful-payment path to order fulfilment coordination.

2. The marketplace coordinates fulfilment using the relevant order details.

3. Order confirmation and fulfilment details are communicated to the customer.

4. The order fulfilment process is completed.

##### Outcome
The marketplace coordinates the fulfilment process and communicates relevant information to the customer.

##### Exceptions
- A producer cannot fulfil an order.

- Delivery or collection is delayed.

- A collection is missed.

- Only part of a multi-producer order is fulfilled.

### P6. Quality and Traceability

The marketplace manages food-quality incidents and traceability using product information, order records and relevant information about producers and customers.

Product listing and inventory management provide product information, while order and payment records support the identification of relevant transactions.

##### Trigger
A food-quality incident is reported by a relevant participant.

##### Main steps
1. The marketplace receives a food-quality incident report.

2. The incident is handled through the food-quality incident and traceability process.

3. Relevant product, inventory and order information is used to support the investigation.

4. The marketplace communicates relevant food-safety information where appropriate.

5. Incident handling is completed.

##### Outcome:
Food-quality incidents can be managed using the information available within the marketplace, supporting investigation and traceability.

##### Exceptions
- Incomplete product or traceability information.

- Insufficient order records to identify affected customers.

- Difficulty obtaining the information required to investigate an incident.

### P7. Sustainability and Community Engagement

The platform supports postcode-based food miles calculations, surplus produce notifications and last-minute discounts to reduce food waste. Producers can also share seasonal recipes, storage guidance and farm stories.

##### Trigger
A need to promote seasonal products, make surplus food available, or communicate sustainability and community information to customers.

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

P7 related to P1 Product Listing and Inventory Management because seasonal and surplus offers depend on accurate product and stock information. It also supports P2 Product Browsing and Discovery by making relevant products and community information visible to customers. However, P7 is part of the wider business analysis and is not explicitly modelled as a separate process in the current strategic BPMN diagram.

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

The strategic BPMN represents the major internal business processes required to operate the BRFN digital marketplace and the interactions between the marketplace and its external participants.

The model begins with product listing and inventory management (P1), which maintains product information and availability. Product browsing and discovery (P2) enables customers to request and view product information. Customer checkout requests initiate order processing (P3), which connects to customer payment processing (P4).

The payment decision determines whether the order can proceed. Successful payment allows the marketplace to coordinate order fulfilment (P5), while unsuccessful payment is handled through a separate path and the order is not confirmed. Producer settlements are managed through a weekly settlement workflow using order and payment records.

Quality and traceability (P6) provides a separate process for handling reported food-quality incidents using relevant product, inventory and order information.

The model identifies the Producer and Customer as black-box pools, reflecting the decision to focus on the marketplace's internal processes rather than the participants' internal workflows. It also includes the Organic Certification Verification Service and External Payment Services to show the marketplace's dependencies on external services.

The strategic BPMN provides a high-level view of the processes and their interactions. Detailed validation rules, stock management behaviour, multi-producer order handling, settlement calculations and incident investigation procedures can be elaborated in the functional requirements and implementation models.
