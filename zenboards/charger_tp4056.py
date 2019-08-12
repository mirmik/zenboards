#!/usr/bin/env python3
import zencad

x = 25
y = 19.4
z = 1.3

hx = 9
hy = 7.5
hz = 3.7
hd = 2 

def charger_tp4056_model():
	model = zencad.box(x,y,z)
	model = model + zencad.box(hx,hy,hz).translate(x-hx+hd,y/2-hy/2,z)

	return model

class charger_tp4056_unit(zencad.assemble.unit):
	def __init__(self, socket=False, center=False):
		super().__init__()

		self.width = y
		self.length = x
		self.cheight = z + hz/2
		self.height = z + hz

		if socket:
			self.model = charger_tp4056_model()
			self.model = self.model.back(y/2).left(x).down(z + hz/2).rotateY(-zencad.deg(90)).rotateZ(-zencad.deg(90))
			self.iobj = self.add_shape(self.model)


if __name__ == "__main__":
	charger = charger_tp4056_unit(socket=True)

	zencad.disp(charger)
	zencad.show()