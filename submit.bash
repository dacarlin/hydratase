#!/bin/bash

#$ -cwd 
#$ -S /bin/bash
#$ -e logs
#$ -o logs

export ROSETTA_DB3=/share/tmp-data-1/siegellab/Rosetta/main/database
export PATH=$PATH:/share/tmp-data-1/siegellab/Rosetta/main/source/bin

relax.linuxgccrelease -in:file:s hydratase.pdb -renumber_pdb 1 -ignore_unrecognized_res 1 -constrain_relax_to_start_coords 1 -out:suffix ${SGE_TASK_ID} 
