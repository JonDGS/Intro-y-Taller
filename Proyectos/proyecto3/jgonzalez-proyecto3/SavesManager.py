import json
import operator

with open("SaveFile.json", "r") as f:
	data = json.load(f)

def save(car1, car2):
	data['save'][1]['player1'] = [car1.x, car1.y, car1.angle, car1.rotcar, car1.total, car1.laps, car1.hits, car1.goal, car1.check]
	data['save'][2]['player2'] = [car2.x, car2.y, car2.angle, car2.rotcar, car2.total, car2.laps, car2.hits, car2.goal, car2.check]
	json.dump(data, open("SaveFile.json", "w"), indent=2)


def compare(data, changes):
	t = changes[0]
	x = changes[1]
	y = changes[2]
	z = changes[3]
	i = -1
	for leader in data['players']:
		i += 1
		if x > leader['total']:
			j = t
			a = x
			b = y
			c = z
			t = data['players'][i]['username']
			x = data['players'][i]['total']
			y = data['players'][i]['laps']
			z = data['players'][i]['hits']
			data['players'][i]['username'] = j
			data['players'][i]['total'] = a
			data['players'][i]['laps'] = b
			data['players'][i]['hits'] = c
		elif x == leader['total']:
			if y > leader['laps']:
				j = t
				a = x
				b = y
				c = z
				t = data['players'][i]['username']
				x = data['players'][i]['total']
				y = data['players'][i]['laps']
				z = data['players'][i]['hits']
				data['players'][i]['username'] = j
				data['players'][i]['total'] = a
				data['players'][i]['laps'] = b
				data['players'][i]['hits'] = c
			elif y == leader['laps']:
				if z > leader['hits']:
					j = t
					a = x
					b = y
					c = z
					t = data['players'][i]['username']
					x = data['players'][i]['total']
					y = data['players'][i]['laps']
					z = data['players'][i]['hits']
					data['players'][i]['username'] = j
					data['players'][i]['total'] = a
					data['players'][i]['laps'] = b
					data['players'][i]['hits'] = c
				elif z == leader['hits'] or z < leader['hits']:
					pass
			else:
				pass
		else:
			pass
	return data

		


def leaderboard(a, x, y, z):
	print(a)
	print(x)
	print(y)
	print(z)
	i = 0
	found = False
	changes = ['', 0, 0, 0]
	global data
	for leader in data['players']:
		print('Llego a iteraciones')
		if not found:
			if x > leader['total']:
				changes[0] = a
				changes[1] = x
				changes[2] = y
				changes[3] = z
				found = True
			elif x == leader['total']:
				if y > leader['laps']:
					changes[1] = a
					changes[1] = x
					changes[2] = y
					changes[3] = z
					found = True
				elif y == leader['laps']:
					if z > leader['hits']:
						changes[1] = a
						changes[1] = x
						changes[2] = y
						changes[3] = z
						found = True
					elif z == leader['hits'] or z < leader['hits']:
						pass
				else:
					pass
			else:
				pass
		else:
			print('Encontro un true')
			pass
	if found and changes[1] != 0:
		print('Llego aqui')
		data = compare(data, changes)
		json.dump(data, open("SaveFile.json", "w"), indent=2)
	else:
		pass



