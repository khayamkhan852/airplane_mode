# ✈️ Airplane Mode

**Airplane Mode** is a full-featured custom app built with the [Frappe Framework](https://frappeframework.com), developed during a full stack course. It simulates a complete airline ticketing and shop management system.

---

## 🚀 Features

### ✈️ Airline & Flight Module
- Manage Airlines, Airplanes, and Flights
- Link Crew Members and Passengers
- Ticket Booking with Add-ons

### 🧍 Crew Management
- Define Crew Types
- Assign Crew to Flights

### 🎫 Ticketing System
- Flight ticket booking
- Web Form for public booking (`book_ticket_web_form`)
- Add-on items and types

### 🛒 In-Flight Shop Management
- Shops per Airport
- Contracts, Rent, Payments
- Shop Settings and Tenants
- Shop Lead Management (with `shop_lead_form`)

### 🔔 Notifications & Reports
- Custom Notification for flight departure
- Reports like:
  - Revenue by Airline
  - Add-on Popularity
  - Airport Shop Availability

---

## 📁 Folder Structure

| Folder | Purpose |
|--------|---------|
| `airplane_mode/doctype/` | All main airline-related doctypes |
| `shop_managment/doctype/` | Shop contract, rent, and tenant doctypes |
| `web_form/` | Public web forms for booking |
| `notification/` | Custom Frappe notifications |
| `report/` | Script and Query reports |
| `fixtures/` | Preloaded data like `crew_type`, `shop_type` |
| `public/` | Custom CSS and JS assets |
| `workspace/` | Custom Frappe workspace views |

---

## 🛠️ Technologies

- Frappe Framework (v15)
- Python
- MariaDB / Redis
- HTML, CSS (custom styles)
- JavaScript (client-side logic)

---

## ⚙️ Setup Guide

```bash
# In your Frappe bench
cd frappe-bench

# Get the app (if from GitHub)
bench get-app airplane_mode https://github.com/khayamkhan852/airplane_mode.git

# Install the app
bench --site yoursite.local install-app airplane_mode

# Run server
bench start
