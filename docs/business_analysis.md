# Business Process and Organisational Responsibilities Analysis

## 1. Analysis of the Business

The Bristol Regional Food Network (BRFN) is a community initiative connecting local food producers with consumers within twenty miles of Bristol city centre. Approximately forty small-to-medium producers currently struggle to reach customers beyond farmers' markets and farm-gate sales. The digital marketplace is intended to help these producers reach a wider customer base.

The network serves three main customer segments:

- Young professionals and families
- Community groups
- Independent restaurants and cafés

The marketplace supports product listing, product discovery, order management, payment processing, producer settlements, order fulfilment coordination, and quality and traceability management.

## 2. Analysis of Major Business Processes

### P1. Product Listing and Inventory Management

Producers submit product information to the marketplace, which validates and maintains product listings. The marketplace also manages inventory and seasonal availability so customers can view current product information and availability.

#### Triggers

- A producer submits a request to list a new product.
- A producer requests an inventory or seasonal availability update.

#### Main Steps: Product Listing and Validation

1. The producer submits a product listing request containing the relevant product information.
2. The marketplace receives the request and validates the submitted information.
3. Where a product is labelled organic, the marketplace requests verification from the organic certification verification service.
4. The verification service returns a result to the marketplace.
5. The listing request is processed, and the product catalogue is updated accordingly.

#### Main Steps: Inventory and Seasonal Availability

1. The producer submits an inventory update request.
2. The marketplace receives the request and manages inventory and seasonal availability.
3. The product catalogue and inventory records are updated.
4. The inventory update process is completed.

#### Outcome

Product listing requests and inventory update requests are processed, allowing the marketplace to maintain product information and availability records.

#### Exceptions and Dependencies

- Missing or invalid product information.
- Unsuccessful organic certification verification.
- Organic certification verification service unavailability.
- Invalid inventory or seasonal availability information.

The diagram represents the organic certification verification service as an external participant. Detailed validation rules and exception handling can be specified in the functional requirements.

### P2. Product Browsing and Discovery

Customers use the marketplace to browse and search for available products. The marketplace retrieves product information from the product catalogue and inventory records and displays relevant information to customers.

#### Trigger

A customer requests product browsing or search.

#### Main Steps

1. The marketplace receives a product browsing request.
2. The platform provides product browsing and search functionality.
3. Product information is retrieved from the product catalogue and inventory records.
4. Relevant product information is displayed to the customer.

#### Outcome

Customers can discover products and view the information made available through the marketplace.

#### Exceptions

- No matching products are available.
- Product information is missing or outdated.
- A product becomes unavailable before an order is placed.

### P3. Order Processing

The marketplace manages customer orders and coordinates the transition from checkout to payment and fulfilment. The process interacts with the product catalogue, inventory records, and order and payment records.

#### Trigger

A customer submits a checkout request.

#### Main Steps

1. The marketplace receives the customer checkout request.
2. The marketplace manages the customer order using the relevant product, inventory, order and payment information.
3. The order proceeds to customer payment processing.
4. The marketplace evaluates the payment result.
5. If payment is successful, the marketplace proceeds to order fulfilment coordination.
6. If payment is unsuccessful, the marketplace handles the unsuccessful payment and the order is not confirmed.

#### Outcome

The marketplace coordinates the order process according to the payment result. Successful payment allows the order to proceed towards fulfilment, while unsuccessful payment is handled separately.

#### Exceptions

- Payment is declined or unsuccessful.
- Product availability changes before checkout is completed.
- The order cannot proceed because relevant product or inventory information is unavailable.

The current BPMN diagram represents order management as a high-level activity. Detailed behaviours such as splitting a multi-producer basket into producer-specific sub-orders, checking the minimum 48-hour preparation period, and reserving or reducing stock should be specified in the functional requirements if they are included in the agreed system scope.

### P4. Payment and Producer Settlement

The marketplace coordinates customer payment processing and manages producer settlements. It maintains order and payment records to support financial operations.

The business model specifies a five per cent commission for BRFN, alongside producer payments and weekly settlement arrangements.

#### Triggers

- A customer checkout request initiates payment processing.
- A weekly settlement timer triggers the producer settlement process.

#### Main Steps: Customer Payment

1. The marketplace processes the customer payment request.
2. The payment request is sent to the external payment service.
3. The external service returns the payment processing result.
4. The marketplace evaluates whether payment was successful.
5. If payment succeeds, the order proceeds towards fulfilment.
6. If payment fails, the marketplace handles the unsuccessful payment and the order is not confirmed.

#### Main Steps: Producer Settlements

1. The weekly settlement timer triggers the settlement process.
2. The marketplace manages producer settlements using the available order and payment records.
3. The settlement process is completed.

#### Outcome

Customer payment outcomes are handled by the marketplace, and producer settlements are processed through a separate weekly settlement workflow.

#### Exceptions and Dependencies

- Declined or unsuccessful customer payment.
- Failed producer payout.
- Refunds or disputed orders.
- Incomplete or inaccurate financial records.

The BPMN diagram represents the external payment service and the weekly settlement trigger. Detailed commission calculations, producer payment allocations, settlement statements and audit records should be specified in the functional requirements.

The assumption that only fulfilled orders qualify for settlement requires confirmation from BRFN.

### P5. Order Fulfilment

The marketplace coordinates order fulfilment after successful customer payment. The process communicates order confirmation and fulfilment details to the customer and coordinates the relevant fulfilment arrangements.

#### Trigger

The payment process indicates that the customer payment was successful.

#### Main Steps

1. The marketplace proceeds from the successful-payment path to order fulfilment coordination.
2. The marketplace coordinates fulfilment using the relevant order details.
3. Order confirmation and fulfilment details are communicated to the customer.
4. The order fulfilment process is completed.

#### Outcome

The marketplace coordinates the fulfilment process and communicates relevant information to the customer.

#### Exceptions

- A producer cannot fulfil an order.
- Delivery or collection is delayed.
- A collection is missed.
- Only part of a multi-producer order is fulfilled.

The current BPMN diagram models fulfilment coordination at a high level. The detailed activities performed by producers, including product preparation, delivery or collection, and individual fulfilment status updates, are not modelled as internal producer activities because the Producer is represented as a black-box pool.

The precise responsibility for arranging delivery or collection must be agreed with BRFN.

### P6. Quality and Traceability

The marketplace manages food-quality incidents and traceability using product information, order records and relevant information about producers and customers.

Product listing and inventory management provide product information, while order and payment records support the identification of relevant transactions.

#### Trigger

A food-quality incident is reported by a relevant participant.

#### Main Steps

1. The marketplace receives a food-quality incident report.
2. The incident is handled through the food-quality incident and traceability process.
3. Relevant product, inventory and order information is used to support the investigation.
4. The marketplace communicates relevant food-safety information where appropriate.
5. Incident handling is completed.

#### Outcome

Food-quality incidents can be managed using the information available within the marketplace, supporting investigation and traceability.

#### Exceptions

- Incomplete product or traceability information.
- Insufficient order records to identify affected customers.
- Difficulty obtaining the information required to investigate an incident.

The current diagram represents food-quality incident management and traceability as a dedicated process. The exact investigation steps, customer notification procedures and any regulatory reporting requirements should be specified in the functional requirements and confirmed with BRFN.

## 3. Relationships Between Business Processes

The business processes are connected through shared product information, inventory records, order and payment records, and communications between the marketplace and its external participants.

### Product Listing, Inventory and Browsing

Product listing and inventory management (P1) maintains the information used by product browsing and discovery (P2). Product information and availability records support the marketplace's ability to display relevant information to customers.

### Browsing and Order Processing

Product browsing and discovery (P2) enables customers to find products through the marketplace. Customer checkout requests initiate order processing (P3), which uses the relevant product, inventory and order information.

### Order Processing and Payment

Order processing (P3) connects to payment processing (P4). The marketplace evaluates the payment result to determine whether the order can proceed. Successful payment allows the order to progress towards fulfilment, while unsuccessful payment is handled separately and the order is not confirmed.

### Payment and Fulfilment

Successful payment allows the marketplace to proceed to order fulfilment coordination (P5). The marketplace coordinates fulfilment and communicates order confirmation and fulfilment details to the customer.

### Payment and Producer Settlement

Producer settlements (P4) are managed through a separate workflow triggered by the weekly settlement timer. The process uses order and payment records. The eligibility rules for settlement, including whether an order must be fulfilled before payment to the producer, require confirmation from BRFN.

### Product Information and Traceability

Product listing and inventory management (P1) maintains product information, while quality and traceability (P6) uses relevant product and order records to support food-quality investigations. The availability and accuracy of these records are important for identifying products and participants associated with an incident.

Overall, these relationships show how the marketplace coordinates its core activities using shared information and communications. The BPMN diagram focuses on the major processes and their relationships rather than modelling every detailed system interaction.

## 4. Organisational Responsibilities

Operating the BRFN digital marketplace requires coordination between producers, customers, BRFN administrators, financial operations and the supporting software platform.

- **Producers:** Submit product listing requests, maintain product information and inventory, and provide relevant information when required for order fulfilment or quality investigations. Their internal activities are outside the detailed scope of the current BPMN diagram.
- **Customers:** Request product browsing, submit checkout requests and receive relevant order confirmation, fulfilment information and food-quality communications.
- **BRFN administrators:** Oversee marketplace operations and support the management of operational or food-quality incidents. Specific administrative approval and escalation responsibilities require confirmation.
- **Financial operations:** Support customer payment processing, producer settlements and the maintenance of appropriate financial records.
- **Marketplace platform:** Performs or coordinates the activities represented in the BPMN diagram, including product listing validation, inventory management, product browsing, customer order management, payment handling, fulfilment coordination, producer settlements and food-quality incident management.
- **External service providers:** Support specific processes, including organic certification verification and customer payment processing.

The Producer and Customer are represented as black-box pools in the strategic BPMN. This means their internal workflows are not modelled in detail; instead, their interactions with the marketplace are represented through message flows.

The responsibilities of business participants should be distinguished from automated activities performed by the software. The platform supports the business processes, while accountability for business decisions and exceptions belongs to the appropriate business role.

## 5. External Services and Dependencies

The current BPMN diagram includes two external services or participants that support marketplace operations.

- **Organic Certification Verification Service:** Receives verification requests from the product listing process and returns certification verification results. This supports the validation of organic product claims.
- **External Payment Services:** Receives payment processing requests and returns payment processing results. The payment workflow should be developed and tested using sandbox or simulated payment environments rather than live payment systems.

The diagram also includes the Producer and Customer as external participants. Their interactions with the marketplace are represented through labelled message flows, while their internal workflows remain outside the current model.

## 6. Implications for the Strategic BPMN

The strategic BPMN represents the major internal business processes required to operate the BRFN digital marketplace and the interactions between the marketplace and its external participants.

The model begins with product listing and inventory management (P1), which maintains product information and availability. Product browsing and discovery (P2) enables customers to request and view product information. Customer checkout requests initiate order processing (P3), which connects to customer payment processing (P4).

The payment decision determines whether the order can proceed. Successful payment allows the marketplace to coordinate order fulfilment (P5), while unsuccessful payment is handled through a separate path and the order is not confirmed. Producer settlements are managed through a weekly settlement workflow using order and payment records.

Quality and traceability (P6) provides a separate process for handling reported food-quality incidents using relevant product, inventory and order information.

The model identifies the Producer and Customer as black-box pools, reflecting the decision to focus on the marketplace's internal processes rather than the participants' internal workflows. It also includes the Organic Certification Verification Service and External Payment Services to show the marketplace's dependencies on external services.

The strategic BPMN provides a high-level view of the processes and their interactions. Detailed validation rules, stock management behaviour, multi-producer order handling, settlement calculations and incident investigation procedures can be elaborated in the functional requirements and implementation models.

Sustainability and community engagement activities, including food-miles reporting, surplus produce offers and community content, are not represented as a dedicated process in the current BPMN diagram. If these capabilities remain within the agreed system scope, they should be documented separately as supporting requirements or covered in a separate process model.