#!/bin/bash
echo "*** daily: `date`"
source /home/biostar/www/production/live/biostar.env

set -ue

# remove old files
find /home/biostar/data/*.gz -type f -mtime +3 -exec rm {} \;

$PYTHON_EXE -m wwwportalmlekozyjestart.bin.sitemap
$PYTHON_EXE -m wwwportalmlekozyjestart.bin.planet --download
$PYTHON_EXE -m wwwportalmlekozyjestart.bin.patch --reduce_notes -n 6
