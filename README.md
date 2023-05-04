

**Step 1. Download the reference geonme hg38 and build index using STAR**

Download both the gtf adn fasta file of hg38 and run STAR index built mode. The code to run STAR is in "build_index.sh"

The fasta file is "/QRISdata/Q5755/hg38/hg38.fa" and the annotation file is "/QRISdata/Q5755/hg38/gencode.v43.annotation.gtf"

**Step 2. Map the single-end clean reads to hg38**

The codes for this step is in "run_mapping.sh"

The sample file is "QRISdata/Q5755/SHOR-0013/fastq_files/230201_NS500239_0527_AH7HGVBGXL_0_mask_short_adapter_reads/SAL_1_S7_R1_001.fastq.gz"

**Step 3. Summarize the results from STAR**

The codes for this step is in "sum.py". The output file from STAR is named "out_prefixReadsPerGene.out.tab"

**Step 4. Create the heatmap**

The codes for this step is in "heatmap.py". The codes uses the output from step 3 "sum_gene.csv" to creat the heatmap
