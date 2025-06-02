#! /bin/bash

echo "Enter a number: "
read number
if (( number % 2 != 0 )); then
    echo "It's an Odd Number"
else
    echo "It's an Even Number"
fi