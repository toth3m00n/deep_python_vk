target: run test coverage lint

venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt

run: venv/bin/activate
	./venv/Scripts/python custom_meta_class.py descriptor.py

lint:
	./venv/Scripts/pylint descriptors.py

test:
	./venv/Scripts/python -m unittest meta_and_descriptor_test.py

coverage:
	./venv/Scripts/python -m coverage run -m unittest meta_and_descriptor_test.py
	./venv/Scripts/python -m coverage report


clean:
	rm -rf __pycache__
	rm -rf venv