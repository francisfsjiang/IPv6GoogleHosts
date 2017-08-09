import dns.resolver
import dns.rdatatype

def main():
    i = open("origin_hosts")
    o = open("hosts", "w")
    for line in i.readlines():
        host = line.strip().split()
        if not host or host[0] == "#":
            o.write(line)
        else:
            try:
                answer = list(dns.resolver.query(host[1], rdtype=dns.rdatatype.AAAA))[0]
                last_answer = answer
            except Exception as e:
                print(e)
                if host[1].endswith("googlevideo.com") or host[1].endswith("gvt1.com"):
                    answer = last_answer
                else:
                    answer = host[0]
            o.write("%-30s %s\n" % (answer, host[1]))
    o.close()
    i.close()


if __name__ == "__main__":
    main()
