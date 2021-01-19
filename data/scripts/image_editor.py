#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Imagem
======

Módulo referente a carregamento de informações da Imagem

'''

from os import path
from PIL import Image, ImageEnhance
import cv2

# Classe responsável gerenciar Editor de Imagem
class image_editor():

	# Variáveis
	image = None
	image_format = None
	image_local = None
	image_name = None
	image_extension = None
	image_size = None
	image_mode = None

	def reset_image(self):
		self.image = None
		self.image_format = None
		self.image_local = None
		self.image_name = None
		self.image_extension = None
		self.image_size = None
		self.image_mode = None

	def upload_image(self, image):
		try:
			self.image = Image.open(image)
			self.image_format = self.image.format
			self.image_local = path.dirname(path.realpath(image)) # Armezenar local da Imagem
			self.image_name, self.image_extension = path.splitext(path.basename(image)) # Armazenar nome e extenção da imagem
			self.image_size = self.image.size
			self.image_mode = self.image.mode
			return True
		except:
			return False

# Instanciar a Classe na variável
ed = image_editor()