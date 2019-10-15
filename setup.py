from setuptools import setup

setup(
    name='student-loan-simulator',
    version='0.0.1',
    packages=['student_loan_simulator'],
    install_requires=[
        'matplotlib>=3.1',
    ],
    entry_points={
        'console_scripts': [
            'student_loan_simulator = student_loan_simulator.__main__:main'
        ]
    },
)
