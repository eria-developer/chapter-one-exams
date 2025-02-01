# 16
full_name = input ("please input your name:")
accepted = full_name [0:5]
favourite_number = input ("your favorite number is ?:")
print ("favourite_number")
print ( f" so {full_name } and number {favourite_number} should be {accepted}{favourite_number}traac ")
    
# 17
ticket_price = 12

print (f"hello your most welcome to our service \n each ticket is $ {ticket_price} ")


customer = input ("what\'s your name :") 
print ("customer")
number = int (input (" how many would you want ?:") )
print ("number") 
total = ticket_price * number
print (f" that will cost you $ {total} . thanks for choosing our services") 


# 18
email_address= input("input your email_address")
user_name= email_address.partition("@")[0]
domain_name= email_address.partition('@')[-1]
'user_name','','domain_name' == email_address.partition("@")
print(email_address.partition("@"))
print(user_name)
print(domain_name)



# 19
sentence="python does not get any better"
words= sentence.split()
print(sentence.split())
hyphen_sentence="-".join(words)
print(f"hyphen_sentence: {hyphen_sentence}")
