## R Coding Practices

 - Functions should be all lower case with underscores separating words
   - `my_function = function { ...`
 - Variable names should be broken with underscores and prefixed with a data type signifier
   - `str_a_long_name`
 - Constants should be in all caps
   - `A_CONSTANT`
 - Underscores are used as most OO languages reserve `.` for properties
 - Use `=` for assignment as opposed to `<-`, in contridiction to all other `R` standards.  It's fewer keystroks and there's only really a distinction for legacy reasons, and global assignment in function calls.  If writing a package to be released on `CRAN`, `devtools` offers a function to replace assignment `=`s with `<-` anyway.
 - When writing packages for release on `CRAN`, never use `library` calls. Explicitly use `::` instead
 - Use spaces between parameters
   - `my_function(a = "foo", b = "bar")`
 - Shiny server and UI functions should follow best practices found [here](http://shiny.rstudio.com/articles/modules.html)
   - Shiny server and UI functions should be in title case
     - `MyServerFunction`, coupled with `MyServerFunctionUI`
   - Modularised code should be stored in a library in seperate files with the filename as the name of the function
     - `MyServerFunction.R` contains `MyServerFunction = function(input, output, ...)`
 - Comments should be placed above code, or two spaces after inline code.  A single space should follow the hash before the comment
   - `x = "hi"  # example comment`

### Data Prefixes

  - `dt_` - data.tables
  - `df_` - data.frames
  - `str_` - vectorised strings
  - `<none>` - vectorised integers (Not sure about this... might be useful to have something)
  - `n_` - counts, should be vector of length `1`
  - `ptn_` - regex patterns

#### Queries

  - `get_` - `SELECT` queries
  - `q_` - all other queries
  - `qr_` - query requests
