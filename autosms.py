from twilio.rest import Client 
from datetime import datetime
from random import randint
import time 

#names
name_arr = ["name_1", "name_2", "name_3"] #add name here
# Message you wanna send 
msg_array = ["message_1", "message_2", "message_3"] #add all message here

#datetime function
def time_convert(time):
    return datetime.strptime(time, "%H:%M:%S")

# Morning time
m_t_start = "07:30:00"
m_t_end = "08:30:00"
mts = time_convert(m_t_start)
mte = time_convert(m_t_end)

# Afternoon 
a_t_start = "12:30:00"
a_t_end = "13:30:00"
ats = time_convert(a_t_start)
ate = time_convert(a_t_end)

# Night
n_t_start = "23:00:00"
n_t_end = "23:59:00"
nts = time_convert(n_t_start)
nte = time_convert(n_t_end)

# twilio authentication  
account_sid = "You'll get this from twilio" 
auth_token = "You'll get this from twilio" 
client = Client(account_sid, auth_token) 

def send_msg():
    # current time 
    now = time.localtime()
    t_n = time.strftime("%H:%M:%S", now)
    tn = time_convert(t_n)

    #random value generate
    n_i = randint(0,4) # calling name change
    msg_i = randint(0,5)  # msg change 

    # check logic based on time
    if mts <= tn <= mte:
        message_body = f"{name_arr[n_i]}, Remove this text and add your message here for morning {msg_array[msg_i]}।" 
    elif ats <= tn <= ate:
        message_body = f"Remove this and add your message {name_arr[n_i]} Remove this and add rest of your message {msg_array[msg_i]}।"
    elif nts <= tn <= nte:
        message_body = f"Remove this and add your message {name_arr[n_i]}, Remove this and add rest of your message {msg_array[msg_i]}।" 
    else:
        message_body = f"{msg_array[msg_i]}।" 


    message = client.messages.create( 
                              from_="You'll get this from twilio",  
                              body=message_body,      
                              to="You'll get this from twilio" 
                          ) 
    print(message.sid)