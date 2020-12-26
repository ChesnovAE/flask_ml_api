#!/bin/sh
gunicorn run:app -w 4 --threads 4 --bind 0.0.0.0:5000
