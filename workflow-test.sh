#!/bin/bash
if [ "$1" = "-h" -o "$1" = "--help" ]; then
  echo "  Args list"
  echo "    --help : show help."
  echo "    <None> : normal pytest."
  echo "    cov    : pytest with code coverage."
  echo "    cov CI : codecov CI mode."
else
  chmod 000 ./debug/permission.txt
  if [ "$1" = "cov" ]; then
    if [ "$2" = "CI" ]; then
      mkdir ./coverage
      pytest --cov=./richcat --cov-report=xml ./tests
    else
      pytest --cov=./richcat ./tests
    fi
  else
    pytest
  fi
  chmod 644 ./debug/permission.txt
fi

