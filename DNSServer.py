import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '127.0.0.1'
real_name_server = '8.8.8.8'  # Use a valid public DNS server IP address

# Create a list of domain names to query - make sure to remove the trailing period
domainList = ['example.com', 'safebank.com', 'google.com', 'nyu.edu', 'legitsite.com']

# Define a function to query the local DNS server for the IP address of a given domain name
def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answers = resolver.query(domain, question_type)  # provide the domain and question_type

    ip_address = answers[0].to_text()
    return ip_address

# Define a function to query a public DNS server for the IP address of a given domain name
def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.query(domain, question_type)  # provide the domain and question_type

    ip_address = answers[0].to_text()
    return ip_address

# Define a function to compare the results from the local and public DNS servers for each domain name in the list
def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_ip_address = query_local_dns_server(domain_name, question_type)
        public_ip_address = query_dns_server(domain_name, question_type)
        if local_ip_address != public_ip_address:
            return False
    return True

# Define a function to print the results from querying both the local and public DNS servers for each domain name in the domainList
def local_external_DNS_output(question_type):
    print("Local DNS Server")
    for domain_name in domainList:
        ip_address = query_local_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")

    print("\nPublic DNS Server")

    for domain_name in domainList:
        ip_address = query_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")

def exfiltrate_info(domain, question_type):
    data = query_local_dns_server(domain, question_type)
    return data

if __name__ == '__main':
    # Set the type of DNS query to be performed
    question_type = 'A'

    # Call the function to print the results from querying both DNS servers
    local_external_DNS_output(question_type)

    # Call the function to compare the results from both DNS servers and print the result
    result = compare_dns_servers(domainList, question_type)
    if result:
        print("DNS servers match for all domains.")
    else:
        print("DNS servers do not match for at least one domain.")
