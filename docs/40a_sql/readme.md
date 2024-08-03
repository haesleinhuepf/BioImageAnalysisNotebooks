# Querying databases

A common task in data science is to combine data sources to gain new insights. These tasks are typically done using relational databases, collections of tables. The [Structured Query Language](https://en.wikipedia.org/wiki/SQL) (SQL) is the tool of choice when it comes to querying databases. When working with Pandas dataframes in Python, we can use the [pandasql](https://github.com/yhat/pandasql/) library for using SQL with [pandas](https://pandas.pydata.org/), more precisely, it uses [SQLite](https://www.sqlite.org/).

See also
* [How to Use SQL in Pandas (Towards Data Science)](https://towardsdatascience.com/how-to-use-sql-in-pandas-62d8a0f6341)
* [Pandas - SQL comparison](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)

## Installation

We can install pandasql using mamba/conda

```
mamba install -c conda-forge pandasql
```
