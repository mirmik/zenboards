#!/usr/bin/env python3
import zencad

class charger_tp4056(zencad.assemble.unit):
	x = 25
	y = 19.4
	z = 1.3

	hx = 9
	hy = 7.5
	hz = 3.7
	hd = 2 

	model = zencad.box(x,y,z)
	model = model + zencad.box(hx,hy,hz).translate(x-hx+hd,y/2-hy/2,z)

	def __init__(self):
		super().__init__()
		self.add_shape(self.model)



if __name__ == "__main__":
	charger = charger_tp4056()

	zencad.disp(charger)
	zencad.show()