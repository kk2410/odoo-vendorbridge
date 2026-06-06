import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendorbridge.settings')
django.setup()

from django.contrib.auth import get_user_model
from vendors.models import Vendor
from rfq.models import RFQ
import datetime

User = get_user_model()

def run():
    print("Starting database seeding...")
    
    # 1. Create Custom Users
    users = [
        ('admin', 'admin@vendorbridge.local', 'admin123', 'admin', 'System', 'Admin'),
        ('procurement', 'procurement@vendorbridge.local', 'procurement123', 'procurement', 'Paul', 'Procurement'),
        ('manager', 'manager@vendorbridge.local', 'manager123', 'manager', 'Mark', 'Manager'),
        ('nexus_vendor', 'nexus@vendorbridge.local', 'vendor123', 'vendor', 'Ned', 'Nexus'),
        ('apex_vendor', 'apex@vendorbridge.local', 'vendor123', 'vendor', 'Amy', 'Apex'),
    ]
    
    for username, email, pwd, role, f_name, l_name in users:
        user, created = User.objects.get_or_create(username=username, defaults={
            'email': email,
            'role': role,
            'first_name': f_name,
            'last_name': l_name,
            'is_staff': True if role == 'admin' else False,
            'is_superuser': True if role == 'admin' else False
        })
        if created:
            user.set_password(pwd)
            user.save()
            print(f"Created user: {username} ({role})")
        else:
            print(f"User {username} already exists")

    # 2. Create Vendor Profiles for Vendor Users
    v1_user = User.objects.get(username='nexus_vendor')
    v1_profile, created = Vendor.objects.get_or_create(user=v1_user, defaults={
        'company_name': 'Nexus IT Solutions',
        'category': 'it',
        'gst_number': '27ABCDE1234F1Z1',
        'contact_person': 'Ned Nexus',
        'email': 'nexus@vendorbridge.local',
        'phone_number': '9876543210',
        'address': 'Tech Building 4, Hitec City, Hyderabad',
        'rating': 4.80,
        'status': 'active'
    })
    if created:
        print("Created Vendor Profile: Nexus IT Solutions")

    v2_user = User.objects.get(username='apex_vendor')
    v2_profile, created = Vendor.objects.get_or_create(user=v2_user, defaults={
        'company_name': 'Apex Office Supplies',
        'category': 'office',
        'gst_number': '27ABCDE5678F1Z2',
        'contact_person': 'Amy Apex',
        'email': 'apex@vendorbridge.local',
        'phone_number': '8765432109',
        'address': 'Industrial Sector 5, Mumbai',
        'rating': 4.20,
        'status': 'active'
    })
    if created:
        print("Created Vendor Profile: Apex Office Supplies")

    # Offline Vendor Profile
    v3_profile, created = Vendor.objects.get_or_create(company_name='Super Logistics Corp', defaults={
        'category': 'logistics',
        'gst_number': '27ABCDE9012F1Z3',
        'contact_person': 'Leo Logistics',
        'email': 'leo@superlogistics.local',
        'phone_number': '7654321098',
        'address': 'Shipping Yard, Port Area, Chennai',
        'rating': 3.90,
        'status': 'active'
    })
    if created:
        print("Created Offline Vendor Profile: Super Logistics Corp")

    # 3. Create Sample RFQs
    proc_user = User.objects.get(username='procurement')
    rfq1, created = RFQ.objects.get_or_create(
        title="Procurement of Laptops for Developers",
        defaults={
            'description': "Requesting quotations for 15 Developer Laptops. Specs:\n- 32GB RAM\n- 1TB SSD\n- Intel i7 or Apple M3 equivalent\n- 3 years warranty",
            'product_name': "Developer Laptops",
            'quantity': 15,
            'deadline': datetime.date.today() + datetime.timedelta(days=15),
            'status': 'published',
            'created_by': proc_user
        }
    )
    if created:
        rfq1.assigned_vendors.add(v1_profile, v2_profile)
        print("Created RFQ: Procurement of Laptops for Developers")

    rfq2, created = RFQ.objects.get_or_create(
        title="Office Chairs and Ergonomic Desks",
        defaults={
            'description': "Requesting quotes for 50 Ergonomic Office Chairs and 50 Adjustable Desks for head office renovation.",
            'product_name': "Renovation Office Furniture",
            'quantity': 50,
            'deadline': datetime.date.today() + datetime.timedelta(days=10),
            'status': 'draft',
            'created_by': proc_user
        }
    )
    if created:
        rfq2.assigned_vendors.add(v2_profile)
        print("Created Draft RFQ: Office Chairs and Ergonomic Desks")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    run()
