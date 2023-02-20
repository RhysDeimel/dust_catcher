# Dust Catcher

GET /

returns
```
{
    "temperature": float  # in Celcius
    "humidity": float  # relative humidity
    "fan_speed": int  # the duty cycle (between 0 and 100)
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
