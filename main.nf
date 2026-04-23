process PIPELINE {
    script:
    """
    python pipeline/run_pipeline.py
    """
}

workflow {
    PIPELINE()
}
