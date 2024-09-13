#!/bin/bash

# Function to check and list empty directories
check_empty_directories() {
  local dir="$1"
  local whitelist="$2"
  local empty_folders=()
  
  # Loop through all directories and subdirectories
  while IFS= read -r -d '' folder; do
    # Check if the folder is in the whitelist
    if [[ "$folder" == *"$whitelist"* ]]; then
      continue
    fi
    # Check if the folder is empty
    if [ -z "$(ls -A "$folder")" ]; then
      empty_folders+=("$folder")
    fi
  done < <(find "$dir" -type d -print0)

  # Print the summary of empty folders
  if [ ${#empty_folders[@]} -eq 0 ]; then
    echo "No empty folders found in $dir"
  else
    echo "Empty folders in $dir:"
    for folder in "${empty_folders[@]}"; do
      echo "$folder"
    done
  fi
}

# Check if correct number of arguments is provided
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 start_directory [whitelist_folder]"
  exit 1
fi

# Directory to start the search
start_directory="$1"

# Whitelist folder name
whitelist_folder=""
if [ "$#" -eq 2 ]; then
  whitelist_folder="$2"
fi

# Call the function with the start directory and whitelist folder
check_empty_directories "$start_directory" "$whitelist_folder"
