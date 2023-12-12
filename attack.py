import requests
import threading

url = ''                             #The target URL for sending POST requests.
data: The payload for the POST requests.

data = {                             #The payload for the POST requests.
    'cc_number': '434343434343',
    'cc_expmonth': '09',
    'cc_expyear': '21',
    'cc_cvv': '234',
    'cardholder_name': 'John Doe',
    'billing_address': {
        'street': '123 Main St',
        'city': 'Cityville',
        'state': 'CA',
        'zip_code': '12345',
        'country': 'USA',
    },
    'email': '@example.com',
    'phone': '555-555-5555',
    'transaction': {
        'amount': 100.00,
        'currency': 'USD',
        'description': 'Product Purchase',
        'order_id': 'ABC123',
        'timestamp': '2023-12-12T12:34:56',
    },
    'additional_info': {
        'customer_ip': '192.168.1.1',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    },
}
def do_request():

    while True:
        response = requests.post(url, data=data).text
        print(response)


threads = []  #Threads Starts

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon =True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
