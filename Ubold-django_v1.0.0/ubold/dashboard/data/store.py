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

statisticsDashboard1Dict = [
    {
        "icon": "fe-heart",
        "color": "primary",
        "amount": 58947,
        "symbolbefore": "$",
        "name": "Total Revenue",
    },
    {
        "icon": "fe-shopping-cart",
        "color": "success",
        "amount": 127,
        "name": "Today's Sales",
    },
    {
        "icon": "fe-bar-chart-line",
        "color": "info",
        "amount": 0.58,
        "symbolafter": "%",
        "name": "Conversion",
    },
    {
        "icon": "fe-eye",
        "color": "warning",
        "amount": 78.41,
        "symbolafter": "k",
        "name": "Today's Visits",
    }
]

statisticsDashboard2Dict = [
  {
    "icon": "fe-aperture",
    "color": "blue",
    "amount": 12145,
    "symbolbefore": "$",
    "name": "Income status",
    "target": 60,
  },
    {
    "icon": "fe-shopping-cart",
    "color": "success",
    "amount": 1576,
    "name": "January's Sales",
    "target": 49,
  },
    {
    "icon": "fe-bar-chart-2",
    "color": "warning",
    "amount": 8947,
    "symbolbefore": "$",
    "name": "Payouts",
    "target": 18,
  },
    {
    "icon": "fe-cpu",
    "color": "info",
    "amount": 178,
    "name": "Available Stores",
    "target": 74,
  }
]

topUsersBalancesDict = [
    {
        "avatar": user2,
        "name": "Tomaslau",
        "text": "Member Since 2017",
        "currencyIcon": "mdi-currency-btc",
        "currency_name": "BTC",
        "balance": 0.00816117,
        "reservedInOrders": 0.00097036,
    },
    {
        "avatar": user3,
        "name": "Erwin E. Brown",
        "text": "Member Since 2017",
        "currencyIcon": "mdi-currency-eth",
        "currency_name": "ETH",
        "balance": 3.16117008,
        "reservedInOrders": 1.70360009,
    },
    {
        "avatar": user4,
        "name": "Margeret V. Ligon",
        "text": "Member Since 2017",
        "currencyIcon": "mdi-currency-eur",
        "currency_name": "EUR",
        "balance": 25.08,
        "reservedInOrders": 12.58,
    },
    {
        "avatar": user5,
        "name": "Jose D. Delacruz",
        "text": "Member Since 2017",
        "currencyIcon": "mdi-currency-cny",
        "currency_name": "CNY",
        "balance": 82.0,
        "reservedInOrders": 30.83,
    },
    {
        "avatar": user6,
        "name": "Luke J. Sain",
        "text": "Member Since 2017",
        "currencyIcon": "mdi-currency-btc",
        "currency_name": "BTC",
        "balance": 2.00816117,
        "reservedInOrders": 1.00097036,
    },
]

revenueStatus = {
    "upcoming": {"name": "Upcoming", "color": "warning"},
    "paid": {"name": "Paid", "color": "success"},
    "overdue": {"name": "Overdue", "color": "danger"},
}

projectionsVsActualsStatDist = {
    "target": "3.8k",
    "last_week": "1.1k",
    "last_month": "25k",
}


revenueStatDist = {
    "target": "7.8k",
    "last_week": "1.4k",
    "last_month": "15k",
}

revenueHistoryDict = [
    {
        "Marketplaces": "Themes Market",
        "Date": "Oct 15, 2018	",
        "Payouts": 5848.68,
        "symbolbefore": "$",
        "status": revenueStatus["upcoming"],
        "action": "/#",
    },
    {
        "Marketplaces": "Freelance",
        "Date": "Oct 12, 2018		",
        "Payouts": 1247.25,
        "symbolbefore": "$",
        "status": revenueStatus["paid"],
        "action": "/#",
    },
    {
        "Marketplaces": "Share Holding",
        "Date": "Oct 10, 2018	",
        "Payouts": 815.89,
        "symbolbefore": "$",
        "status": revenueStatus["paid"],
        "action": "/#",
    },
    {
        "Marketplaces": "Envato's Affiliates",
        "Date": "Oct 03, 2018	",
        "Payouts": 248.75,
        "symbolbefore": "$",
        "status": revenueStatus["overdue"],
        "action": "/#",
    },
    {
        "Marketplaces": "Marketing Revenue",
        "Date": "Sep 21, 2018	",
        "Payouts": 978.21,
        "symbolbefore": "$",
        "status": revenueStatus["upcoming"],
        "action": "/#",
    },
    {
        "Marketplaces": "Advertise Revenue",
        "Date": "Sep 15, 2018	",
        "Payouts": 358.1,
        "symbolbefore": "$",
        "status": revenueStatus["paid"],
        "action": "/#",
    },
]


topSellingProductsDict = [
    {
        "productName": "ASOS Ridley High Waist",
        "price": 79.49,
        "quantity": 82,
        "amount": 6518.18,
        "symbolbefore": "$",
    },
    {
        "productName": "Marco Lightweight Shirt",
        "price": 128.5,
        "quantity": 37,
        "amount": 4754.5,
        "symbolbefore": "$",
    },
    {
        "productName": "Half Sleeve Shirt",
        "price": 39.99,
        "quantity": 64,
        "amount": 2559.36,
        "symbolbefore": "$",
    },
    {
        "productName": "Lightweight Jacket",
        "price": 20.0,
        "quantity": 184,
        "amount": 3680.0,
        "symbolbefore": "$",
    },
    {
        "productName": "Marco Shoes",
        "price": 28.49,
        "quantity": 69,
        "amount": 1965.81,
        "symbolbefore": "$",
    },
    {
        "productName": "ASOS Ridley High Waist",
        "price": 79.49,
        "quantity": 82,
        "amount": 6518.18,
        "symbolbefore": "$",
    },
    {
        "productName": "Half Sleeve Shirt",
        "price": 39.99,
        "quantity": 64,
        "amount": 2559.36,
        "symbolbefore": "$",
    },
    {
        "productName": "Lightweight Jacket",
        "price": 20.0,
        "quantity": 184,
        "amount": 3680.0,
        "symbolbefore": "$",
    },
]

inboxDict = [
    {
        "avatar": user2,
        "name": "Tomaslau",
        "text": "I've finished it! See you so...",
        "link": "/#",
    },
    {
        "avatar": user3,
        "name": "Stillnotdavid",
        "text": "This theme is awesome!",
        "link": "/#",
    },
    {
        "avatar": user4,
        "name": "Kurafire",
        "text": "Nice to meet you",
        "link": "/#",
    },
    {
        "avatar": user5,
        "name": "Shahedk",
        "text": "Hey! there I'm available...",
        "link": "/#",
    },
    {
        "avatar": user6,
        "name": "Adhamdannaway",
        "text": "This theme is awesome!",
        "link": "/#",
    },
    {
        "avatar": user3,
        "name": "Stillnotdavid",
        "text": "This theme is awesome!",
        "link": "/#",
    },
    {
        "avatar": user4,
        "name": "Kurafire",
        "text": "Nice to meet you",
        "link": "/#",
    },
]

todoListDict = [
    {
        "id": "1",
        "item": "Design One page theme",
        "done": False,
    },
    {
        "id": "2",
        "item": "Build a js based app",
        "done": True,
    },
    {
        "id": "3",
        "item": "Creating component page",
        "done": True,
    },
    {
        "id": "4",
        "item": "Testing??",
        "done": True,
    },
    {
        "id": "5",
        "item": "Hehe!! This looks cool!",
        "done": False,
    },
    {
        "id": "6",
        "item": "Create new version 3.0",
        "done": False,
    },
    {
        "id": "7",
        "item": "Build an angular app",
        "done": True,
    },
    {
        "id": "8",
        "item": "Vue Admin & Dashboard  ",
        "done": False,
    },
]

chatusers = [
    {"id": 1, "name": "Geneva", "avatar": user5,
        "gender": "Male", "currentUser": False, },
    {
        "id": 2,
        "name": "Dominic",
        "avatar": user1,
        "gender": "Female",
        "currentUser": True,
    },
]

chatDict = [
    {
        "id": 1,
        "userFrom": chatusers[0],
        "text": "Hello!",
        "time": "10:00",
    },
    {
        "id": 2,
        "userFrom": chatusers[1],
        "text": "Hi, How are you? What about our next meeting?",
        "time": "10:01",
    },
    {
        "id": 3,
        "userFrom": chatusers[0],
        "text": "Yeah everything is fine",
        "time": "10:01",
    },
    {
        "id": 4,
        "userFrom": chatusers[1],
        "text": "Wow that's great",
        "time": "10:02",
    },
    {
        "id": 5,
        "userFrom": chatusers[0],
        "text": "Yeah..!",
        "time": "10:02",
    },
]

projectStatus = {
    "WorkInProgress": {
        "name": "Work in Progress",
        "color": "info",
    },
    "Pending": {
        "name": "Pending",
        "color": "warning",
    },
    "Completed": {
        "name": "Completed",
        "color": "success",
    },
    "ComingSoon": {
        "name": "Coming Soon",
        "color": "dark",
    },
}

projectsDict = [
    {
        "ProjectName": "App design and development",
        "StartDate": "Jan 03, 2015",
        "DueDate": "Oct 12, 2018",
        "Team": [
            {"name": "Mat Helme", "avatar": user1},
            {"name": "Michael Zenaty", "avatar": user2},
            {"name": "James Anderson", "avatar": user3},
            {"name": "Username", "avatar": user5},
        ],
        "Status": projectStatus["WorkInProgress"],
        "Clients": "Halette Boivin",
    },
    {
        "ProjectName": "Coffee detail page - Main Page",
        "StartDate": "Sep 21, 2016",
        "DueDate": "May 05, 2018",
        "Team": [
            {"name": "James Anderson", "avatar": user3},
            {"name": "Mat Helme", "avatar": user4},
            {"name": "Username", "avatar": user5},
        ],
        "Status": projectStatus["Pending"],
        "Clients": "Durandana Jolicoeur",
    },
    {
        "ProjectName": "Poster illustation design",
        "StartDate": "Mar 08, 2018",
        "DueDate": "Sep 22, 2018",
        "Team": [
            {"name": "Michael Zenaty", "avatar": user2},
            {"name": "Mat Helme", "avatar": user6},
            {"name": "Username", "avatar": user7},
        ],
        "Status": projectStatus["Completed"],
        "Clients": "Lucas Sabourin",
    },
    {
        "ProjectName": "Drinking bottle graphics",
        "StartDate": "Oct 10, 2017",
        "DueDate": "May 07, 2018",
        "Team": [
            {"name": "Mat Helme", "avatar": user9},
            {"name": "Michael Zenaty", "avatar": user10},
            {"name": "James Anderson", "avatar": user1},
        ],
        "Status": projectStatus["WorkInProgress"],
        "Clients": "Donatien Brunelle",
    },
    {
        "ProjectName": "Landing page design - Home",
        "StartDate": "Coming Soon",
        "DueDate": "May 25, 2021",
        "Team": [
            {"name": "Michael Zenaty", "avatar": user5},
            {"name": "James Anderson", "avatar": user8},
            {"name": "Mat Helme", "avatar": user2},
            {"name": "Username", "avatar": user7},
        ],
        "Status": projectStatus["ComingSoon"],
        "Clients": "Karel Auberjo",
    },
]

lifetimeSalesStatDict = {
    "total_sales": "3,487",
    "open_campaign": "814",
    "daily_sales": "5,324",
}

dashboard4BarChartStatDict = {
    "total_sales": "1,284",
    "open_campaign": "7,841",
}

incomeAmountsStatDict = {
    "total_sales": "2,845",
    "open_campaign": "6,487",
    "daily_sales": "201",
}

showcaseUsersDict = [
  {
    "avatar": user3,
    "name": "Thelma Fridley",
    "role": "Admin User",
  },
  {
    "avatar": user4,
    "name": "Chandler Hervieux",
    "role": "Manager",
  },
  {
    "avatar": user5,
    "name": "Percy Demers",
    "role": "Director",
  },
  {
    "avatar": user6,
    "name": "Antoine Masson",
    "role": "Premium User",
    "isPremiumUser": True,
  },
]
