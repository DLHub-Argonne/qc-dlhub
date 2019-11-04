import click

from qc_dlhub import QcDlhubClient


@click.group()
def cli():
    """Client to make QC predictions with DLHub."""
    pass


@cli.command()
@click.argument("quantum-output", nargs=1, type=click.Path(exists=True))
@click.option("--output-file", "-o", default=None, type=click.Path(exists=False))
def autopredict(quantum_output, output_file):
    try:
        qc = QcDlhubClient()
        result = qc.autopredict(quantum_output)
        if result["success"]:
            print("Prediction:\n{}".format(result["prediction"]))
        else:
            print("Error during prediction: {}".format(result["error"]))
    except Exception as e:
        print("Error running prediction: {}".format(str(e)))
