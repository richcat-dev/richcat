chmod 000 ./debug/permission.txt

if [ "$1" = "cov" ]; then
  mkdir ./coverage
  pytest --cov=./ --cov-report=xml
else
  pytest
fi

chmod 644 ./debug/permission.txt

