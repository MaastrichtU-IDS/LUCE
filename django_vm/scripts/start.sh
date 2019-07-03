# Only for development use
# This script allows me to quickly continue after restarting the VM
# 

echo
echo "Change to /vagrant/src/ directory"
cd /vagrant/src

echo
echo "Activate conda environment"
conda activate try_django

echo
echo "Run Django server"
python manage.py runserver 0.0.0.0:8000 --noreload