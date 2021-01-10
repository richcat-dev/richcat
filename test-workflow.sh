chmod 000 ./debug/permission.txt

if [ "$1" = "cov" ]; then
  mkdir ./coverage
  pytest --cov=./richcat --cov-report=xml ./tests
else
  pytest
fi

chmod 644 ./debug/permission.txt

