# anbima_calendar Makefile
# Version: 0.1
# Language: Python
# Targets:
#	lint:      runs isort + black
#	test:      run project tests
#

PROJECT_PATH := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
CURRENT_PATH := $(shell pwd)

ifneq ($(PROJECT_PATH),$(CURRENT_PATH))
$(error 'You need to be inside the projects root directory')
endif


.PHONY: test isort black lint

test:
	@export PYTHONPATH=$(PROJECT_PATH) && \
		poetry run pytest -v -x -p no:warnings --cov-report html --cov=$(PROJECT_PATH)

isort:
	@echo 'Running isort...'
	@poetry run isort -rc $(PROJECT_PATH)/anbima_calendar

black:
	@echo 'Running black...'
	@poetry run black $(PROJECT_PATH)/anbima_calendar

lint: isort black
