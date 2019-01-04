#!/bin/bash
ERR='\033[0;31m'
OK='\033[0;32m'
WARN='\033[0;33m'
OK_BLUE='\033[0;36m'
NC='\033[0m'


printf "Running setup...\n"


if [ ! -d src/out ]; then
	printf "Creating src/out...\n"
	mkdir src/out  
	printf "Successfully created src/out\n"
else
	printf "${WARN}src/out already exists${NC}\n"
fi

if [ ! -d src/data ]; then
	printf "Creating src/data...\n"
	mkdir src/data  
	printf "Successfully created src/data\n"
else
	printf "${WARN}src/data already exists${NC}\n"
fi

reportlab=$(python3 -m pip --disable-pip-version-check freeze | grep reportlab)

if [ -z "$reportlab" ]; then
	printf "Installing required python libraries\n"
	python3 -m pip --disable-pip-version-check install -r requirements.txt
else
	printf "Libraries already installed\n"
fi

echo ${reportlab}

printf "${OK}Setup complete\n"

exit 0

