from pprint import pprint

def format_linter_error(error: dict) -> dict:
    # formats a single error
    return {
        "line": error["line_number"], 
        "column": error["column_number"], 
        "message": error["text"], 
        "name": error["code"], 
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # formats all errors for a particular file 
    # and adds the `path` key — path to the file,
    # and the `status` key — "failed" if there 
    # are errors, "passed" if there are no errors
    return {
        "errors": [format_linter_error(cur_err) for cur_err in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # formats all errors for all report files
    return [format_single_linter_file(key, value) for key, value in linter_report.items()]


error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": "    return f\"I like to filter, rounding, doubling, "
    "store and decorate numbers: {\", \".join(items)}!\"",
}
print("# format_linter_error----------")
pprint(format_linter_error(error=error), sort_dicts=False)
# The output will be:
"""
{
    "line": 18, 
    "column": 80, 
    "message": "line too long (99 > 79 characters)", 
    "name": "E501", 
    "source": "flake8"
}
"""


errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
         "text": "line too long (99 > 79 characters)",
        "physical_line": "    return f\"I like to filter, rounding, doubling, "
        "store and decorate numbers: {\", \".join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": "    return f\"I like to filter, rounding, doubling, "
        "store and decorate numbers: {\", \".join(items)}!\"",
    },
]
print("# format_single_linter_error----------")
pprint(format_single_linter_file(file_path="./source_code_2.py", errors=errors), sort_dicts=False)
# The output will be:
"""
{
    "errors": 
        [
            {
                "line": 18, 
                "column": 80, 
                "message": "line too long (99 > 79 characters)", 
                "name": "E501", 
                "source": "flake8"
            }, 
            {
                "line": 18, 
                "column": 100, 
                "message": "no newline at end of file", 
                "name": "W292", 
                "source": "flake8"
            }
        ], 
    "path": "./source_code_2.py", 
    "status": "failed"
}
"""


report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py":
        [
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": "    return f\"I like to filter, rounding, doubling, "
                "store and decorate numbers: {\", \".join(items)}!\"",
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line": "    return f\"I like to filter, rounding, doubling, "
                "store and decorate numbers: {\", \".join(items)}!\"",
            },
        ]
}
print("# format_linter_report----------")
pprint(format_linter_report(linter_report=report_file), sort_dicts=False)
# The output will be:
"""
[
    {
        "errors": [], 
        "path": "./test_source_code_2.py", 
        "status": "passed"
    }, 
    {
        "errors": 
            [
                {
                    "line": 18, 
                    "column": 80, 
                    "message": "line too long (99 > 79 characters)", 
                    "name": "E501", 
                    "source": "flake8"
                }, 
                {
                    "line": 18, 
                    "column": 100, 
                    "message": "no newline at end of file", 
                    "name": "W292", 
                    "source": "flake8"
                }
            ], 
        "path": "./source_code_2.py", 
        "status": "failed"
    }
]
"""