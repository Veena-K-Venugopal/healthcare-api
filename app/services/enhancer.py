def enhance_prediction_output(output: dict) -> dict:
    output["enhanced"] = True
    output["explanation"] = ("This is a mock prediction used for development and testing purposes only.")

    return output