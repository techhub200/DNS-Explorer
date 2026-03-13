#importing dns library
import dns.resolver as DNS_Function
domain= input("Enter the domain name :")
#DNS_Function sends a query to the DNS Server 
result=DNS_Function.resolve(domain ,"A")

for record in result:
    print(record)
