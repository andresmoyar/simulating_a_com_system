#############################################################
#															#
#       SIMULATING A COMUNICATION SYSTEM USING IMAGES		#
#	  Jeaustin Sirias Chacon (jeaustin.sirias@ucr.ac.c)     #
#                     Copyright (C) 2020					#
#															#
#############################################################
# VARIABLES
TEST = ./test/
SOURCE = ./source/

# COMMANDS
require: # Install requirements
	pip install pip --upgrade \
	&& pip install -r requirements.txt

run: # Run without installing 
	python3 -m test $(filter-out $@, $(MAKECMDGOALS))

install: # Install and run
	python3 setup.py install \
	&& runfile

unittest:
	
