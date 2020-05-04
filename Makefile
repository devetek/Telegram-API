.PHONY: run-setup
run-dev: .validator
	@ cp main.ini development.ini

.PHONY: run-dev
run-dev: .prepare-env
	@ export ENV=development && python3 main.py

.PHONY: .prepare-env
.prepare-env: .validator
	@ pip3 install virtualenv
	@ python3 -m venv python_modules
	( \
		source python_modules/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
	)

.PHONY: .validator
.validator:
	$(eval WHICH_PY3 := $(shell which python3))
	$(eval WHICH_PIP3 := $(shell which pip3))
	$(eval WHICH_VENV := $(shell which virtualenv))

	@ test -n "$(WHICH_PY3)" || sh -c 'echo "No python3 binary, follow this link to install in mac https://github.com/pyenv/pyenv" && exit 1'
	@ test -n "$(WHICH_PIP3)" || sh -c 'echo "No compose pip3, follow this link to install in mac https://pip.pypa.io/en/stable/installing/" && exit 1' 
	@ test -n "$(WHICH_VENV)" || sh -c 'echo "No virtualenv binary, follow this link to install in mac https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3" && exit 1'
