#!/bin/sh
gunicorn run:app -w 2 --threads 4 --bind 0.0.0.0:5000 --timeout 300
