import requests

r = requests.get('https://www.gstatic.com/ipranges/goog.json')
f = open('/root/.pvpn-cli/split_allow_tunnel.txt', 'w')
for item in r.json().get('prefixes'):
  cidr = item.get('ipv4Prefix')
  if cidr:
    f.write(cidr + '\n')
f.close()
