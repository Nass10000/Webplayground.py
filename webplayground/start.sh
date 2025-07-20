#!/bin/bash
echo "Iniciando configuración de base de datos..."
python manage.py migrate --noinput
echo "Migraciones completadas"
python manage.py collectstatic --noinput
echo "Archivos estáticos recopilados"
echo "Iniciando servidor..."
gunicorn webplayground.wsgi --log-file -
