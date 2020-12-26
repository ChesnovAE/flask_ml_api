#!/bin/sh
gunicorn run:app -w 4 --threads 4