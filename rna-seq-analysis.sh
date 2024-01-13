#!/bin/bash

# This script contains commands that were used to process data for the project.
# Commands were executed separately.

fastqc -o /home/mb20879/BS312coursework /storage/projects/BS312/brain_1_1.fastq
fastqc -o /home/mb20879/BS312coursework /storage/projects/BS312/heart_1_1.fastq /storage/projects/BS312/heart_1_1.fastq

tophat -o brain_1_tophat hg38 /storage/projects/BS312/brain_1_1.fastq /storage/projects/BS312/brain_1_2.fastq
tophat -o heart_1_tophat hg38 /storage/projects/BS312/heart_1_1.fastq /storage/projects/BS312/heart_1_2.fastq
tophat -o heart_1v2_tophat hg38 /storage/projects/BS312/heart_1_1.fastq /storage/projects/BS312/heart_1_2.fastq
tophat -o heart_2_tophat hg38 /storage/projects/BS312/heart_2_1.fastq /storage/projects/BS312/heart_2_2.fastq

cufflinks /home/mb20879/BS312coursework/brain_1_tophat/accepted_hits_brain_1.bam
cufflinks -o cufflinks_brain_1 /home/mb20879/BS312coursework/brain_1_tophat/accepted_hits_brain_1.bam

cuffdiff -o brain_heart_cuffdiff /storage/projects/BS312/chr17_hg38.gtf /home/mb20879/BS312coursework/brain_1_tophat/accepted_hits_brain_1.bam,/home/mb20879/BS312coursework/brain_2_tophat/accepted_hits_brain_2.bam /home/mb20879/BS312coursework/heart_1v2_tophat/accepted_hits_heart_1v2.bam,/home/mb20879/BS312coursework/heart_2_tophat/accepted_hits_heart_2.bam