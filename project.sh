#!/bin/bash
# script for local development and testing of the microservice along with all the dep.
# this script needs (docker - docker compose - azure func tools) on the system.
# for the function app to run the shell script must be runned within an environment that contains all the required dependencies. 
# $ANACONDA=path where anaconda is installed locally

# activate proper env
source $ANACONDA/etc/profile.d/conda.sh

# main
if  [ "$1" = "help" ]; then
    echo "help: display help"
    echo "test: run test cases"
    echo "start: start the project locally"
    echo "stop: stop the project locally"
    echo "install_dep: install project dependencies"
elif [ "$1" = "test" ]; then
    echo "Starting tests"
    pytest ./tests
elif [ "$1" = "start" ]; then
    echo "Starting project locally"
    # start the database and needed storage account
    docker-compose build
    gnome-terminal -- /bin/sh -c 'docker-compose up --force-recreate'
    # wait for resource creation
    sleep 10
    # apply database migrations
    yoyo apply --database postgresql://username:password@localhost:5432/ilamo ./database/migrations --batch
    # start the function app
    cd function_app/
    func host start
elif [ "$1" = "stop" ]; then
    echo "Stopping project locally"
    docker-compose down
elif [ "$1" = "install_dep" ]; then
    echo "Installing project dependencies locally"
    pip install -r function_app/requirements.txt
    pip install -r database/requirements.txt
    pip install -r tests/requirements.txt
    echo "Adding environment variables"
    conda env config vars set ENV="local"
else
    echo "Must provide an option [help - test - start - stop - install_dep]"
fi
      