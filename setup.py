from setuptools import setup

setup(
    name="qc_dlhub",
    version="0.0.1",
    packages=["qc_dlhub"],
    description="Submission tool for QC predictions in DLHub",
    entry_points='''
    [console_scripts]
    qc-dlhub=qc_dlhub.main:cli
''',
    install_requires=[
        "dlhub_sdk>=0.8.3"
    ],
    python_requires=">3.4"
)
