#!/bin/sh
echo 'building executable'
zip main.zip __main__.py
cat hashbang.txt main.zip > hello
rm main.zip
chmod u+x hello
