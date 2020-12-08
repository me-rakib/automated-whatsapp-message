from apscheduler.schedulers.blocking import BlockingScheduler
from autosms import send_msg

sched = BlockingScheduler()

sched.add_job(send_msg, 'interval', minutes=55)  #change minutes as you like

sched.start()