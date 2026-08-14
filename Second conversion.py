#program 10
# Second Conversion

y=int(input("Enter seconds:"))
hour=y//3600
x=y%3600
min=x/60
sec=x%60
print(f" Total {hour}, {min} minutes and {sec} seconds")
