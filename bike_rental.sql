-- Driver's information
create table driver_info(
    dl_number char(16) not null,
    constraint pk_driver_dl primary key(dl_number),
    driver_name varchar(35) not null,
    driver_dob date not null,
    driving_experience int not null,
    available boolean default true
);
alter table driver_info
add constraint check_experience check(driving_experience >= 2);

-- Drivers Contact numbers
create table driver_contacts(
    dl_number char(16) not null,
    constraint fk_driver_dl foreign key(dl_number) references driver_info(dl_number),
    phone_no char(10)
);
alter table driver_contacts 
modify phone_no char(10) not null;
alter table driver_contacts 
add constraint check_phone check(char_length(phone_no) = 10);

-- Customer's information
create table customer_info(
    customer_id int not null auto_increment,
    dl_number char(16) unique,
    firstname varchar(35) not null,
    lastname varchar(35) not null,
    phone_no char(10) not null,
    username varchar(35) not null unique,
    password varchar(50) not null,
    dob date not null,
    email varchar(35),
    state varchar(35) not null,
    city varchar(35) not null,
    street varchar(35) not null,
    zipcode char(5) not null,
    constraint pk_customer_id primary key(customer_id),
    constraint check_phone_customer check(char_length(phone_no) = 10)
);
alter table customer_info auto_increment = 20000;

-- Customers Contact numbers
/* create table customers_contacts(
    customer_id int not null,
    phone_no char(10) not null,
    constraint fk_customer_id foreign key(customer_id) references customer_info(customer_id),
    constraint check_phone_customer check(char_length(phone_no) = 10)
); */

-- Location Details
create table locations(
    location_id int not null auto_increment,
    location_name varchar(50) not null,
    state varchar(35) not null,
    city varchar(35) not null,
    street varchar(35) not null,
    zipcode int(5) not null,
    constraint pk_location_id primary key(location_id)
);
alter table locations auto_increment = 40000;
alter table locations 
modify location_name varchar(50) not null unique;

-- Bike Category
create table bike_category(
    category_name varchar(35) not null,
    no_persons int not null,
    cost_per_day double not null,
    late_fee_per_hour double not null,
    constraint pk_category_name primary key(category_name)
);

-- Bike details
create table bike_details(
    registration_no char(6) not null,
    model_name varchar(35) not null,
    make varchar(35) not null,
    model_year int(4) not null,
    mileage double not null,
    available boolean default true,
    category varchar(35) not null,
    bike_location int not null,
    constraint pk_bike_reg primary key(registration_no),
    constraint fk_bike_category foreign key(category) references bike_category(category_name),
    constraint fk_bike_location foreign key(bike_location) references locations(location_id)
);

-- Discount
create table discount(
    coupon_code char(4) not null,
    coupon_name varchar(35) not null,
    discount_percentage double not null,
    expiry_date date not null,
    constraint pk_discount_coupon primary key(coupon_code)
);

-- Booking
        
create table booking_details(
    booking_id int not null auto_increment,
    from_date date not null,
    return_date date not null,
    basic_fare double not null, -- no. of days * price per day of bike - discount amt
    discount_percentage double default 0, -- from discount percentage
    booking_status boolean default false,
    with_driver boolean default false,
    actual_return_date date not null,
    pickup_location int not null,
    drop_location int not null,
    coupon_code char(4),
    bike_reg_no char(6) not null,
    customer_id int not null,
    booking_date date default current_date(), 
    constraint pk_booking_id primary key(booking_id),
    constraint fk_booking_coupon foreign key(coupon_code) references discount(coupon_code),
    constraint fk_booking_bike foreign key(bike_reg_no) references bike_details(registration_no),
    constraint fk_booking_pickup foreign key(pickup_location) references locations(location_id),
    constraint fk_booking_pickdrop foreign key(drop_location) references locations(location_id),
    constraint fk_booking_customer foreign key(customer_id) references customer_info(customer_id)
);
alter table booking_details auto_increment=50000;

-- Billing
create table billing_details(
    bill_id int not null auto_increment,
    booking_id int not null,
    tax_amount double default 20.0,
    damage_compensation double default 0,
    late_fee double default 0, -- if actual return date > return date
    bill_date date default current_date(),
    constraint pk_bill_id primary key(bill_id),
    constraint fk_bill_booking foreign key(booking_id) references booking_details(booking_id)
);
alter table billing_details auto_increment = 60000;

/* -- Payment details
create table payment_details(
    bill_id int not null,
    bill_date date not null,
    amount double default 0,
    constraint fk_payment_bill foreign key(bill_id) references(bill_id) not null
); */



create table booking_with_driver(
    id int not null auto_increment,
    driver_dl char(16) not null,
    customer_id int not null,
    booking_id int not null,
    booking_date date default current_date(),
    constraint pk_driver_customer_id primary key(id),
    constraint fk_booking_driver_customer foreign key(driver_dl) references driver_info(dl_number),
    constraint fk_booking_customer_driver foreign key(customer_id) references customer_info(customer_id),
    constraint fk_booking_id foreign key(booking_id) references booking_details(booking_id)
);

alter table booking_with_driver auto_increment = 70000;

/* -- drop this table
-- done
create table experience_charge(
    experience int not null,
    amount double default 200.0,
    constraint pk_experience primary key(experience)
); */

