#!/bin/sh

devpath=$1

# Find last partition
PART_NUM=$(parted $devpath -ms unit s p | tail -n 1 | cut -f 1 -d:)

# Extract the partition's start sector
PART_START=$(parted $devpath -ms unit s p | grep "^${PART_NUM}" | cut -f 2 -d:)

echo "Devpath: $devpath"
echo "PART_NUM: $PART_NUM"
echo "PART_START: $PART_START"
echo

# Remove the last partition
parted $devpath -ms rm 2

# Create a new partition with the old partition's start sector
# but using 100% of the available space as size.
parted $devpath -ms unit s mkpart primary $PART_START 100%

echo "Resizing ${devpath}p${PART_NUM}..."
resize2fs ${devpath}p${PART_NUM}

