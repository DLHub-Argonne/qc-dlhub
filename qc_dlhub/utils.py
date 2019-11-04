from qc_dlhub import CONFIG


def qc_extract(quantum_output):
    # TODO
    print("Mock extraction")
    return {
    }


def model_selector(data):
    # TODO
    print("Mock model selection")
    return CONFIG["MODEL_METADATA"]["test_model"]


def qc_transform(transformer, data):
    # TODO
    print("Mock run transformation")
    return transformer(data)
