#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# 1. Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 2. Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 3. Apply database migrations (Crucial for a new deployment)
echo "Applying database migrations..."
python manage.py migrate

echo "Build process complete!"