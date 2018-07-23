import sys, os
import ImageEnhance
paths = ['/home/samy/Bureau/script/script python/Imaging-1.1.7']

for path in paths:
	if not path  in paths:
		sys.path.append(path)

from PIL import Image
from PIL.ImageQt import ImageQt

class image_operation:
	"""
	this class treat with PIL to do some image operation needed on our systeme.
	"""
	def __init__(self, image_path = None, image_entity =None):
		
		# image_operation constructor class,
		# here we init our class variables which deal with PIL

		# path of current image it can be directly set from constructor
		self.cureent_image_path = image_path
		self.old_entity = None

		# entity object from PIL it can be directly set from constructor
		self.current_image_entity = image_entity
		self.current_image_entity_size = [0,0]

	def load_image(self,path):
		
		# we load image with pil module
		if os.path.exists(path):
			self.current_image_entity = None
			self.cureent_image_path = path
			self.current_image_entity = Image.open(path)
			self.current_image_entity_size = self.current_image_entity.size
			#self.current_image_entity = self.ubuntu_fix_qt(self.current_image_entity)
			print 'entity self.current_image_entity : %s' % self.current_image_entity 
		else :
			print "Error file %s doesn't exist" % path

	@staticmethod
	def ubuntu_fix_qt(img):
		"""
		function wich correct ubuntu bug, which lost image data when we use 
		Qt 
		return : cast ImageQt of
		"""
		return ImageQt(img)

	def contrast_image(self,value):
		print "dans Contrast image"
		if self.current_image_entity==None:
			img = Image.open(self.cureent_image_path)
		else:
			img = self.current_image_entity
		#print img
		amelioration = ImageEnhance.Contrast(img)
		img_2 = amelioration.enhance(value)
		#img_2.show()
		self.current_image_entity = img_2
		self.old_entity = img
		return img_2


	def brightness_image(self,value):
		print "dans brihtness image"
		if self.current_image_entity==None:
			img = Image.open(self.cureent_image_path)
		else :
			img = self.current_image_entity
		#print img
		amelioration = ImageEnhance.Brightness(img)
		img_2 = amelioration.enhance(value)
		#img_2.show()
		self.current_image_entity = img_2
		self.old_entity = img
		return img_2

	def sharpen_image(self,value):
		print "dans sharpen image"
		if self.current_image_entity==None:
			img = Image.open(self.cureent_image_path)
		else :
			img = self.current_image_entity
		#print img
		amelioration = ImageEnhance.Sharpness(img)
		img_2 = amelioration.enhance(value)
		#img_2.show()
		self.current_image_entity = img_2
		self.old_entity = img
		return img_2
