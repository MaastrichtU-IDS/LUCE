#!/bin/bash

# Script to easily deploy to a server with SSH

ssh ids2 'cd /data/deploy-ids-tests/LUCE ; git pull ; docker-compose -f docker-compose.prod.yml down ; docker-compose -f docker-compose.prod.yml build --no-cache ; docker-compose -f docker-compose.prod.yml up -d ;'