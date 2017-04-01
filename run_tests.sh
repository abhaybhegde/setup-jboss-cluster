#!/bin/bash

#Travis-CI script to make it easier to run all the unit-test 

PROJECT_ROOT=`pwd` 
echo "Currently in $PROJECT_ROOT"
cd $PROJECT_ROOT/tests
export PYTHONPATH=$PROJECT_ROOT/health_check:$PROJECT_ROOT/configure_slaves
#Run all unit tests and calculate the code coverage. 
#Consolidated code coverage will be present in $PROJECT_ROOT/tests/htmlcov
coverage run unit_test_suite.py
