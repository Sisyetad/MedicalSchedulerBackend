#!/bin/sh

# Exit immediately on error
set -e

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL..."
while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
  sleep 1
done
echo "✅ PostgreSQL is ready."

# Run migrations
echo "🔄 Running migrations..."
python ./manage.py migrate

# Start the server
echo "🚀 Starting Django server..."
python ./manage.py runserver 0.0.0.0:8000

