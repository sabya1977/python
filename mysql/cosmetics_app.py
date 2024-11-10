import mysql.connector
def connect_db():
    try:
        conn = mysql.connector.connect(user='sabya', password='oracle',
                                   host='127.0.0.1', database='cosmetics')
        print("Connected")
    except:
        print ("Error connecting to database")
    else:
        return conn
    
def close_db (cdb):
    cdb.close()

def return_main():
    choice=''
    choice = input("Press Enter to go back to main menu -> ")
    if not choice:
        return
    else:
        return
    
def show_menu ():
    print("Welcome to QUBA Beauty")
    print ("------------------------------------")
    print ("Here are your options!")
    print ("------------------------------------")
    print ("1. Explore our cosmetics collection")
    print ("2. Search a product by product/brand name")
    print ("3. Place an order for your product")
    print ("4. Cancel an existing order")
    print ("5. Get details of an existing order")
    print ("6. Quit Main menu")
    choice = int(input ("Enter your choice: "))
    if choice == 1:
        get_prod()
    elif choice == 2:
        get_prod_brn()
    elif choice == 3:
        place_order()
    elif choice == 4:
        cancel_order()
    elif choice == 6:
        return choice


def get_prod():
    cnx = connect_db()
    csr = cnx.cursor()
    qry = ("select * from products")
    csr.execute(qry)
    records = csr.fetchall()
    for rec in records:
        print(rec)
    close_db (cnx) 
    return_main()
   
def get_prod_brn():
    iprod = input("Enter Product name: ")
    ibrand = input("Enter Brand name: ")
    cnx = connect_db()
    csr = cnx.cursor()
    csr.execute("select * from products where prod_name = '{}' or brand_name = '{}'".format(iprod,ibrand))
    records = csr.fetchall()
    if csr.rowcount <=0:
        print ("Product/Brand not found!")
    else:
        for rec in records:
            print(rec)   
    close_db (cnx) 
    return_main()

def place_order():
    cnx = connect_db()
    iprod = ''
    ibrn=''
    iqty = 0
    imob = ''
    icname = ''
    ipin = ''
    print ("All input fields are mandatory!")
    print("----------------------------------")

    iprod = input("Enter Product name: ")
    ibrn= input("Enter Brand name: ")
    iqty = int(input("Enter quantity: "))
    imob = input("Enter your mobile no: ")
    icname = input("Enter your name: ")
    ipin = input("Enter your Pin Code: ")
    if (not iprod) or (not ibrn) or (not iqty) or (not imob) or (not icname) or (not ipin):
        print ("One of the mandatory fields is missing or invalid. Order cannot be placed")
        close_db (cnx) 
        return_main()
    else:
        csr = cnx.cursor()
        csr.execute("select prod_id from products where prod_name = '{}'".format(iprod))
        records = csr.fetchone()
        if csr.rowcount <=0:
            print ("Product Name you entered is not available in our store")
            close_db (cnx) 
            return_main()
        else:
            csr.execute("select prod_id from products where prod_name = '{}' and stock >= {}".format(iprod, iqty))
            records = csr.fetchone()
            if csr.rowcount <=0:
                print ("Product name you want to order is out of stock")
                close_db (cnx) 
                return_main()
            else:
                iprod_id = records[0]
                csr.execute ("select ifnull(max(order_id),0) from orders")
                maxord = csr.fetchone()
                iorder_id = int(maxord [0])
                iorder_id = iorder_id + 1
                csr.execute ("select unit_price from products where prod_name = '{}'".format(iprod))
                unit_price = csr.fetchone()
                print (unit_price [0])
                iunitp = unit_price [0]
                itotp = 0
                print(int(iqty) * iunitp)
                itotp = int(iqty) * iunitp
                csr.execute ("insert into orders (order_id, prod_id, tot_item, tot_price, cust_name, pin_code, mob_no) \
                        values({}, '{}', {}, {}, '{}', '{}', '{}')".format (iorder_id, iprod_id, iqty, itotp, icname, ipin, imob))
                
                csr.execute ("update products set stock = stock - {} where prod_id = '{}'".format(iqty,iprod_id))
                
                ch = input("Confirm order? (Y/N): ")
                if ch == 'Y' or ch == 'y':
                    cnx.commit()
                    print("Your order is placed. Order ID: ", iorder_id)
                else:
                    cnx.rollback()
                close_db (cnx) 
                return_main()

def cancel_order():
    ordrec = ()
    iord_id = 0
    ord_tot_item = 0
    cnx = connect_db()
    iord_id = int(input("Enter Order ID: "))
    csr = cnx.cursor()
    
    csr.execute ("select tot_item from orders where order_id = {}".format (iord_id))

    if csr.rowcount <=0:
        print ("You entered an invalid Order id, order cannot be cancelled")
        close_db(cnx)
        return_main()
    # else:

    # cnx.rollback()
    # return_main()

ch = 0
while ch != 6:
    ch = show_menu()