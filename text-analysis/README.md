# Project Structure and Setup

Analysis is a process, not a product, thus the entire analysis must be
reproducible such that the code base can decentralised and worked on
collaboratively.  

We work within an opinionated framework to reduce errors and
allow for more than one set of eyes on a project.  This takes slightly more time
at first, but gets quicker with experience, and is faster in terms of
maintaining code and finding bugs.

 - Never save your interactive R session
 - The original data must be (treated as) read only
 - Munge the data into a "tidy" format first, and work from this
   - The munging is redone everytime you open n R session
   - This should _only_ clean from say, horribly formatted excel to the very
   base data that you will start working with, and so should be fast
   - In this context, tidy means a table that can be stored in an R table
   - This includes `data.frames`, `data.tables` and `tibbles`

The folder structure is defined by the package `ProjectTemplate`. The
`.Rprofile` file loads the project when you load an R session. This

 - Recreates your datasets that you have a handle to in the R Session everytime
 - Loads anything you've saved in `cache` for later
   - Things in `cache` must still be reproducible, and by defintion, are not
   commited to github

The minimal `ProjectTemplate` folder structure (extras have comments) is

```
  - /
    - cache/
    - config/
    - data/
      - __classifiers/__  # Manually curated extra classifer sets stored here
    - munge/
    - src/
      - __classifiers/__  # To scrape and create automatic classifier set
      - __utils.R__
    - __script.R__  # Main run script, should recreate results
```

The bold folders are just a suggestion, there may be a better way to do it in
practice!

 - `src` should not contain data
 - `munge` should not contain data
 - `data` should not contain code

Most of the folders are self-explanatory. `data` and `munge` should depend on
eachother, and should result in a clean workspace containing only your tidy
tables (and cache) every time you load an R session.

`src` is where you create analyses. These are loaded into the global environment
such that `script.R` should be extremely brief (~40 lines). It may take some time
to run as text analysis tends to be fairly computationally heavy, however it
reduces errors in results.

After the text classification, `script.R` may use from functions in `src` to
explore, tabulate or visualise the resulting variables.

## Text Analysis Libraries

To have access to a simple text classification library which will suffice for
the majority of our text analytics projects, let one of the github admins know
such that we can add you to a the repo.  

For more complicated text analysis, investigate `tidytext` or `termco`.

### Automatic and Manual classifiers

You can merge the automatic and manual classifiers with a function in `src`.

```
# In utils.R

merge_classifers = function(l1, l2) {
  keys <- unique(c(names(l1), names(l2)))
  classifers = setNames(mapply(c, l1[keys], l2[keys]), keys)
  purrr::map(classifers, unique)
}
```

Then

```
# Make some data
l1 = list(a = c("cat", "dog", "rabbit"), b = c("frog", "horse"))
l2 = list(a = c("cat", "hamster"), c = c("gerbil"))

> l1
$a
[1] "cat"    "dog"    "rabbit"

$b
[1] "frog"  "horse"

> l2
$a
[1] "cat"     "hamster"

$c
[1] "gerbil"
```

Resulting in

```
> merge_classifers(l1, l2)
$a
[1] "cat"     "dog"     "rabbit"  "hamster"

$b
[1] "frog"  "horse"

$c
[1] "gerbil"
```
