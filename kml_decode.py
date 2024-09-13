

city_name = "New York"
lat = 40.7128
long = -74.0060
decode=f"""  
  <Placemark>
    <name>{city_name}</name>
    <description>City</description>
    <Point>
      <coordinates>{lat},{long},0</coordinates>
    </Point>
  </Placemark>
  """
print(decode)