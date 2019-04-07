import requests

grundfos_url = "http://192.168.0.100/api/resource"

resp = requests.get(grundfos_url)

print(resp.status_code)
print(resp.json())


#pump.h forskellen mellem inlet og outlet
# power watt den bruger
# q32 er flow m3 / h
# speed rounds pr minut
# t2_h antal timer den har kørt
# t_w temperatur i celcius
