echo 'building project'
pip install -r requirements.txt
echo 'requirement'

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo 'migration complete'


