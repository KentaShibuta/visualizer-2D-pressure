#!/bin/sh
echo ファイルのパスを入力:
read input_file_name
output_file_name=`date +"%Y%m%d%H%M%S"`
f_name_node='_node'
f_name_nbool='_nbool'
f_name_velocity='_velocity'
f_name_pressure='_pressure'

awk '/# mesh_start/,/# mesh_end/' $input_file_name|awk '! /^#/'|awk 'BEGIN{OFS=","} {print $1, $2, $3}'>$output_file_name$f_name_node.csv

awk '/# nbool_start/,/# nbool_end/' $input_file_name|awk '! /^#/'|awk 'BEGIN{OFS=","} {print $1, $2, $3, $4, $5, $6, $7}'>$output_file_name$f_name_nbool.csv

awk '/# start_velocity/,/# end_velocity/' $input_file_name|awk '! /^#/'|awk 'BEGIN{OFS=","} {print $1, $2, $3}'>$output_file_name$f_name_velocity.csv

awk '/# start_pressure/,/# end_pressure/' $input_file_name|awk '! /^#/'|awk 'BEGIN{OFS=","} {print $1, $2}'>$output_file_name$f_name_pressure.csv
