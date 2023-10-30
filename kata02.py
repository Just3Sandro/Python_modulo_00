from datetime import datetime

kata = (2019, 9, 25, 3, 30)
date = datetime(*kata).strftime("%Y-%m-%d %H:%M")

print(f"The date and time are : {date}")
