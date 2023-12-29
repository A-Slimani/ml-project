npm --prefix ../frontend run build

cd ..

Get-ChildItem backend/static/ | Remove-Item -Force
Remove-Item -Recurse -Force backend/templates/*

Copy-Item frontend/dist/assets/* backend/static
# Copy-Item frontend/dist/*.png backend/static
Copy-Item frontend/dist/index.html backend/templates

cd ./scripts