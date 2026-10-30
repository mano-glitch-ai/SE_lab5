# Issues

## Issue 1
Type: Medium / Security  
Line(s): 10  
Description: User-controlled `student and `scheme` values are inserted directly into the SQL query using string formatting. This can lead to SQL injection. Bandit reported B608.  
Fix Approach: Replace string interpolation with parameterized SQL using `?` placeholders and pass the values separately.

## Issue 2
Type: Medium / Code Quality  
Line(s): 9  
Description: The `audit=[]` mutable default argument is reused between function calls, which can cause data from previous calls to remain in the list. Pylint reported W0102.  
Fix Approach: Change the default value to `None` and create a new list inside the function when required.

## Issue 3
Type: Low / Security  
Line(s): 26  
Description: The program uses `os.system()` to execute a shell command. Bandit reported B605 and B607 because starting a shell is unnecessary for this operation.  
Fix Approach: Remove the shell command and directly perform the required operation in Python.

## Issue 4
Type: Low / Reliability  
Line(s): 27  
Description: The code catches the general `Exception` and uses `pass`, which silently hides any errors that occur. Pylint reported W0718 and Bandit reported B110.  
Fix Approach: Remove the unnecessary exception handling and allow meaningful errors to be handled explicitly.

## Issue 5
Type: Code Quality  
Line(s): 6, 16  
Description: The `disbursed_total` variable is maintained as global state and modified using the `global` statement. Pylint reported an invalid naming style and use of a global statement.  
Fix Approach: Remove the global variable and calculate the total from the database when required.

## Issue 6
Type: Code Quality  
Line(s): 15–21  
Description: The `disburse()` function returns an amount when an award exists but does not explicitly return a value when the award is not found. Pylint reported inconsistent return statements.  
Fix Approach: Return `0` when the requested award does not exist so that every execution path returns a value.

## Issue 7
Type: Code Quality  
Line(s): 31–32  
Description: The function name `bySchemeCount` does not follow Python's snake_case naming convention, and the comparison `scheme == None` is not the recommended way to check for `None`.  
Fix Approach: Rename the function to `by_scheme_count()` and change the comparison to `scheme is None`.

## Issue 8
Type: Code Quality  
Line(s): 1, 5, 9, 15, 24, 31, 37  
Description: The module and several functions do not have docstrings. Pylint reported missing module and function documentation. Several lines also exceed the configured line-length limit reported by Pylint and Flake8.  
Fix Approach: Add concise docstrings to the module and functions and split long statements across multiple lines.