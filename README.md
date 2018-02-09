THIS IS AN UNOFFICIAL LIBRARY
-----------------------------
# fcc_complaints
FCC Complaints is a library to wrap the FCC's Consumer Complaints Data.  The authors of this library have no affiliation with the FCC or the US government.

Individual informal consumer complaint data detailing complaints filed with the Consumer Help Center beginning October 31, 2014. This data represents information selected by the consumer. The FCC does not verify the facts alleged in these complaints.[1](https://opendata.fcc.gov/Consumer/CGB-Consumer-Complaints-Data/3xyp-aqkj)

This api and library aim to make it easier to look up complaints made against numbers to the FCC.

The number of requests you can make on the data is limited unless you sign up for an API token.

# Installation

```
pip install fcc_complaints
```

# Configuration
Setup a file in either `~/.fcc_complaints` or `/etc/default/fcc_complaints` with your FCC API settings.
Sign up at the FCC website for a token: https://opendata.fcc.gov/profile/app_tokens

The configuration file should look something like this:
```
[auth]
app_token = {{YOUR APP TOKEN}}
username = {{YOUR USERNAME}}
```

This is not required but allows you to not have to pass it in every time you initialize the api.  You can also provide the API tokens when you initialize the API.  If no tokens are provided you can still use the API but you will be limited in how many requests you can make by the FCC.


# Usage
