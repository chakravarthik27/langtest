datasets_info = {
    "BoolQ": {
        "split": ("test-tiny", "test", "dev-tiny", "dev", "combined"),
        "extension": ".jsonl",
    },
    "NQ-open": {
        "split": ("test-tiny", "test", "combined"),
        "extension": ".jsonl",
    },
    "XSum": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "TruthfulQA": {
        "split": ("test-tiny", "test", "combined"),
        "extension": ".jsonl",
    },
    "MMLU": {"split": ("test-tiny", "test", "clinical"), "extension": ".jsonl"},
    "OpenBookQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Quac": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Toxicity": {"split": ("test",), "extension": ".jsonl"},
    "NarrativeQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "HellaSwag": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Translation": {"split": ("test",), "extension": ".jsonl"},
    "BBQ": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Prompt-Injection-Attack": {"split": ("test",), "extension": ".jsonl"},
    "Clinical": {
        "split": (
            "Medical-files",
            "Gastroenterology-files",
            "Oromaxillofacial-files",
        ),
        "extension": ".jsonl",
    },
    "ASDiv": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Bigbench": {
        "Causal-judgment": {
            "split": ("test-tiny", "test"),
            "extension": ".jsonl",
        },
        "DisflQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
        "Abstract-narrative-understanding": {
            "split": ("test-tiny", "test"),
            "extension": ".jsonl",
        },
        "DisambiguationQA": {
            "split": ("test-tiny", "test"),
            "extension": ".jsonl",
        },
    },
    "LogiQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "Narrative-Wedging": {"split": ("test-tiny",), "extension": ".jsonl"},
    "Wino-test": {"split": ("test",), "extension": ".jsonl"},
    "Legal-Support": {"split": ("test",), "extension": ".jsonl"},
    "Factual-Summary-Pairs": {"split": ("test",), "extension": ".jsonl"},
    "MultiLexSum": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "wikiDataset": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "CommonsenseQA": {
        "split": (
            "test-tiny",
            "test",
            "validation-tiny",
            "validation",
            "sample-test-tiny",
        ),
        "extension": ".jsonl",
    },
    "SIQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "PIQA": {
        "split": (
            "test-tiny",
            "test",
            "validation-tiny",
            "validation",
            "sample-test-tiny",
        ),
        "extension": ".jsonl",
    },
    "Consumer-Contracts": {"split": ("test",), "extension": ".jsonl"},
    "Contracts": {"split": ("test",), "extension": ".jsonl"},
    "Privacy-Policy": {"split": ("test",), "extension": ".jsonl"},
    "Crows-Pairs": {"split": ("test",), "extension": ".csv"},
    "StereoSet": {"split": ("test",), "extension": ".jsonl"},
    "Fiqa": {"split": ("test",), "extension": ".jsonl"},
    "MedQA": {"split": ("test-tiny", "test"), "extension": ".jsonl"},
    "MedicationQA": {"split": ("test",), "extension": ".jsonl"},
    "LiveQA": {"split": ("test",), "extension": ".jsonl"},
    "healthsearchqa": {"split": ("test",), "extension": ".jsonl"},
    "PubMedQA": {
        "pqaa": {"split": ("test",), "extension": ".jsonl"},
        "pqal": {"split": ("test",), "extension": ".jsonl"},
    },
    "MedMCQA": {
        "MedMCQA-Test": {
            "split": (
                "Anaesthesia",
                "Anatomy",
                "Biochemistry",
                "Dental",
                "ENT",
                "Forensic_Medicine",
                "Gynaecology_Obstetrics",
                "Medicine",
                "Microbiology",
                "Ophthalmology",
                "Pathology",
                "Pediatrics",
                "Pharmacology",
                "Physiology",
                "Psychiatry",
                "Radiology",
                "Skin",
                "Social_Preventive_Medicine",
                "Surgery",
                "Unknown",
            ),
            "extension": ".jsonl",
        },
        "MedMCQA-Validation": {
            "split": (
                "Anaesthesia",
                "Anatomy",
                "Biochemistry",
                "Dental",
                "ENT",
                "Forensic_Medicine",
                "Gynaecology_Obstetrics",
                "Medicine",
                "Microbiology",
                "Ophthalmology",
                "Pathology",
                "Pediatrics",
                "Pharmacology",
                "Physiology",
                "Psychiatry",
                "Radiology",
                "Skin",
                "Social_Preventive_Medicine",
                "Surgery",
                "Unknown",
            ),
            "extension": ".jsonl",
        },
    },
    "BSS": {
        "split": ("test",),
        "extension": ".jsonl",
    },
    "DrugSwap": {
        "split": ("qa_generic_to_brand",),
        "extension": ".jsonl",
    },
}
