Note: Needs updating

# Data Exploration

This repository is to track and document exploratory analysis performed on various datasets found within APJNP. This is to provide a skeletal frame for any exploratory work to ensure it is reproducible, accessible, readable and documented. The usage documentation below is aimed towards `python` and `R` analyses.

The documentation is added to hopefully make things easier, i.e. you won't have to think about the structure of the analysis, rather just follow the skeletal structure laid out. Any improvements, changes or suggestions are welcomed.

## Exploration

Create a new folder for each analysis context, to hold all working documents and the analysis report. Data should go inside a `data` subdirectory. The top analysis directory shouldn't need any organisation. Data is found through a standard filepath, the generative script is available in the top analysis directory and the report is available as a generated `html`/`word`/`pdf` file for export, or for display on github as a `filename.md` file. An appropriate program such as `pandocs` or `knitr` will generate the `filename.md` file and figure for you. 

**The `README.md` in the top analysis directory should be reserved for an executive summary that all organisation members, regardless of programming ability, should be able to understand.**

The executive summary may contain 
 - Potential actions
 - Interesting insights
 - Key visuals 
 - Any other high level information.
The summary should not use abbreviations or acronyms without explanation, and should attempt to define common subject matter abbreviations.

## Data
Data should be held in a spreadsheet or database, **but the original file should not be edited**. 
 * If the data to be analysed is small, such as an excel file, re-run any feature extraction/mutation each time as the time penalty is negligible
 * For medium sized databases, save the mutated database as a copy and use control flows to run feature extraction as needed
 * *For bigger data, i.e. big data, I haven't thought of an appropriate method yet and would appreciate ideas*
 
Primarily, this helps keeps efforts reproducible. It also prohibits updates to a data source from disrupting workflow, as the new dataset can simply be dumped into the appropriate directory to continue the analysis.

Add databases to a `.gitignore` in the analysis directory. Excel files can be uploaded to `GitHub` (obviously size dependant).

### Data information
Place a `readme` in `project/data` containing the following information:
 - Where/who the file was originally sourced from
 - Date sourced
 - Who has done any analysis on it and for what purpose
 - Any link to the APJNP data catalogue

## Tags (Assumptions)

Several tags should be used inline with the code such that any tagged event can be batch extracted.  For example, assumptions made during any analysis should follow the format 

Language: | `<comment-character> @@ An example comment`
----------|---------------------------------------------
R | `# @@ This is an example comment`
python | `# @@ This is an example comment`

A full list of assumptions within any script, and their effective locations can then be found by running

`grep -Inr "@@" --exclude=\*.Rhistory`

from a terminal. In the top directory this outputs

```
akhil@akhil-pc data-exploration $ grep -Inr "@@" --exclude=\*.Rhistory
README.md:18:`<comment-character> @@ An example comment`
README.md:22:`# @@ This is an example comment`
README.md:26:`grep -Inr "@@" --exclude=\*.Rhistory`
```
In a exploratory folder we would see the assumptions made, and the line number from where they take effect.

### Other Tags
A list of the current inline code tags which may be useful are as follows

Tag      |  Usage
---------|-------
`@@`     | Assumptions
`TODO`   | Items to be handled immediately/ASAP
`IDEA`   | Thoughts from exploration, not to be immediately tested
`ACTION` | Action for either the analyst or business
`INT`    | Data integrity issue

Improvements welcome and necessary.

## Tests

Tests are useful, but not essential. For example, I tend to use them mostly when doing analyses from excel sheets, to check the format of the sheet hasn't changed with a new update. Tests can either go inline with the script, or in `tests` and `fixtures` subdirectories, depending on usage.

## Languages

Longer analyses should preferable be done in `R` or `python` such that the standard format for any exploratory work can be a markdown document, and for integrity of analysis. This will also help control the amount of analysis work that has to be redone, and will allow people to pick up analyses that others have done, such that they will have a better understanding of a dataset, without having to perform the analyses themselves. 

 * `R` analyses should used `rmarkdown` and `knitr`. The option `keep_md: true` will generate the markdown file
 * `python` analyses should use something similar to `iPython notebook` (If I'm wrong about the best way to do this, let me know)
  - `Jupyter` notebook is also available for R, but I prefer `knitr`
 * `Excel` analyses are to be decided upon with regards to a best practice
 
`*.md` files are readable on `GitHub` and figures are automatically embedded.

### R Markdown Options

A minimal options list for a `*.Rmd` file could be
```
---
title: "Title Here"
author: "Author"
date: "31 April 2000"
output:
  html_document:
    keep_md: true
---
```
 
## Git usage

To attempt to keep the branch structure manageable, checkout a new branch for a new analysis project and merge into the master periodically. Any new branches from a master project branch should be merged back into the project master branch first, then the `data-exploration` master branch. This is potentially unnecessary, but shouldn't add too much overhead and will keep projects decoupled.
