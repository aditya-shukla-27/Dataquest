import numpy as NumPy


class Script:

	@staticmethod
	def main():
		vector = NumPy.array([5, 10, 15, 20])
		matrix = NumPy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
		print(str(vector))
		print(str(matrix))



Script.main()