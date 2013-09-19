#!/bin/bash
echo "*** sixhours.sh: `date`"
source /home/biostar/www/production/live/biostar.env

set -ue

$PYTHON_EXE -m wwwportalmlekozyjestart.bin.planet --update 1
$PYTHON_EXE -m wwwportalmlekozyjestart.bin.patch --blog_cleanup
