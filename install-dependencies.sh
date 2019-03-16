#!/bin/bash

echo installing dependencies ..

for d in `cat requirements.txt`; do  sudo pip2 install  $d; done


echo Installation done !