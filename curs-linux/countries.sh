#!/bin/sh

# count the number of countries in Countries.txt
wc Countries.txt | cut -d " " -f2

# first 3 countries
head -n 3 Countries.txt | cut -d "|" -f2

# last 3 countries
tail -n 3 Countries.txt | cut -d "|" -f2

# 10th country
head -n 10 Countries.txt | tail -n 1 | cut -d "|" -f2

# create folders SistemFisiere/ with subdirs Coduri and Names
mkdir -p SistemFisere/{Tari,Coduri}

# create Coduri.txt and Nume.txt
cat Countries.txt | cut -d "|" -f1 > SistemFisere/Coduri/Coduri.txt
cat Countries.txt | cut -d "|" -f2 > SistemFisere/Tari/Nume.txt

# create hard links for these files on Desktop
ln ~/projecteuler.net/curs-linux/SistemFisere/Coduri/Coduri.txt ~/Desktop
ln ~/projecteuler.net/curs-linux/SistemFisere/Tari/Nume.txt ~/Desktop

# copy some files to ~/img (I couldn't find any images)
find . -name "*txt" -size +1k -exec cp {} ~/img \;   