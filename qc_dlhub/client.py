import os

from dlhub_sdk.client import DLHubClient

from qc_dlhub import CONFIG, utils


class QcDlhubClient():
    """The QcDlhubClient allows easier predictions using DLHub for QC data."""
    client_id = "33998f8c-8b1b-4d59-a5df-aa3a9e1c4680"
    app_name = "QcDlhubClient"

    def __init__(self):
        """Create a QcDlhubClient.
        """
        self.dlhub_client = DLHubClient()

    def autopredict(self, quantum_output):
        """Automatically run applicable DLHub models on input data.

        Arguments:
            quantum_output (str): The path to the QC output to use as model input.
        """
        quantum_output = os.path.abspath(os.path.expanduser(quantum_output))
        if not os.path.exists(quantum_output):
            raise FileNotFoundError("Path '{}' does not exist.".format(quantum_output))
        extracted_data = utils.qc_extract(quantum_output)
        model_info = utils.model_selector(extracted_data)
        sanitized_data = utils.qc_transform(model_info["transformer"], extracted_data)

        prediction = self.model_run(model_info, sanitized_data)

        return {
            "success": True,
            "prediction": prediction
        }

    def model_run(self, model_name, input_data):
        """Run a model on DLHub.

        Arguments:
            model_name (str): The name of the model to run.
            input_data (???): The input data for the model.
        """
        print("Mock model run")
        return "Prediction: Foo"
        return self.dlhub_client.run(model_name, input_data, input_type='json', asynchronous=False)
