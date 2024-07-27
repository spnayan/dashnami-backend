#!/bin/bash
# Build the project
echo $(whereis python3.9)
echo "Building the project..."
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear
