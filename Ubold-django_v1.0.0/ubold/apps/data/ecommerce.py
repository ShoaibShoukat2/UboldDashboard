user1 = "/static/images/users/user-1.jpg"
user2 = "/static/images/users/user-2.jpg"
user3 = "/static/images/users/user-3.jpg"
user4 = "/static/images/users/user-4.jpg"
user5 = "/static/images/users/user-5.jpg"
user6 = "/static/images/users/user-6.jpg"
user7 = "/static/images/users/user-7.jpg"
user8 = "/static/images/users/user-8.jpg"
user9 = "/static/images/users/user-8.jpg"
user10 = "/static/images/users/user-10.jpg"

visaCard = "/static/images/cards/visa.png"
masterCard = "/static/images/cards/master.png"
amazonCard = "/static/images/cards/amazon.png"
americanExpressCard = "/static/images/cards/american-express.png"
discoverCard = "/static/images/cards/discover.png"

product1 = "/static/images/products/product-1.png"
product2 = "/static/images/products/product-2.png"
product3 = "/static/images/products/product-3.png"
product4 = "/static/images/products/product-4.png"
product5 = "/static/images/products/product-5.png"
product6 = "/static/images/products/product-6.png"
product7 = "/static/images/products/product-7.png"
product8 = "/static/images/products/product-8.png"
product9 = "/static/images/products/product-9.jpg"
product10 = "/static/images/products/product-10.jpg"
product11 = "/static/images/products/product-11.jpg"
product12 = "/static/images/products/product-12.jpg"


ecommerceStatisticsDict = [
    {
        "icon": "dripicons-wallet",
        "color": "primary",
        "amount": 58947,
        "symbolbefore": "$",
        "name": "Total Revenue",
    },
    {
        "icon": "dripicons-basket",
        "color": "success",
        "amount": 1845,
        "name": "Orders",
    },
    {
        "icon": "dripicons-store",
        "color": "info",
        "amount": 825,
        "name": "Stores",
    },
    {
        "icon": "dripicons-user-group",
        "color": "warning",
        "amount": 2430,
        "name": "Sellers",
    },
]

transactionHistoryDict = [
    {
        "person": {"name": "Imelda J. Stanberry", "avatar": user2},
        "card": {"img": visaCard, "number": "**** 3256"},
        "date": "27.03.2018",
        "amount": "$345.98",
        "status": {
            "name": "Failed",
            "color": "danger",
        },
    },
    {
        "person": {"name": "Francisca S. Lobb", "avatar": user3},
        "card": {"img": masterCard, "number": "**** 8451"},
        "date": "28.03.2018",
        "amount": "$1,250",
        "status": {
            "name": "Paid",
            "color": "success",
        },
    },
    {
        "person": {"name": "James A. Wert", "avatar": user1},
        "card": {"img": amazonCard, "number": "**** 2258"},
        "date": "28.03.2018",
        "amount": "$145",
        "status": {
            "name": "Paid",
            "color": "success",
        },
    },
    {
        "person": {"name": "Dolores J. Pooley", "avatar": user4},
        "card": {"img": americanExpressCard, "number": "**** 6950"},
        "date": "29.03.2018",
        "amount": "$2,005.89",
        "status": {
            "name": "Failed",
            "color": "danger",
        },
    },
    {
        "person": {"name": "Karen I. McCluskey", "avatar": user5},
        "card": {"img": discoverCard, "number": "**** 0021"},
        "date": "31.03.2018",
        "amount": "$24.95",
        "status": {
            "name": "Paid",
            "color": "success",
        },
    },
]

recentProductsDict = [
    {
        "product": {"name": "Adirondack Chair", "img": product1},
        "category": "Dining Chairs",
        "addedDate": "27.03.2018",
        "amount": "$345.98",
        "status": {
            "name": "Active",
            "color": "success",
        },
    },
    {
        "product": {"name": "Biblio Plastic Armchair", "img": product2},
        "category": "Baby Chairs",
        "addedDate": "28 .03.2018",
        "amount": "$1,250",
        "status": {
            "name": "Active",
            "color": "success",
        },
    },
    {
        "product": {"name": "Amazing Modern Chair", "img": product3},
        "category": "Plastic Armchair",
        "addedDate": "28.03.2018",
        "amount": "$145",
        "status": {
            "name": "Deactive",
            "color": "danger",
        },
    },
    {
        "product": {"name": "Designer Awesome Chair", "img": product4},
        "category": "Wing Chairs",
        "addedDate": "29.03.2018",
        "amount": "$2,005.89",
        "status": {
            "name": "Active",
            "color": "success",
        },
    },
    {
        "product": {"name": "The butterfly chair", "img": product5},
        "category": "Dining Chairs",
        "addedDate": "31.03.2018",
        "amount": "$24.95",
        "status": {
            "name": "Active",
            "color": "success",
        },
    },
]

productsDict = [
    {
        "id": 1,
        "img": product1,
        "name": "Adirondack Chair",
        "stocks": 98,
        "price": "$39",
    },
    {
        "id": 2,
        "img": product2,
        "name": "Biblio Plastic Armchair",
        "stocks": "23",
        "price": "$98",
    },
    {
        "id": 3,
        "img": product3,
        "name": "Amazing Modern Chair",
        "stocks": "235",
        "price": "$49",
    },

    {
        "id": 4,
        "img": product4,
        "name": "Designer Awesome Chair",
        "stocks": "385",
        "price": "$29",
    },

    {
        "id": 5,
        "img": product5,
        "name": "The butterfly chair",
        "stocks": "25",
        "price": "$49",
    },
    {
        "id": 6,
        "img": product6,
        "name": "Dining Chairs",
        "stocks": "39",
        "price": "$19",
    },

    {
        "id": 7,
        "img": product7,
        "name": "Plastic Armchair",
        "stocks": "36",
        "price": "$99",
    },

    {
        "id": 8,
        "img": product8,
        "name": "Wing Chairs",
        "stocks": "128",
        "price": "$29",
    },
]

outletDict = [
    {
        "name": "ASOS Ridley Outlet - NYC",
        "price": "$139.58",
        "stock": "27",
        "colour": "danger",
        "revenue": "$1,89,547",
    },
    {
        "name": "Marco Outlet - SRT",
        "price": "$149.99",
        "stock": "71",
        "colour": "success",
        "revenue": "$87,245",
    },
    {
        "name": "Chairtest Outlet - HY",
        "price": "$135.87",
        "stock": "82",
        "colour": "success",
        "revenue": "$5,87,478",
    },
    {
        "name": "Nworld Group - India",
        "price": "$159.89",
        "stock": "42",
        "colour": "warning",
        "revenue": "$55,781",
    },
]


productDetailDict = {
    "images": {
        "img1": product9,
        "img2": product10,
        "img3": product11,
        "img4": product12,
    },
    "detail": {
        "brand": "Jack & Jones",
        "name": "Jack & Jones Men's T-shirt (Blue)",
        "rating": 4,
        "numberOfReviews": 36,
        "offer": "20 %",
        "price": "$80",
        "discountedPrice": "$64",
        "instock": True,
        "description":
        " The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators.",
    },
}


customerStatus = {
    "active": {"name": "Active", "color": "success"},
    "blocked": {"name": "Blocked", "color": "danger"},
}

customersDict = [
    {
        "id": 1,
        "customer": {
            "name": "Rory Seekamp",
            "avatar": user2,
        },

        "phone": "078 5054 8877",
        "balance": "$3365.12",
        "orders": "25",

        "lastOrder": {
            "date": "April 21 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["blocked"],
    },
    {
        "id": 2,
        "customer": {
            "name": "Bryan J. Luellen",
            "avatar": user3,
        },

        "phone": "215-302-3376",
        "balance": "$874.25",
        "orders": "220",

        "lastOrder": {
            "date": "August 04 2019",
            "time": "08:18 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 3,
        "customer": {
            "name": "Paul J. Friend",
            "avatar": user4,
        },

        "phone": "050 414 8778",
        "balance": "$12,874.82",
        "orders": "43",

        "lastOrder": {
            "date": "August 05 2019 ",
            "time": "10:29 PM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 4,
        "customer": {
            "name": "Timothy Kauper",
            "avatar": user1,
        },

        "phone": "(216) 75 612 706",
        "balance": "$561.25",
        "orders": "62",

        "lastOrder": {
            "date": "February 01 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 5,
        "customer": {
            "name": "Zara Raws",
            "avatar": user5,
        },

        "phone": "(02) 75 150 655",
        "balance": "$2147.84",
        "orders": "09",

        "lastOrder": {
            "date": "February 01 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 6,
        "customer": {
            "name": " Edward Roseby",
            "avatar": user8,
        },

        "phone": "078 6013 3854",
        "balance": "$71584.2",
        "orders": "365",

        "lastOrder": {
            "date": "February 09 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 7,
        "customer": {
            "name": "Kathryn S. Collier",
            "avatar": user3,
        },

        "phone": "828-216-2190",
        "balance": "$125.78",
        "orders": "841",

        "lastOrder": {
            "date": "November 04 2019",
            "time": "10:29 PM",
        },

        "status": customerStatus["blocked"],
    },
    {
        "id": 8,
        "customer": {
            "name": "Jenny C. Gero",
            "avatar": user7,
        },

        "phone": "078 7173 9261",
        "balance": "$965.20",
        "orders": "	214",

        "lastOrder": {
            "date": "November 14 201",
            "time": "07:22 AM",
        },

        "status": customerStatus["blocked"],
    },
    {
        "id": 9,
        "customer": {
            "name": "Dean Smithies",
            "avatar": user10,
        },

        "phone": "077 6157 4248",
        "balance": "$482.15",
        "orders": "68",

        "lastOrder": {
            "date": "October 09 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 10,
        "customer": {
            "name": "Labeeb Ghali",
            "avatar": user1,
        },

        "phone": "050 414 8778",
        "balance": "$7852.3",
        "orders": "475",

        "lastOrder": {
            "date": "October 27 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 11,
        "customer": {
            "name": "Annette P. Kelsch",
            "avatar": user6,
        },

        "phone": "(+15) 73 483 758",
        "balance": "$451.28",
        "orders": "25",

        "lastOrder": {
            "date": "September 07 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
    {
        "id": 12,
        "customer": {
            "name": " Anna Ciantar",
            "avatar": user9,
        },

        "phone": "(216) 76 298 896",
        "balance": "$5482.00",
        "orders": "921",

        "lastOrder": {
            "date": "September 12 2019",
            "time": "07:22 AM",
        },

        "status": customerStatus["active"],
    },
]


paymentStatuses = {
    "paid": {"name": "Paid", "color": "success", "icon": "mdi-currency-usd-circle"},
    "awaitingAuthorization": {
        "name": "Awaiting Authorization",
        "color": "warning",
        "icon": "mdi-timer-sand",
    },
    "paymentFailed": {
        "name": "Payment Failed",
        "color": "danger",
        "icon": "mdi-cancel",
    },
    "cashonDelivery": {
        "name": "Cash on Delivery",
        "color": "info",
        "icon": "mdi-cash",
    },
}

orderStatus = {
    "shipped": {"name": "Shipped", "color": "info"},
    "processing": {"name": "Processing", "color": "warning"},
    "delivered": {"name": "Delivered", "color": "success"},
    "cancelled": {"name": "Cancelled", "color": "danger"},
}


ordersDict = [
    {
        "id": 1,
        "orderID": "#UB9708",
        "products": [
            {
                "id": 1,
                "img": product1,
            },
            {
                "id": 2,
                "img": product2,
            },
        ],
        "date": "August 05 2018",
        "time": "10:29 PM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "$176.41",
        "paymentMethod": "Mastercard",
        "orderStatus": orderStatus["shipped"],
    },
    {
        "id": 2,
        "orderID": "#UB9707",
        "products": [
            {
                "id": 3,
                "img": product3,
            },
            {
                "id": 4,
                "img": product4,
            },
            {
                "id": 5,
                "img": product5,
            },
        ],
        "date": "August 04 2018",
        "time": "08:18 AM",
        "paymentStatus": paymentStatuses["awaitingAuthorization"],
        "total": "$1,458.65",
        "paymentMethod": "Visa",
        "orderStatus": orderStatus["processing"],
    },
    {
        "id": 3,
        "orderID": "#UB9706",
        "products": [
            {
                "id": 7,
                "img": product7,
            },
        ],
        "date": "August 04 2018",
        "time": "10:29 PM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "$801.99",
        "paymentMethod": "Credit Card",
        "orderStatus": orderStatus["processing"],
    },
    {
        "id": 4,
        "orderID": "#UB9705",
        "products": [
            {
                "id": 3,
                "img": product3,
            },
            {
                "id": 8,
                "img": product8,
            },
        ],
        "date": "August 03 2018",
        "time": "07:56 AM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "$2,514.36",
        "paymentMethod": "Paypal",
        "orderStatus": orderStatus["delivered"],
    },
    {
        "id": 5,
        "orderID": "#UB9704",
        "products": [
            {
                "id": 5,
                "img": product5,
            },
            {
                "id": 7,
                "img": product7,
            },
        ],
        "date": "May 22 2018",
        "time": "07:22 PM",
        "paymentStatus": paymentStatuses["paymentFailed"],
        "total": "$2,514.36",
        "paymentMethod": "Paypal",
        "orderStatus": orderStatus["cancelled"],
    },
    {
        "id": 6,
        "orderID": "#UB9703",
        "products": [
            {
                "id": 2,
                "img": product2,
            },
        ],
        "date": "April 02 2018",
        "time": "03:02 AM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "$183.20",
        "paymentMethod": "Payoneer",
        "orderStatus": orderStatus["shipped"],
    },
    {
        "id": 7,
        "orderID": "#UB9702",
        "products": [
            {
                "id": 4,
                "img": product4,
            },
            {
                "id": 6,
                "img": product6,
            },
        ],
        "date": "March 18 2018",
        "time": "11:19 PM",
        "paymentStatus": paymentStatuses["awaitingAuthorization"],
        "total": "$1,768.41",
        "paymentMethod": "Visa",
        "orderStatus": orderStatus["processing"],
    },
    {
        "id": 8,
        "orderID": "#UB9701",
        "products": [
            {
                "id": 6,
                "img": product6,
            },
            {
                "id": 8,
                "img": product8,
            },
            {
                "id": 3,
                "img": product3,
            },
        ],
        "date": "February 01 2018",
        "time": "07:22 AM",
        "paymentStatus": paymentStatuses["cashonDelivery"],
        "total": "$3,582.99",
        "paymentMethod": "Paypal",
        "orderStatus": orderStatus["shipped"],
    },
    {
        "id": 9,
        "orderID": "#UB9700",
        "products": [
            {
                "id": 2,
                "img": product2,
            },
            {
                "id": 5,
                "img": product5,
            },
        ],
        "date": "January 22 2018",
        "time": "08:09 PM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "923.95",
        "paymentMethod": "Credit Card",
        "orderStatus": orderStatus["delivered"],
    },
    {
        "id": 10,
        "orderID": "#UB9699",
        "products": [
            {
                "id": 7,
                "img": product7,
            },
            {
                "id": 8,
                "img": product8,
            },
        ],
        "date": "January 17 2018",
        "time": "02:30 PM",
        "paymentStatus": paymentStatuses["paid"],
        "total": "$5,177.68",
        "paymentMethod": "Mastercard",
        "orderStatus": orderStatus["shipped"],
    },
]


orderDict = {
    "orderID": "#VL2537",
    "trackOrderData": {
        "trackingID": "894152012012",
        "trackerData": [
            {
                "name": "Order Placed",
                "time": "07:22 AM",
                "date": "April 21 2019",
                "status": "completed",
            },
            {
                "name": "Packed",
                "time": "12:16 AM",
                "date": "April 22 2019",
                "status": "completed",
            },
            {
                "name": "Shipped",
                "time": "April 22 2019 05:16 PM",
                "date": "April 22 2019",
                "status": "active",
            },
            {
                "name": "Delivered",
                "estimatedtime": "delivery within 3 days",
                "status": "incomplete",
            },
        ],
    },
    "billData": {
        "prodects": [
            {
                "name": "Polo Navy blue T-shirt",
                "img": product1,
                "quantity": 1,
                "price": "$39",
                "total": "$39",
            },
            {
                "name": "Red Hoodie for men",
                "img": product5,
                "quantity": 2,
                "price": "$46",
                "total": "$92",
            },
            {
                "name": "Red Hoodie for men",
                "img": product3,
                "quantity": 1,
                "price": "$46",
                "total": "$46",
            },
        ],
        "subTotal": "$177",
        "shippingCharge": "$24",
        "estimatedTax": "$12",
        "total": "$213",
    },
    "shippingInformation": {
        "name": "Brent Jones",
        "address": "3559 Roosevelt Wilson Lane San Bernardino, CA 92405",
        "phone": "(123) 456-7890",
        "mobile": "(+01) 12345 67890",
    },
    "billingInformation": {
        "paymentType": "Credit Card",
        "provider": "Visa ending in 2851",
        "validDate": "02/2020",
        "CVV": "xxx",
    },
    "deliveryInfo": {
        "orderID": "xxxx235",
        "paymentMode": "COD",
    },
}

sellersDict = [
    {
        "id": 1,
        "owner": {
            "name": "Paul J. Friend",
            "avatar": user2,
        },
        "storeName": "Homovee",
        "ratings": "4.9",
        "products": "128",
        "walletBalance": "$128,250",
        "createDate": "07/07/2018",
        "revenue": "$258.26k",
    },
    {
        "id": 2,
        "owner": {
            "name": "Bryan J. Luellen",
            "avatar": user3,
        },
        "storeName": "Execucy",
        "ratings": "3.5",
        "products": "09",
        "walletBalance": "$78,410",
        "createDate": "09/12/2018",
        "revenue": "$152.3k",
    },
    {
        "id": 3,
        "owner": {
            "name": "Kathryn S. Collier",
            "avatar": user4,
        },
        "storeName": "Epiloo",
        "ratings": "4.1",
        "products": "78",
        "walletBalance": "$89,458",
        "createDate": "06/30/2018",
        "revenue": "$178.6k",
    },
    {
        "id": 4,
        "owner": {
            "name": "Timothy Kauper",
            "avatar": user1,
        },
        "storeName": "Uberer",
        "ratings": "4.9",
        "products": "847",
        "walletBalance": "$258,125",
        "createDate": "09/08/2018",
        "revenue": "$368.2k",
    },
    {
        "id": 5,
        "owner": {
            "name": "Zara Raws",
            "avatar": user5,
        },
        "storeName": "Symic",
        "ratings": "5.0",
        "products": "235",
        "walletBalance": "$56,210",
        "createDate": "07/15/2018",
        "revenue": "$89.5k",
    },
    {
        "id": 6,
        "owner": {
            "name": "Annette P. Kelsch",
            "avatar": user6,
        },
        "storeName": "Insulore",
        "ratings": "4.0",
        "products": "485",
        "walletBalance": "$330,251",
        "createDate": "09/05/2018",
        "revenue": "$597.8k",
    },
    {
        "id": 7,
        "owner": {
            "name": "Jenny C. Gero",
            "avatar": user7,
        },
        "storeName": "Susadmin",
        "ratings": "4.3",
        "products": "38",
        "walletBalance": "$12,000",
        "createDate": "08/02/2018",
        "revenue": "$29.3k",
    },
    {
        "id": 8,
        "owner": {
            "name": "Edward Roseby",
            "avatar": user8,
        },
        "storeName": "Hyperill",
        "ratings": "5.0",
        "products": "77",
        "walletBalance": "$45,216",
        "createDate": "08/23/2018",
        "revenue": "$48.6k",
    },
    {
        "id": 9,
        "owner": {
            "name": "Anna Ciantar",
            "avatar": user9,
        },
        "storeName": "Vicedel",
        "ratings": "2.7",
        "products": "347",
        "walletBalance": "$7,815",
        "createDate": "05/06/2018",
        "revenue": "$12.1k",
    },
    {
        "id": 10,
        "owner": {
            "name": "Dean Smithies",
            "avatar": user10,
        },
        "storeName": "Circumous",
        "ratings": "4.9",
        "products": "506",
        "walletBalance": "$68,143",
        "createDate": "04/09/2018",
        "revenue": "$78.2k",
    },
]


cartProductsDict = [
    {
        "id": 1,
        "img": product1,
        "name": "Polo Navy blue T-shirt",
        "size": "Large",
        "color": "Light Green",
        "price": 148.66,
        "quantity": 5,
        "total": "$743.30",
    },
    {
        "id": 2,
        "img": product2,
        "name": "Brown Hoodie for men",
        "size": "Small",
        "color": "Brown",
        "price": 99.0,
        "quantity": 2,
        "total": "$198.00",
    },
    {
        "id": 3,
        "img": product3,
        "name": "Designer Awesome T-Shirt",
        "size": "Medium",
        "color": "Light Pink",
        "price": 49.99,
        "quantity": 10,
        "total": "$499.90",
    },
    {
        "id": 4,
        "img": product4,
        "name": "Half Sleeves Tshirt",
        "size": "Large",
        "color": "Green",
        "price": 129.99,
        "quantity": 1,
        "total": "$129.99",
    },
]
cartSummaryDict = {
    "grandTotal": 1571.19,
    "discount": 157.11,
    "shippingCharge": 25,
    "estimatedTax": 19.22,
    "total": 1458.3,
}
cartDiscountCode = "UBTF25"
cartDiscountRate = 25


checkoutHomeAddress = {
    "name": "Brent Rowe",
    "address": "3559 Roosevelt Wilson Lane San Bernardino, CA 92405",
    "phone": "(123) 456-7890",
    "mobile": "(+01) 12345 67890",
}

checkoutOfficeAddress = {
    "name": "Brent Rowe",
    "address": "3559 Roosevelt Wilson Lane San Bernardino, CA 92405",
    "phone": "(123) 456-7890",
    "mobile": "(+01) 12345 67890",
}

checkoutStandardDeliveryDict = {
    "price": 0,
    "estimatedDays": "5-7",
}
checkoutFastDeliveryDict = {
    "price": 25,
    "estimatedDays": "1-2",
}

checkoutOrderDict = {
    "id": "UB9708",
    "products": [
        {"name": "Polo Navy blue T-shirt", "image": product1, "quantity": 1, "price": 39},
        {"name": "Red Hoodie for men", "image": product2, "quantity": 2, "price": 46},
        {
            "name": "Designer Awesome T-Shirt",
            "image": product3,
            "quantity": 1,
            "price": 26,
        },
    ],
    "shipping": 0,
}
