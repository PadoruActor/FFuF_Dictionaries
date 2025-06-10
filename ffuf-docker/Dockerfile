FROM alpine:latest

RUN apk add --no-cache git go && \
    go install github.com/ffuf/ffuf@latest && \
    mv /root/go/bin/ffuf /usr/local/bin/ && \
    rm -rf /root/go && \
    apk del go git

WORKDIR /scans



RUN echo '#!/bin/sh\n\
echo "=== Running FFUF Scan 1 ==="\n\
echo "=== Getting common directrories ==="\n\
ffuf -u https://www.maria-ra.ru/FUZZ -w /wordlists/common.txt\n\
echo "\n=== Running FFUF Scan 2 ==="\n\
echo "\n=== Getting base subdomains ==="\n\
ffuf -u https://www.FUZZ.maria-ra.ru -w /wordlists/subdomains.txt \n\
echo "\n=== Running FFUF Scan 3 ==="\n\
echo "\n=== Running FFUF Scan 3 ==="\n\
ffuf -u https://www.maria-ra.ru?FUZZ1=FUZZ2 -w /wordlists/burp-parameter-names.txt:FUZZ1 -w wordlists/parameters.txt:FUZZ2' > run_ffuf.sh && \
    chmod +x run_ffuf.sh

COPY wordlists /wordlists
ENTRYPOINT ["./run_ffuf.sh"]