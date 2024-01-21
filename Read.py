from BikeRentalBackend import cursor
from Setup import DB_NAME
import pandas as pd
import streamlit as st

# ------------------------------------------------------------------------------------------------
# Driver's Info
# ------------------------------------------------------------------------------------------------
def driverFormat(data):
    drivers = []
    for driver in data:
        drivers.append({
            "DL": driver[0],
            "Name": driver[1],
            "DOB": driver[2],
            "Experience": driver[3],
            "Available": driver[4],
        })
    return drivers

def getDriverCost(experience):
    cursor.execute(f"use {DB_NAME}")
    query = (" select driver_charge(%s)")
    cursor.execute(query, (experience,))
    driverFare = cursor.fetchone()
    return driverFare

def getAllDriversUI():
    with st.container():
        with st.expander("Show All Driver's details"):
            st.table(pd.DataFrame(getAllDrivers()))

def getDriverByDLUI():
    with st.container():
        dl = st.selectbox("Select DL no.", options=[driver["DL"] for driver in getAllDrivers()])
        with st.expander("Show Driver details"):
            st.table(pd.DataFrame(getDriverByDL(dl)))

def getAllDrivers():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_info")
    cursor.execute(query)
    allDrivers = cursor.fetchall()
    allDrivers = driverFormat(allDrivers)
    # allDrivers = pd.DataFrame(allDrivers)
    return allDrivers

def getDriverByDL(DL):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_info where dl_number = %s")
    cursor.execute(query, (DL,))
    allDrivers = cursor.fetchall()
    allDrivers = driverFormat(allDrivers)
    # allDrivers = pd.DataFrame(allDrivers)
    return allDrivers

def getAVailableDrivers():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_info where available = true")
    cursor.execute(query)
    allDrivers = cursor.fetchall()
    allDrivers = driverFormat(allDrivers)
    # allDrivers = pd.DataFrame(allDrivers)
    return allDrivers
# -----------------------------------------------------------------------------------------------------
# Driver's Contact's
# -----------------------------------------------------------------------------------------------------
def driverContactsFormat(data):
    contacts = []
    for contact in data:
        contacts.append({
            "DL": contact[0],
            "Contact": contact[1]
        })
    return contacts

def getDriverContactByDLUI():
    dl = st.selectbox("Select DL no.", options=[driver["DL"] for driver in getAllDrivers()])
    with st.expander("Driver's Contacts"):
        st.table(pd.DataFrame(getDriverContactByDL(dl)))

def getDriverContactByDL(DL):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_contacts where dl_number = %s")
    cursor.execute(query, (DL,))
    allcontacts = cursor.fetchall()
    allcontacts = driverContactsFormat(allcontacts)
    return allcontacts

def getAllDriverContactsUI():
    with st.expander("Driver's Contacts"):
        st.table(pd.DataFrame(getAllDriverContacts()))

def getAllDriverContacts():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_contacts")
    cursor.execute(query)
    allcontacts = cursor.fetchall()
    allcontacts = driverContactsFormat(allcontacts)
    return allcontacts

def getDLByContact(contact):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from driver_contacts where phone_no = %s")
    cursor.execute(query, (contact,))
    allcontacts = cursor.fetchall()
    allcontacts = driverContactsFormat(allcontacts)
    # print("allcontacts: ", allcontacts)
    return allcontacts

# ----------------------------------------------------------------------------------------------
# Customer Details
# ----------------------------------------------------------------------------------------------

def getAllCustomersUI():
    with st.expander("Customer Details"):
        st.table(pd.DataFrame(getAllCustomers()))

def formatCustomers(data):
    customers = []
    for customer in data:
        customer_data = {}
        customer_data["Customer ID"] = customer[0]
        customer_data["DL No."] = customer[1]
        customer_data["Firstname"] = customer[2]
        customer_data["Lastname"] = customer[3]
        customer_data["Phone No."] = customer[4]
        customer_data["Username"] = customer[5]
        customer_data["Password"] = "*********"
        customer_data["DOB"] = customer[7]
        customer_data["Email"] = customer[8]
        customer_data["State"] = customer[9]
        customer_data["City"] = customer[10]
        customer_data["Street"] = customer[11]
        customer_data["Zipcode"] = customer[12]
        customers.append(customer_data)
    return customers

def getCustomerByUsernameUI():
    username = st.selectbox("Select DL no.", options=[customer["Username"] for customer in getAllCustomers()])
    with st.expander("Customer Details's"):
        st.table(pd.DataFrame(getCustomerByUsername(username)))

def getAllCustomers():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from customer_info")
    cursor.execute(query)
    allcustomers = cursor.fetchall()
    allcustomers = formatCustomers(allcustomers)
    # print(allcustomers)
    return allcustomers

def getCustomerByUsername(username):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from customer_info where username = %s")
    cursor.execute(query, (username,))
    allcustomers = cursor.fetchall()
    allcustomers = formatCustomers(allcustomers)
    # print(allcustomers)
    return allcustomers

# ---------------------------------------------------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------------------------------------------------
def formatLocations(data):
    locations = []
    for location in data:
        location_data = {}
        location_data["Location Id"] = location[0]
        location_data["Location Name"] = location[1]
        location_data["State"] = location[2]
        location_data["City"] = location[3]
        location_data["Street"] = location[4]
        location_data["Zipcode"] = location[5]
        locations.append(location_data)
    return locations

def getAllLocations():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from locations")
    cursor.execute(query)
    allLocations = cursor.fetchall()
    allLocations = formatLocations(allLocations)
    # print(allLocations)
    return allLocations

def getLocationByName(locationName):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from locations where location_name = %s")
    cursor.execute(query, (locationName, ))
    allLocations = cursor.fetchall()
    allLocations = formatLocations(allLocations)
    # print(allLocations)
    return allLocations

def getAllLocationsUI():
    with st.expander("Location Details"):
        st.table(pd.DataFrame(getAllLocations()))

def getLocationByNameUI():
    location_name = st.selectbox("Select Location Name", options=[location["Location Name"] for location in getAllLocations()])
    with st.expander("Location Details's"):
        st.table(pd.DataFrame(getLocationByName(location_name)))

# --------------------------------------------------------------------------------------------------------------------------------------
# Bike category
# --------------------------------------------------------------------------------------------------------------------------------------
def formatBikeCateory(data):
    categories = []
    for category in data:
        bike_category = {}
        bike_category["Name"] = category[0]
        bike_category["NoPersons"] = category[1]
        bike_category["CostPerDay"] = category[2]
        bike_category["LateFee"] = category[3]
        categories.append(bike_category)
    return categories


def getAllBikeCategoriesUI():
    with st.expander("Bike Categories"):
        st.table(pd.DataFrame(getAllBikeCategories()))

def getAllBikeCategoryByNameUI():
    category_name = st.selectbox("Select Category Name", [category["Name"] for category in getAllBikeCategories()])
    with st.expander("Bike Categories"):
        st.table(pd.DataFrame(getBikeCategoryByName(category_name)))

def getAllBikeCategories():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from bike_category")
    cursor.execute(query)
    all_categories = cursor.fetchall()
    all_categories = formatBikeCateory(all_categories)
    # print(all_categories)
    return all_categories

def getBikeCategoryByName(category_name):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from bike_category where category_name = %s")
    cursor.execute(query, (category_name,))
    all_categories = cursor.fetchall()
    all_categories = formatBikeCateory(all_categories)
    # print(all_categories)
    return all_categories

# ------------------------------------------------------------------------------------------------------------------------
# Bike details
# ------------------------------------------------------------------------------------------------------------------------
def formatBikeDetails(data):
    bikes = []
    for bike in data:
        bikes_details = {}
        bikes_details["Registration No"] = bike[0]
        bikes_details["Model Name"] = bike[1]
        bikes_details["Make"] = bike[2]
        bikes_details["Model Year"] = bike[3]
        bikes_details["Mileage"] = bike[4]
        bikes_details["Available"] = bike[5]
        bikes_details["Category"] = bike[6]
        bikes_details["Location Id"] = bike[5]
        bikes.append(bikes_details)
    return bikes

def getAllBikesUI():
    with st.expander("Bikes"):
        st.table(pd.DataFrame(getAllBikes()))

def getAllBikeByModelNameUI():
    model_name = st.selectbox("Select Model Name", [bike["Model Name"] for bike in getAllBikes()])
    with st.expander("Bikes"):
        st.table(pd.DataFrame(getBikeByModelName(model_name)))

def getAllBikes():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from bike_details")
    cursor.execute(query)
    all_categories = cursor.fetchall()
    all_categories = formatBikeDetails(all_categories)
    # print(all_categories)
    return all_categories

def getBikeByModelName(model_name):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from bike_details where model_name = %s")
    cursor.execute(query, (model_name,))
    all_categories = cursor.fetchall()
    all_categories = formatBikeDetails(all_categories)
    # print(all_categories)
    return all_categories

def getBikeByRegNo(reg_no):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from bike_details where registration_no = %s")
    cursor.execute(query, (reg_no,))
    all_categories = cursor.fetchall()
    all_categories = formatBikeDetails(all_categories)
    # print(all_categories)
    return all_categories

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Discount
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def formatDiscountCoupon(data):
    coupons = []
    for bike in data:
        coupon_details = {}
        coupon_details["coupon_code"] = bike[0]
        coupon_details["coupon_name"] = bike[1]
        coupon_details["discount_percentage"] = bike[2]
        coupon_details["expiry_date"] = bike[3]
        coupons.append(coupon_details)
    return coupons

def getAllDiscountCouponsUI():
    with st.expander("Coupons"):
        st.table(pd.DataFrame(getAllDiscountCoupons()))

def getDiscountCouponByCodeUI():
    coupon_code = st.selectbox("Select coupon code", [coupon["coupon_code"] for coupon in getAllDiscountCoupons()])
    with st.expander("Coupons"):
        st.table(pd.DataFrame(getDiscountCouponByCode(coupon_code)))

def getAllDiscountCoupons():
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from discount")
    cursor.execute(query)
    all_categories = cursor.fetchall()
    all_categories = formatDiscountCoupon(all_categories)
    # print(all_categories)
    return all_categories

def getDiscountCouponByCode(coupon_code):
    cursor.execute(f"use {DB_NAME}")
    query = ("select * from discount where coupon_code = %s")
    cursor.execute(query, (coupon_code,))
    all_categories = cursor.fetchall()
    all_categories = formatDiscountCoupon(all_categories)
    # print(all_categories)
    return all_categories

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# All Bikes with Category
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bikesWithCategoryFormat(data):
    availableBikes = []
    for bike in data:
        bike_schema = {}
        bike_schema["RegistrationNo"] = bike[0]
        bike_schema["ModelName"] = bike[1]
        bike_schema["Make"] = bike[2]
        bike_schema["ModelYear"] = bike[3]
        bike_schema["Mileage"] = bike[4]
        bike_schema["Category"] = bike[6]
        bike_schema["NoOfPersons"] = bike[9]
        bike_schema["CostPerDay"] = bike[10]
        bike_schema["LateFeePerHour"] = bike[11]
        availableBikes.append(bike_schema)
    return availableBikes

def getAllBikesWithCategory():
    cursor.execute(f"use {DB_NAME}")
    selectQuery = (
        "select * from bike_details, bike_category where category = category_name and available = true order by cost_per_day")
    cursor.execute(selectQuery)
    res = cursor.fetchall()
    availableBikes = bikesWithCategoryFormat(res)
    return availableBikes

# ------------------------------------------------------------------------------------------------------------------------------------
# Booking details
# ------------------------------------------------------------------------------------------------------------------------------------
def bookingFormat(data):
    bookings = []
    for booking in data:
        new_booking = {}
        new_booking["Booking Id"] = booking[0]
        new_booking["From"] = booking[1]
        new_booking["To"] = booking[2]
        new_booking["Basic Fare"] = booking[3]
        new_booking["Discount(%)"] = booking[4]
        new_booking["Booking Status"] = booking[5]
        new_booking["With Driver"] = booking[6]
        new_booking["Actual Return Date"] = booking[7]
        new_booking["Pickup Location"] = booking[8]
        new_booking["Drop Location"] = booking[9]
        new_booking["Coupon code"] = booking[10]
        new_booking["Bike RegNo."] = booking[11]
        new_booking["Customer Id"] = booking[12]
        new_booking["Booked On"] = booking[13]
        bookings.append(new_booking)
    return bookings

def AllBookingDetailsUI():
    with st.expander("All Bookings"):
        st.table(pd.DataFrame(AllBookingDetails()))

def AllBookingDetails():
    cursor.execute(f"use {DB_NAME}")
    selectQuery = (
        "select * from booking_details")
    cursor.execute(selectQuery)
    res = cursor.fetchall()
    bookings = bookingFormat(res)
    return bookings

def getBookingDetailsById(id):
    cursor.execute(f"use {DB_NAME}")
    selectQuery = (
        "select * from booking_details where booking_id = %s")
    cursor.execute(selectQuery, (id,))
    res = cursor.fetchall()
    bookings = bookingFormat(res)
    return bookings