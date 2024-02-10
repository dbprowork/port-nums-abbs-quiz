import random

num_dict = {20: "FTP",
            21: "FTP (Command)",
            22: "SSH",
            23: "Telnet",
            25: "SMTP", 
            53: "DNS",
            67: "DHCP (Server)",
            68: "DHCP (Client)",
            80: "HTTP",
            110: "POP3",
            137: "NetBIOS (Name)",
            138: "NetBIOS (Datagram)",
            139: "NetBIOS (Session)",
            143: "IMAP",
            161: "SNMP (Query)",
            162: "SNMP (Trap)",
            389: "LDAP",
            443: "HTTPS",
            445: "SMB/CFS",
            3389: "RDP"       
}

num_key_list = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 137, 138, 139, 143, 161, 162, 389, 443, 445, 3389]

abb_dict = {"FTP": "File Transfer Protocol",
            "SSH": "Secure Shell",
            "Telnet": "Telecommunication Network",
            "SMTP": "Simple Mail Transfer Protocol",
            "DNS": "Domain Name System",
            "DHCP": "Dynamic Host Configuration Protocol",
            "HTTP": "Hypertext Transfer Protocol",
            "POP3": "Post Office Protocol 3",
            "NetBIOS": "Network Basic Input/Output System",
            "IMAP": "Internet Message Access Protocol",
            "SNMP": "Simple Network Management Protocol",
            "LDAP": "Lightweight Directory Access Protocol",
            "HTTPS": "Hypertext Transfer Protocol Secure",
            "SMB/CFS": "Server Message Block/Common File System",
            "RDP": "Remote Desktop Protocol"
}

abb_key_list = ["FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "HTTP", "POP3", "NetBIOS", "IMAP", "SNMP", "LDAP", "HTTPS", "SMB/CFS", "RDP"]

def main():
    quiz_type = input("Would you like a quiz on (p)ort numbers or (a)bbreviations: ")

    if quiz_type == "p":
        score = 0
        for i in range(10):
            ind = random.randint(0, len(num_key_list) - 1)
            port = num_key_list[ind]
            print(port)
            answer = input("Answer: ").lower()
            if answer == num_dict[port].lower():
                print("Correct")
                score += 1
            else:
                print(f"The correct answer was {num_dict[port]}")
        print(f"You scored {score}/10")

    elif quiz_type == "a":
        score = 0
        for i in range(10):
            ind = random.randint(0, len(abb_key_list) - 1)
            abb = abb_key_list[ind]
            print(abb)
            answer = input("Answer: ").lower()
            if answer == abb_dict[abb].lower():
                print("Correct")
                score += 1
            else:
                print(f"The correct answer was {abb_dict[abb]}")
        print(f"You scored {score}/10")

if __name__ == "__main__":
    main()
