from StepperMotor import StepperMotor
import RPi.GPIO as GPIO
from time import sleep



class Tester():
	def __init__(self):
		self.stepperHandler = StepperMotor(0.001)


	def test_switches(self):
		print("---------------------------------------")
		print("---------------------------------------")
		print("------------ Switch tester ------------")
		print("---------------------------------------")
		print("---------------------------------------")
		
		print("\n")
	
		if not self.security_question("Do you want to continue with Switch tester?"):
			return 0
		
		print("Follow the instruction to test the stepper motors, check diagram to see the name of the switch")
		
		print("\n")
		
		
		# check Xmin and Xmax
		print("Press Xmin")
		while GPIO.input(self.stepperHandler.Xmin)==1:
			sleep(.1)
		
		print("Xmin pressed")
		
		print("\n")
		print("Press Xmax")
		while GPIO.input(self.stepperHandler.Xmax)==1:
		        sleep(.1)
		
		print("Xmax pressed")
		
		print("\n")
		
		
		# Check Yman and Ymax
		
		print("Press Ymin")
		while GPIO.input(self.stepperHandler.Ymin)==1:
		        sleep(.1)
		
		print("Ymin pressed")
		
		print("\n")
		print("Press Ymax")
		while GPIO.input(self.stepperHandler.Ymax)==1:
		        sleep(.1)
		
		print("Ymax pressed")
		
		print("\n")
		
		# Check Wmin and Wmax
		
		print("Press Wmin")
		while GPIO.input(self.stepperHandler.Wmin)==1:
		        sleep(.1)
		
		print("Wmin pressed")
		
		print("\n")
		print("Press Wmax")
		while GPIO.input(self.stepperHandler.Wmax)==1:
		        sleep(.1)
		
		print("Wmax pressed")

		print("\n")
		print("Test completed succesfully")
		
		return 1





	def security_question(self,question="Do you want to continue?"):
		cont = input(question+"[Y/n]: ")

		while cont not in ("n","N","Y","y"):
			sleep(.1)
			cont = input(question+"[Y/n]: ")

		if cont in ("n","N"):
			print("Aborting")
			return 0

		return 1


	def test_motors(self):
		print("---------------------------------------")
		print("---------------------------------------")
		print("------------ Motors tester ------------")
		print("---------------------------------------")
		print("---------------------------------------")
		
		print("\n")

		if not self.security_question("Do you want to continue with Motors tester?"):
			return 0


		print("\n")
		
		print("Before continuing with the Motors tester, check that all motors can move without hitting anything.")
		
		print("\n")
		

		
		if self.security_question("Is it safe to move W 100 steps clockwise?"):
			print("\n")
			print("Moving W motor clockwise...")
			self.stepperHandler.moveW(100,1)

		if self.security_question("Is it safe to move W 100 steps counter-clockwise?"):
			print("\n")
			print("Moving W motor counter-clockwise...")
			self.stepperHandler.moveW(100,0)


		if self.security_question("Is it safe to move Y 1000 steps up?"):
			print("\n")
			print("Moving Y motor up...")
			self.stepperHandler.moveY(1000,1)

		if self.security_question("Is it safe to move Y 1000 steps down?"):
			print("\n")
			print("Moving Y motor down...")
			self.stepperHandler.moveY(1000,0)


		if self.security_question("Is it safe to move X 3000 stepes toward the parking?"):
			print("\n")
			print("Moving X towards the parking...")
			self.stepperHandler.moveX(3000,0)

		if self.security_question("Is it safe to move X 3000 steps away from the parking?"):
			print("\n")
			print("Moving X away from the parking")
			self.stepperHandler.moveX(3000,1)


tester = Tester()

tester.test_switches()

tester.test_motors()
