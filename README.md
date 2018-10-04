## Learning Flask.

### The Flask Request-Response Cycle.

    Browser ---------> routes.py
    routes.py ---------> Python Function
    Python Function ---------> /templates (Finds HTML)
    /templates ----------> /static (Find Images,js,css)
    /templates ----------> renders HTML
    routes.py -----------> Sends back the HTML to Browser.