echo off
cd %~dp0
git add .
git commit -m "fix"
git push -u origin main