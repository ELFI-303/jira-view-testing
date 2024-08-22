#!/bin/bash

open -a Docker
xhost +localhost
open -a Safari http://localhost/
docker compose up --build