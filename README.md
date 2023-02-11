# Dust Catcher

GET /

returns
```
{
    "temperature": float  # in Celcius
    "humidity": float  # relative humidity
    "fan_speed": int  # the duty cycle (between 0 and 100)
    "fan_rpm": int  # as key indicates
}
```

PUT /
takes
```
{
    "fan_speed": int  # bounded between 0 and 100
}
```

returns 200 OK



```
b'PUT / HTTP/1.1\r\n'
b'Content-Type: application/json\r\n'
b'User-Agent: PostmanRuntime/7.29.2\r\n'
b'Accept: */*\r\n'
b'Postman-Token: 9835a933-e187-4071-895b-b1e67eb9be42\r\n'
b'Host: 192.168.1.106\r\n'
b'Accept-Encoding: gzip, deflate, br\r\n'
b'Connection: keep-alive\r\n'
b'Content-Length: 24\r\n'
b'\r\n'
client connected from ('192.168.1.141', 40020)
b'PUT / HTTP/1.1\r\n'
b'Content-Type: application/json\r\n'
b'User-Agent: PostmanRuntime/7.29.2\r\n'
b'Accept: */*\r\n'
b'Postman-Token: 10ac789d-7514-4927-824f-4ede2dbbe982\r\n'
b'Host: 192.168.1.106\r\n'
b'Accept-Encoding: gzip, deflate, br\r\n'
b'Connection: keep-alive\r\n'
b'Content-Length: 24\r\n'
b'\r\n'
```