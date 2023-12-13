#!/bin/bash

npm --prefix ../frontend run build

cd ..

# find backend/static/ -type f ! -name '*.json' -delete
rm -rf backend/templates/*

cp -r frontend/dist/assets/* backend/static
# cp frontend/dist/*.png backend/static
cp frontend/dist/index.html backend/templates

cd ./scripts