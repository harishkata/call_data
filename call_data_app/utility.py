import os
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

def parse_call_data():
    call_data = []
    with open(os.path.join(current_dir, 'test-call-data', 'CDR.txt'), 'r') as file:
        next(file) 
        for line in file:
            values = line.strip().split(':')
            call_data.append({
                "MSISDN": values[0],
                "DURATION": int(values[7])
            })
    return call_data

def parse_customer_data():
    customer_data = {}
    with open(os.path.join(current_dir,'test-call-data', 'customer.txt'), 'r') as file:
        next(file) 
        for line in file:
            values = line.strip().split(':')
            customer_data[values[2]] = {
                "Customer ID": int(values[0]),
                "Customer Name": values[1]
            }
    return customer_data

def match_calls_with_customers(call_data, customer_data,msdin):
    matched_calls = {}
    for call in call_data:
        customer_id = None
        if call["MSISDN"] in customer_data and msdin == call["MSISDN"]:
            customer_id = customer_data[call["MSISDN"]]["Customer ID"]
            customer_name = customer_data[call["MSISDN"]]["Customer Name"]
            duration = 0
            if call["MSISDN"] in matched_calls:
                duration = matched_calls[call["MSISDN"]]["Duration (minutes)"] + call["DURATION"]
            else:
                duration = call["DURATION"]
            matched_calls[call["MSISDN"]] = {
                "Customer ID": customer_id,
                "Customer Name": customer_name,
                "Duration (minutes)": duration
            }
    return matched_calls

def get_msdin(customer_data, params):

    if 'name' in params:
        msdin = ""
        for key, val in customer_data.items():
            if val['Customer Name'] == params['name']:
                msdin = key
                break
    elif 'msdin' in params:
        msdin = '+' + params['msdin'][1:]

    return msdin