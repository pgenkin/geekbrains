time = int(input("Enter time in seconds: "))

hours = time // 3600
hh = str(hours)

minutes = (time % 3600) // 60
mm = str(minutes)

seconds = (time % 3600) % 60
ss = str(seconds)

print('{}:{}:{}'.format(hh.zfill(2), mm.zfill(2), ss.zfill(2)))
