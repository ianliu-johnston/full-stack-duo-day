#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    signs = ["aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"]
    time = "today"
    if len(sys.argv) < 2:
        print("Usage: ./get_horoscope.py <sun sign> <{yesterday|today|tomorrow}>\n\tEx:./get_horoscope.py libra today")
        sys.exit(1)
    if sys.argv[1].lower() not in signs:
        print("Sign not found.")
        sys.exit(1)
    if len(sys.argv) >= 3:
        if sys.argv[2] in ["yesterday", "today", "tomorrow"]:
            time = sys.argv[2].strip()
        else:
            print("Please enter yesterday, today or tomorrow.")
            sys.exit(1)
    baseurl = "http://sandipbgt.com/theastrologer/api/horoscope/" + sys.argv[1] + "/" + time
    r = requests.get(baseurl)
    print("**~~..*-}}*--- {:s}{:s} ---*{{-*..~~**".format(sys.argv[1][0].upper(), sys.argv[1][1:]))
    print("**~~..*-}}*--- Your horoscope {:s} ---*{{-*..~~**".format(time))
    print(r.json().get('horoscope'))

