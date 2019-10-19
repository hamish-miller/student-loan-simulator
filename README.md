# Student Loan Simulator

Simulates the effect of making additional monthly payments towards a Plan 2
student loan in the UK.

The intention is to provide information about the benefits/drawbacks of making
additional repayments towards the student loan, above the minimum repayment.

No guarantees are made about the correctness of the simulation - the results
output do not consitute financial advice.


## Installation

Clone the repo:
```
git clone https://github.com/hamish-miller/student-loan-simulator.git
```

From the root of the repo, run:
```
pip install .
```

## Usage

In the root of the repo, create the config file `settings.ini`.

Fill in the following values in the config:
```ini
[required]
salary = {int}
initial_balance = {int}
max_monthly_repayments = {int}
```

where `salary` is in (£/yr), `initial_balance` is in (£) and `max_monthly_repayments` is in (£).

`max_monthly_repayments` is only used to trim the produced graph to the specified value (to allow for "zooming" into the graph)

Then, simply run via:
```
python -m student_loan_simulator
```


## Output

Output is placed in the `results` directory provided with the repo.

| Output            | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `analysis.json `  | Key results parsed from the simulation.                 |
| `graph.png`       | Graphical output of the result of the simulation.       |
| `metadata.json`   | Additional metadata for simulation run.                 |
| `results.json`    | Raw output of the simulation.                           |
| `settings.ini`    | Copy of the config used to initiate the simulation.     |

*Note:* Subsequent simulation runs will overwrite existing files in `results`.


## License

[MIT License](LICENSE)
