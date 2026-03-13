#importing dns library
import dns.resolver as DNS_Function
domain= input("Enter the domain name :")
#defining types of DNS record 
record_types = ["A", "AAAA", "MX", "CNAME", "TXT"]

for record_type in record_types:
    print(f"\n--- {record_type} Records ---")
    try:
        result = DNS_Function.resolve(domain, record_type)
        for record in result:
            print(print(f"  Value: {record}  |  TTL: {result.ttl} seconds"))
    except DNS_Function.NoAnswer:
        print(f"No {record_type} records found")
    except DNS_Function.NXDOMAIN:
        print("Domain does not exist")

    
