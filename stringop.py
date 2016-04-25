

example1 = 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
example2 = 'Coordinates: {latitude}, {longitude}'.format(**coord)

print (example1)
print(example2)