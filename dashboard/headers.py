def get_product_list_headers():
    return [
        {
            "key": "number",
            "label": "Number",
            "link": "",
        },
        {
            "key" : "photo",
            "label" : "Photo",
            "link" : "",
        },
        {
            "key": "name",
            "label": "Product Name",
            "link": ["get_edit_link"],
        },
        {
            "key": "unit_price",
            "label": "Price (B$)",
            "link": "",
        },
        {
            "key": "description",
            "label": "Description",
            "link": "",
        },
        {
            "key": "status",
            "label": "Status",
            "link": "",
        },
        {
            "key": "links",
            "label": "",
            "link": [
                {"label" : "Edit", "action": "get_edit_link"},
            ],
        },
    ]

def get_branch_list_headers():
    return [
        {
            "key": "number",
            "label": "Number",
            "link": "",
        },
        {
            "key": "name",
            "label": "Branch Name",
            "link": ["get_edit_link"],
        },
        {
            "key": "phone_number",
            "label": "Phone Number",
            "link": "",
        },
        {
            "key": "address",
            "label": "Address",
            "link": "",
        },
        {
            "key": "links",
            "label": "",
            "link": [
                {"label" : "Edit", "action": "get_edit_link"},
                {"label" : "Opening Times", "action": "get_opening_hours_link"},
            ],
        },
    ]

def get_opening_hours_list_headers():
    return [
        {
            "key": "number",
            "label": "Number",
            "link": "",
        },
        {
            "key": "days",
            "label": "Days",
            "link": "",
        },
        {
            "key": "start_time",
            "label": "Start Time",
            "link": "",
        },
        {
            "key": "end_time",
            "label": "End Time",
            "link": "",
        },
        {
            "key": "break_start_time",
            "label": "Break Start Time",
            "link": "",
        },
        {
            "key": "break_end_time",
            "label": "Break End Time",
            "link": "",
        },
        {
            "key": "links",
            "label": "",
            "link": [
                {"label" : "Edit", "action": "get_edit_link"},
            ],
        },
    ]
