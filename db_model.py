# ROLES
super_admin:
    # - create DB
    - create tables
    - add admin
    - login
    - log_out
admin:
    - fill tables
    - change data
    - delete data
    - get data by filter
    - login
    - log_out

unregistered_user:
    - register
    - login
    - log_out
    - get data by filter

registered_user
    - buy product
    - discount card
    - login
    - log_out

# DB model
users 
    - id
    - first_name
    - last_name
    - address
    - phone
    - birth_date
    - role
    - password
    - email
    - discount

products --> MEBLI
    - id
    - unique_code
    - name
    - price
    - count
    - description
    - image
    - SUB_category_id

МЕБЛІ>СТОЛИ>КУХОННІ>...

SUB_categories
    - id
    - name
    - categori_id

catrgories
    - id
    - name