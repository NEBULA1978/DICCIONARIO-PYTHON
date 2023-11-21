#!/bin/bash

# Declare an associative array
declare -A my_dict

# Initialize the array with values
my_dict=([Juan]='{"edad": 30, "casado": true}')

# Print the array
echo "${my_dict[@]}"

# Declare arrays for names and ages
names=("Alex" "Anna" "Petter" "Angela")
ages=(22 33 43 51)

# Create an associative array using a loop
for ((i=0; i<${#names[@]}; i++)); do
  my_dict[${names[$i]}]=${ages[$i]}
done

# Print the array
echo "${my_dict[@]}"

# Create an associative array with random ages
for name in "${names[@]}"; do
  my_dict[$name]=$((RANDOM % 41 + 10))
done

# Print the array
echo "${my_dict[@]}"

# Another way to create an associative array
other_dict=( [a]=23 [b]=551 [c]=98 )

# Copy values from one array to another
for key in "${!other_dict[@]}"; do
  my_dict[$key]=${other_dict[$key]}
done

# Print the array
echo "${my_dict[@]}"

# Square the values in the array
for key in "${!other_dict[@]}"; do
  my_dict[$key]=$(( ${other_dict[$key]} ** 2 ))
done

# Print the array
echo "${my_dict[@]}"

# Remove the 'b' key from the array
unset my_dict[b]

# Print the array
echo "${my_dict[@]}"
