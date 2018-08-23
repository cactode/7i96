import os, sys, subprocess
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def readCard(parent):

	if parent.ipAddressCB.currentText() == 'None':
		parent.outputLB.setText('An IP address must be selected')
		return
	ipAddress = parent.ipAddressCB.currentText()
	command = [parent.mesaflash, "--device", "7i96", "--addr", ipAddress, "--readhmid"]

	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.outputLB.setText(output.decode(sys.getfilesystemencoding()))
		return output.decode(sys.getfilesystemencoding())
	except subprocess.CalledProcessError as e:
		#print('exit code: {}'.format(e.returncode))
		#print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.outputLB.setText(e.output.decode(sys.getfilesystemencoding()))
		return e.output.decode(sys.getfilesystemencoding())

def flashCard(parent):
	if not parent.firmwareCB.currentData():
		parent.outputLB.setText('A firmware must be selected')
		return

	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return
	parent.statusbar.showMessage('Flashing the 7i96...')
	parent.outputLB.setText('')
	ipAddress = parent.ipAddressCB.currentText()
	firmware = os.path.join(parent.cwd, parent.firmwareCB.currentData())
	command = [parent.mesaflash, '--device', '7i96', '--addr', ipAddress, '--write', firmware]
	output = []

	with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
		for line in proc.stdout:
			output.append(line.decode())
	print('flash done')
	parent.outputLB.setText(''.join(output))
	parent.statusbar.clearMessage()

def reloadCard(parent):
	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return

	ipAddress = parent.ipAddressCB.currentText()
	command = [parent.mesaflash, '--device', '7i96', '--addr', ipAddress, '--reload']
	output = []

	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	process.communicate()[0]
	if process.returncode == 0:
		parent.outputLB.setText('Reload Sucessful')
	elif process.returncode == 255:
		parent.outputLB.setText('No 7i96 board found')
	else:
		parent.outputLB.setText('Reload returned an error code of {}'.format(process.returncode))

def cpuInfo(parent):
	output = []
	with subprocess.Popen('lscpu', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
		for line in proc.stdout:
			output.append(line.decode())
	parent.infoLB.setText(''.join(output))

def nicInfo(parent):
	# subprocess.check_output(('ps', '-A')) and then str.find on the output.
	ps = subprocess.Popen('lspci', stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', 'Ethernet'), stdin=ps.stdout)
	#print(type(output))
	parent.infoLB.setText(''.join(output.decode("utf-8")))

