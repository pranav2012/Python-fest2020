# Program to convert seconds to days, hours, minutes and seconds
# Coded By Rudransh Joshi     https://github.com/FireHead90544

def convertor(time):
    '''Program to convert seconds to days, hours, minutes and seconds'''
    time = int(time)
    
    days = time // 86400
    hours = int(time % 86400) // 3600
    minutes = int(time % 86400 - hours * 3600) // 60
    seconds = int(time % 86400 - hours * 3600) % 60
    
    if days == 0 and hours > 0:
        print(f"{hours}h, {minutes}m, {seconds}s")
    elif days == 0 and hours == 0 and minutes > 0:
        print(f"{minutes}m, {seconds}s")
    elif days == 0 and hours == 0 and minutes == 0 and seconds >= 0:
        print(f"{seconds}s")
    else:
        print(f"{days}d, {hours}h, {minutes}m, {seconds}s") 



   
    
while True:
    time = float(input("Enter Time In Seconds:\t"))
    convertor(time)
