'''
headers:
POST /cgi_bin/inet_pnstat_cgi_14350.cgi HTTP/1.1
Host: www.indianrail.gov.in
Connection: keep-alive
Content-Length: 89
Cache-Control: max-age=0
Origin: http://www.indianrail.gov.in
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://www.indianrail.gov.in/pnr_Enq.html
Accept-Encoding: gzip, deflate
Accept-Language: en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4
Cookie: _ga=GA1.3.1274124828.1489040410

Content:
lccp_pnrno1:1234567890
lccp_cap_value:24357
lccp_capinp_value:24357
submit:Please Wait...
'''
import requests;

HEADERS = '''
Host: www.indianrail.gov.in
Connection: keep-alive
Content-Length: 89
Cache-Control: max-age=0
Origin: http://www.indianrail.gov.in
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://www.indianrail.gov.in/pnr_Enq.html
Accept-Encoding: gzip, deflate
Accept-Language: en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4
Cookie: _ga=GA1.3.1274124828.1489040410
'''

CONTENT = '''
lccp_pnrno1:1234567890
lccp_cap_value:24357
lccp_capinp_value:24357
submit:Please Wait...
'''
class Scraper:

    def __init__(self):
        global HEADERS;
        self.headers = self.getHeaders(HEADERS);
        self.pnr = "1234567890";
        return;

    def getHeaders(self, headers=None):
        if headers == None:
            global HEADERS;
            headers = HEADERS;
        header_dict = dict();
        lines = headers.split("\n");
        lines.pop();
        lines.pop(0);
        for line in lines:
            split = line.split(": ");
            header = split[0];
            value = split[1];
            header_dict[header]=value;
        return(header_dict);
    
    def getContent(self, content=None):
        if content == None:
            global CONTENT;
            content = CONTENT;
        content_dict = dict();
        lines = content.split("\n");
        lines.pop();
        lines.pop(0);
        for line in lines:
            split = line.split(":");
            key = split[0];
            value = split[1];
            content_dict[key]=value;
        return(content_dict);

    def setPNR(self,pnr):
        self.pnr = str(pnr);
        return;

if __name__ == "__main__":
    sc = Scraper();
    print(sc.getHeaders());
    print(sc.getContent());
    sc.setPNR(1234567890);    