from Read import getDriverByDL, getAllDriversUI, getAllDrivers, getAllDriverContactsUI, getAllDriverContacts, getDLByContact, getCustomerByUsername, getAllCustomersUI, getAllCustomers, getLocationByName, getAllLocations, getAllLocationsUI, getAllBikeCategoriesUI, getAllBikeCategories, getBikeCategoryByName, getBikeByRegNo, getAllBikes, getAllBikesUI, getAllDiscountCoupons, getDiscountCouponByCode, getAllDiscountCouponsUI, AllBookingDetails, getBookingDetailsById, AllBookingDetailsUI

import streamlit as st
import datetime
from BikeRentalBackend import cursor, db
from Setup import DB_NAME
import pandas as pd

def UpdateDriverUI():
    with st.container():
        getAllDriversUI()
        selected_driver = st.selectbox("Select Driver To Update", options=[driver["DL"] for driver in getAllDrivers()])
        driverdata = getDriverByDL(selected_driver)
        # st.write(driverdata)
        driverdata = driverdata[0]
        newDriverdata = {}
        st.write("Update Driver Details")
        dl_numberUI, driver_dobUI = st.columns([3, 2])
        driver_nameUI, driver_experienceUI = st.columns(2)

        dl_number = dl_numberUI.text_input(
            label="Driving License Number", placeholder="Enter Driving License No.",  max_chars=16, value=driverdata["DL"], disabled=True)
        newDriverdata["dl_number"] = dl_number

        driver_dob = driver_dobUI.date_input(label="Date of birth", min_value=datetime.date(
            1950, 1, 1), max_value=datetime.date.today(), value= driverdata["DOB"])
        newDriverdata["driver_dob"] = str(driver_dob)

        driver_name = driver_nameUI.text_input(
            label="Driver's Name", placeholder="Driver's Name", value=driverdata["Name"])
        newDriverdata["driver_name"] = driver_name

        driver_experience = driver_experienceUI.number_input(
            "Driving Experience", min_value=2, value=driverdata["Experience"])
        newDriverdata["driver_experience"] = driver_experience

        driver_available = st.selectbox(
            "Availability", options=[True, False], index = ([1, 0].index(int(driverdata["Available"]))))
        newDriverdata["driver_available"] = driver_available

        if st.button("Update Driver"):
            UpdateDriver(driverdata=newDriverdata)

def UpdateDriver(driverdata):
    # st.write(driverdata)
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update driver_info set driver_name = %s, driver_dob = %s, driving_experience = %s, available = %s where dl_number = %s"
    )
    cursor.execute(query, (driverdata["driver_name"], str(driverdata["driver_dob"]), driverdata["driver_experience"], driverdata["driver_available"], driverdata["dl_number"]))
    db.commit()
    st.success("Updated Successfully", icon="✅")
    getAllDriversUI()



def UpdateDriverContactUI():
    getAllDriverContactsUI()
    selected_contact = st.selectbox("Select Contact To Update", options=[contact["Contact"] for contact in getAllDriverContacts()])
    newdata = {}
    st.write(selected_contact)
    driverdata = getDLByContact(selected_contact)
    driverdata = driverdata[0]
    dl_numberUI, contact_no = st.columns([3, 2])
    
    dl_numberUI.text_input(
            label="Driving License Number", placeholder="Enter Driving License No.",  max_chars=16, value=driverdata["DL"], disabled=True)
    newContact = contact_no.text_input("Enter New Phone Number", placeholder="Enter Phone Number", max_chars=10)
    newdata["selected_contact"] = selected_contact
    newdata["new_contact"] = newContact
    newdata["DL"] = driverdata["DL"]

    if st.button("Update Contact"):
        # st.write(newdata)
        UpdateDriverContact(newdata)

def UpdateDriverContact(driverdata):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update driver_contacts set phone_no = %s where dl_number = %s and phone_no = %s"
    )
    cursor.execute(query, (driverdata["new_contact"], driverdata["DL"], driverdata["selected_contact"],))
    db.commit()
    st.success("Updated Successfully", icon="✅")
    getAllDriverContactsUI()

# --------------------------------------------------------------------------------------------------------------------
# Customer's details
# --------------------------------------------------------------------------------------------------------------------

def UpdateCustomerUI():
    all_customers = getAllCustomers()
    with st.expander("Before Update"):
        st.table(pd.DataFrame(all_customers))
    username = st.selectbox("Select Username to Update", options= [customer["Username"] for customer in all_customers])
    newdata = {}
    olddata = getCustomerByUsername(username= username)[0]
    newdata["username"] = olddata["Username"]
    registerContainer = st.container()
    with registerContainer:
        firstnameUI, lastnameUI = st.columns(2)
        licenseNoUI, dobUI = st.columns([3, 2])
        usernameUI, phoneNoUI = st.columns(2)
        passwordUI, confirmPasswordUI = st.columns(2)
        stateUI, cityUI = st.columns(2)
        zipcodeUI, streetUI = st.columns(2)

        newdata["firstname"] = firstnameUI.text_input(
            label="Firstname", placeholder="Enter Firstname", value=olddata["Firstname"])
        newdata["lastname"] = lastnameUI.text_input(
            label="Lastname", placeholder="Enter Lastname", value=olddata["Lastname"])
        newdata["licenseNo"] = licenseNoUI.text_input(
            label="Driving License Number", placeholder="Enter Driving License No.",  max_chars=16, value= olddata["DL No."])
        newdata["dob"] = dobUI.date_input(label="Date of birth", min_value=datetime.date(
            1950, 1, 1), max_value=datetime.date.today(), value=olddata["DOB"])
        newdata["dob"] = str(newdata["dob"])
        usernameUI.text_input(
            label="Username", placeholder="Enter Username", value= olddata["Username"], disabled=True)
        newdata["phoneNo"] = phoneNoUI.text_input(
            label="Mobile No", placeholder="Enter Mobile No", value=olddata["Phone No."], max_chars=10)
        newdata["password"] = passwordUI.text_input(
            label="Password", type="password", value=olddata["Password"], disabled=True)
        newdata["confirmPassword"] = confirmPasswordUI.text_input(
            label="Confirm Password", type="password", value=olddata["Password"], disabled=True)
        newdata["email"] = st.text_input(
            label="Email", placeholder="Enter Email", value=olddata["Email"])
        newdata["state"] = stateUI.text_input(
            label="State", placeholder="Enter State", value=olddata["State"])
        newdata["city"] = cityUI.text_input(
            label="City", placeholder="Enter City", value=olddata["City"])
        newdata["street"] = streetUI.text_input(
            label="Street", placeholder="Enter Street", value=olddata["Street"])
        newdata["zipcode"] = zipcodeUI.text_input(
            label="Zipcode", max_chars=5, placeholder="Enter Zipcode", value=olddata["Zipcode"])

        if st.button("Update"):
            # st.write(newdata)
            UpdateCustomer(newdata)

def UpdateCustomer(customer):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update customer_info set dl_number = %s, firstname = %s,  lastname = %s, phone_no = %s, dob = %s, email = %s, state = %s, city = %s, street = %s, zipcode = %s where username = %s"
    )
    cursor.execute(query, (customer["licenseNo"], customer["firstname"], customer["lastname"], customer["phoneNo"], customer["dob"], customer["email"], customer["state"], customer["city"], customer["street"], customer["zipcode"], customer["username"],))
    db.commit()
    st.success("Updated Successfully", icon="✅")
    getAllCustomersUI()

# ---------------------------------------------------------------------------------------------------------------------
# Location details
# ---------------------------------------------------------------------------------------------------------------------

def UpdateLocationUI():
    # with st.expander("Before Update"):
    getAllLocationsUI()
    selected_location = st.selectbox("Select Location Name to Update", [location["Location Name"] for location in getAllLocations()])
    selected_location = getLocationByName(selected_location)[0]
    location_name = st.text_input("Location Name", placeholder="Enter Location Name", value= selected_location["Location Name"])
    stateUI, zipcodeUI, cityUI = st.columns([3, 1, 1])
    state = stateUI.text_input("State", placeholder="State", value=selected_location["State"])
    zipcode = zipcodeUI.text_input("Zipcode", placeholder="Zipcode", max_chars=5, value=selected_location["Zipcode"])
    city = cityUI.text_input("City", placeholder="City", value=selected_location["City"])
    street = st.text_input("Street", placeholder="Street", value=selected_location["Street"])

    location_data = {
        "location_id": selected_location["Location Id"],
        "location_name": location_name,
        "state": state,
        "zipcode": zipcode,
        "street": street,
        "city": city
    }

    if st.button("Update Location"):
        # st.write(location)
        UpdateLocation(location_data)
    
def UpdateLocation(location_data):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update locations set location_name = %s, state = %s, city = %s, street = %s, zipcode = %s where location_id = %s"
    )
    cursor.execute(query, (location_data["location_name"], location_data["state"], location_data["city"], location_data["street"], location_data["zipcode"], location_data["location_id"]))
    db.commit()
    st.success('Location Updated Successfully!', icon="✅")
    # with st.expander("After Update"):
    getAllLocationsUI()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bike Category
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def UpdateBikeCategoryUI():
    getAllBikeCategoriesUI()
    with st.container():
        selected_category = st.selectbox("Select Category Name to Update", [category["Name"] for category in getAllBikeCategories()])
        selected_category = getBikeCategoryByName(selected_category)[0]
        categoryNameUI, noOfPersonUI = st.columns([2,1])
        costPerDayUI, lateFeePerDayUI = st.columns(2)

        category_name = categoryNameUI.text_input("Category Name", placeholder="Category Name", value=selected_category["Name"], disabled=True)
        noOfPerson = noOfPersonUI.number_input("No Of Persons.", value=selected_category["NoPersons"])
        costPerDay = costPerDayUI.number_input("Cost Per Day", value=selected_category["CostPerDay"])
        lateFeePerDay = lateFeePerDayUI.number_input("Late Fee Per Day", value=selected_category["LateFee"])
        newcategory = {
            "category_name": category_name,
            "noOfPerson": noOfPerson,
            "costPerDay": costPerDay,
            "lateFeePerDay": lateFeePerDay
        }
        if st.button("Add Bike Category"):
            # st.write(category)
            UpdateBikeCategory(category= newcategory)

def UpdateBikeCategory(category):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update bike_category set no_persons = %s, cost_per_day = %s, late_fee_per_hour = %s where category_name = %s"
    )
    cursor.execute(query, (category["noOfPerson"], category["costPerDay"], category["lateFeePerDay"], category["category_name"],))
    db.commit()
    st.success('Bike Category Updated Successfully!', icon="✅")
    getAllBikeCategoriesUI()

# -----------------------------------------------------------------------------------------------------------------------------------------
# Bike details
# -----------------------------------------------------------------------------------------------------------------------------------------

def UpdateBikeUI():
    getAllBikesUI()
    with st.container():
        reg_no = st.selectbox("Select Reg No.", options=[bike["Registration No"] for bike in getAllBikes()])
        old_data = getBikeByRegNo(reg_no)[0]
        # st.write(old_data)
        registration_noUI, model_nameUI = st.columns(2)
        makeUI, model_yearUI = st.columns(2)
        mileageUI, availableUI = st.columns(2)
        categoryUI, bike_locationUI = st.columns(2)
        
        registration_no = registration_noUI.text_input("Bike Registration No.", max_chars= 6, placeholder="Bike Registration No.", disabled=True, value=old_data["Registration No"])
        model_name = model_nameUI.text_input("Model Name", placeholder="Model Name", value=old_data["Model Name"])
        make = makeUI.text_input("Make", placeholder="Make", value=old_data["Make"])
        mileage = mileageUI.number_input("Mileage", min_value= 2.0, value=old_data["Mileage"])
        model_year = model_yearUI.text_input("Model Year", value=old_data["Model Year"])
        available = availableUI.selectbox("Available", options=[True, False], index = [1, 0].index(old_data["Available"]))
        # category = categoryUI.selectbox("Bike Category", options=[category["Name"] for category in getAllBikeCategories()], index= getAllBikeCategories().index(old_data["Category"]))
        # location = bike_locationUI.selectbox("Bike Location", options=[location["Location Name"] for location in getAllLocations()])

        bike_details = {}
        bike_details["registration_no"] = old_data["Registration No"]
        bike_details["model_name"] = model_name
        bike_details["make"] = make
        bike_details["mileage"] = mileage
        bike_details["model_year"] = model_year
        bike_details["available"] = available
        


        if st.button("Update Bike"):
            # st.write(category)
            UpdateBike(bike_details= bike_details)

def UpdateBike(bike_details):
    # st.write(bike_details)
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update bike_details set model_name = %s, make = %s, model_year = %s, mileage = %s, available = %s where registration_no = %s"
            )
    # locationId = None
    # for location in getAllLocations():
    #     if location["Location Name"] == bike_details["location"]:
    #         locationId = location["Location Id"]
    cursor.execute(query, (bike_details["model_name"], bike_details["make"], bike_details["model_year"], bike_details["mileage"], bike_details["available"], bike_details["registration_no"],))
    db.commit()
    st.success('Bike Updated Successfully!', icon="✅")
    getAllBikesUI()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Discount
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def UpdateDiscountCouponUI():
    with st.container():
        getAllDiscountCouponsUI()
        selected_coupon = st.selectbox("Select Coupon Code", options=[coupon["coupon_code"] for coupon in getAllDiscountCoupons()])
        old_data = getDiscountCouponByCode(selected_coupon)[0]
        coupon_codeUI, coupon_nameUI = st.columns(2)
        discount_percentageUI, expiry_dateUI = st.columns(2)
        # st.write(old_data["expiry_date"])
        coupon_name = coupon_nameUI.text_input("Coupon Name", placeholder="Coupon Name", value = old_data["coupon_name"])
        coupon_codeUI.text_input("Coupon Code", placeholder="Coupon Code", value = old_data["coupon_code"], disabled= True)
        discount_percentage = discount_percentageUI.number_input("Discount %", value = old_data["discount_percentage"])
        expiry_date = expiry_dateUI.date_input("Expiry Date", value= old_data["expiry_date"])

        discount = {
            "coupon_name": coupon_name,
            "coupon_code": old_data['coupon_code'],
            "discount_percentage": discount_percentage,
            "expiry_date": str(expiry_date)
        }

        if st.button("Update Coupon"):
            UpdateDiscountCoupon(discount)

def UpdateDiscountCoupon(discount_data):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update discount set coupon_name = %s, discount_percentage = %s, expiry_date = %s where coupon_code = %s"
    )
    cursor.execute(query, (discount_data["coupon_name"], discount_data["discount_percentage"], discount_data["expiry_date"], discount_data["coupon_code"], ))
    db.commit()
    st.success('Discount Coupon Updated Successfully!', icon="✅")
    getAllDiscountCouponsUI()

# ------------------------------------------------------------------------------------------------------------------------------------
# Booking details
# ------------------------------------------------------------------------------------------------------------------------------------

def UpdateBookingDetailsUI():
    AllBookingDetailsUI()
    all_bookings = AllBookingDetails()
    selected_booking = st.selectbox("Select Booking Id to update", options=[booking["Booking Id"] for booking in all_bookings])
    
    oldData = getBookingDetailsById(selected_booking)[0]
    fromDateUI, toDateUI = st.columns(2)
    bookingDateUI, actualReturnDateUI = st.columns(2)
    couponUI, bikeRegNoUI = st.columns(2)

    fromDateUI.date_input(
                label="From",
                value=oldData["From"],
                disabled=True
            )

    toDateUI.date_input(
                label="To",
                value=oldData["To"],
                disabled=True
            )
    couponUI.text_input("Discount Coupons", value=oldData["Discount(%)"], disabled=True )     
    bikeRegNoUI.text_input("Bike RegNo.", value=oldData["Bike RegNo."], disabled=True )   

    bookingDateUI.date_input(
                label="Booked On",
                value=oldData["Booked On"],
                disabled=True
            )

    actualReturnDate = actualReturnDateUI.date_input(
                label="Actual Return Date",
                min_value= datetime.date.today()
            )
    damageCompensation = st.number_input("Damage Compensation", min_value=0.0)

    booking_data = {}
    booking_data["booking_id"] = oldData["Booking Id"]
    booking_data["actualReturnDate"] = str(actualReturnDate)
    booking_data["damageCompensation"] = damageCompensation


    if st.button("Update Booking"):
        # st.write(booking_data)
        UpdateBookingDetails(booking_data)

def UpdateBookingDetails(booking_data):
    cursor.execute(f"use {DB_NAME}")
    query = (
        "update booking_details set actual_return_date = %s where booking_id = %s"
    )
    cursor.execute(query, (booking_data["actualReturnDate"], booking_data["booking_id"]))
    db.commit()

    query = ("update billing_details set damage_compensation = %s where booking_id = %s")
    cursor.execute(query, (booking_data["damageCompensation"], booking_data["booking_id"]))
    db.commit()

    AllBookingDetailsUI()

    query = f'call get_total_amount({booking_data["booking_id"]}, @total_amount)'
    cursor.execute(query)
    cursor.execute("select @total_amount")
    total_amount = cursor.fetchone()
    st.info(f'Total Amount ₹{total_amount[0]}', icon="ℹ️")
    st.success('Booking Updated!', icon="✅")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Billing Details
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

