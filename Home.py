import streamlit as st

from Create import AddDriverUI, AddDriverContactUI, AddCustomerUI, AddLocationUI, AddBikeCategoryUI, AddBikeUI, AddDiscountCouponUI, AddBookingDetailsUI

from Read import getAllDriversUI, getDriverByDLUI, getDriverContactByDLUI, getAllDriverContactsUI, getAllCustomersUI, getCustomerByUsernameUI, getLocationByNameUI, getAllLocationsUI, getAllBikeCategoriesUI, getAllBikeCategoryByNameUI, getAllBikesUI, getAllBikeByModelNameUI, getAllDiscountCouponsUI, getDiscountCouponByCodeUI, AllBookingDetailsUI

from Delete import DeleteDriverUI, DeleteDriverContactUI, DeleteCustomerByUsernameUI, DeleteLocationByNameUI, DeleteDiscountCouponUI, DeleteBikeCategoryByNameUI, DeleteBikeRegNoUI, DeleteBookingDetailsUI

from Update import UpdateDriverUI, UpdateDriverContactUI, UpdateCustomerUI, UpdateLocationUI, UpdateBikeCategoryUI, UpdateBikeUI, UpdateDiscountCouponUI, UpdateBookingDetailsUI


st.set_page_config(page_title="My Bike Rental | Home", page_icon=":bike:")

with st.container():
    AVAILABLE_TABLES = ["Driver Info", "Driver Contacts", "Customer Info", "Locations", "Bike Category", "Bike Details", "Discount", "Booking Details"]
    AVAILABLE_OPERATIONS = ["CREATE", "READ", "UPDATE", "DELETE"]
    choseTable = st.sidebar.selectbox("Available Tables", options = AVAILABLE_TABLES)
    # st.sidebar.button("Execute Query")
    selected_operation = st.selectbox("Select Operation", options = AVAILABLE_OPERATIONS)
    if choseTable == AVAILABLE_TABLES[0]:
        # st.write(AVAILABLE_TABLES[0])
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDriverUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDriversUI()
                getDriverByDLUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDriverUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDriverUI()
            
    elif choseTable == AVAILABLE_TABLES[1]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDriverContactUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDriverContactsUI()
                getDriverContactByDLUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDriverContactUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDriverContactUI()

    elif choseTable == AVAILABLE_TABLES[2]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddCustomerUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllCustomersUI()
                getCustomerByUsernameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateCustomerUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteCustomerByUsernameUI()
    elif choseTable == AVAILABLE_TABLES[3]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddLocationUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllLocationsUI()
                getLocationByNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateLocationUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteLocationByNameUI()
    elif choseTable == AVAILABLE_TABLES[4]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddBikeCategoryUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllBikeCategoriesUI()
                getAllBikeCategoryByNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateBikeCategoryUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteBikeCategoryByNameUI()
    elif choseTable == AVAILABLE_TABLES[5]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddBikeUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllBikesUI()
                getAllBikeByModelNameUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateBikeUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteBikeRegNoUI()
    elif choseTable == AVAILABLE_TABLES[6]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddDiscountCouponUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                getAllDiscountCouponsUI()
                getDiscountCouponByCodeUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateDiscountCouponUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteDiscountCouponUI()
    elif choseTable == AVAILABLE_TABLES[7]:
        with st.container():
            if selected_operation == AVAILABLE_OPERATIONS[0]:
                AddBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[1]:
                AllBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[2]:
                UpdateBookingDetailsUI()
            elif selected_operation == AVAILABLE_OPERATIONS[3]:
                DeleteBookingDetailsUI()


