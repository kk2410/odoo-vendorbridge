# odoo-vendorbridge
 VendorBridge – Smart Procurement & Vendor Management ERP

VendorBridge is a modern Procurement & Vendor Management ERP platform built with Django. It streamlines the complete procurement lifecycle by connecting procurement managers and vendors on a single digital platform.

The system enables organizations to publish RFQs (Request for Quotations), receive vendor quotations, compare bids intelligently, generate purchase orders, manage invoices, and monitor procurement performance through analytics.

---

 Key Features

 Vendor Management

- Vendor Registration & Onboarding
- GST Verification Support
- Vendor Category Management
- Vendor Rating System
- Vendor Profile Tracking

 RFQ Management

- Create and Publish RFQs
- Product Quantity & Requirement Specification
- Vendor Selection for RFQ Distribution
- RFQ Status Tracking

 Quotation Management

- Vendors can submit quotations digitally
- Multiple quotations for comparison
- Structured quotation workflow
- Approval-ready quotation records

 Smart Bid Scoring Engine

Automatic quotation evaluation based on:

- 50% Price
- 30% Delivery Timeline
- 20% Vendor Rating

Helps procurement teams make faster and more objective decisions.

 Purchase Order Management

- Generate Purchase Orders
- Track Order Status
- Procurement Workflow Automation
- Order History Management

 Approval Workflow

- Manager Approval System
- Role-Based Authorization
- Procurement Governance

 Analytics Dashboard

- Vendor Statistics
- RFQ Analytics
- Purchase Order Insights
- Procurement Performance Metrics

---

 User Roles

Manager

- Publish RFQs
- Review Quotations
- Approve Procurement Requests
- Generate Purchase Orders
- Monitor Analytics

Vendor

- Register on Platform
- View Assigned RFQs
- Submit Quotations
- Track Purchase Orders
- Manage Company Profile

---

 Technology Stack

Backend

- Python
- Django
- SQLite

Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

Tools

- Git
- GitHub
- VS Code

---

 Project Modules

- Accounts
- Vendors
- RFQ
- Quotations
- Purchase Orders
- Invoices
- Approvals
- Notifications
- Analytics Dashboard

---

 Security Features

- Django Authentication
- Role-Based Access Control
- Protected Routes
- Session Management
- Secure Form Validation

---

 Installation

git clone https://github.com/yourusername/vendorbridge.git

cd vendorbridge

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Open:

http://127.0.0.1:8000/

---

 Problem Statement

Organizations often struggle with fragmented procurement processes, manual vendor communication, quotation comparisons, and approval delays.

VendorBridge solves these challenges by providing a centralized ERP platform that digitizes vendor onboarding, RFQ publishing, quotation evaluation, purchase order generation, and procurement analytics.

---

 Future Enhancements

- Email Notifications
- AI-based Vendor Recommendation
- Predictive Procurement Analytics
- Payment Gateway Integration
- Document Upload & Verification
- Multi-Organization Support
- Cloud Deployment

---

 Developed For

Odoo Hackathon 2026

VendorBridge demonstrates how digital procurement transformation can improve transparency, efficiency, and vendor collaboration through a unified ERP ecosystem.
