#!/bin/bash

#Travis-CI script to make it easier to run all the unit-test 

PROJECT_ROOT=`pwd` 
echo "Currently in $PROJECT_ROOT"
cd $PROJECT_ROOT/tests
export PYTHONPATH=$PROJECT_ROOT/health_check:$PROJECT_ROOT/configure_slaves
python -m unittest test_check_network_connectivity
python -m unittest test_slave
python -m unittest test_generate_key_value_pair
