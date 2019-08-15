## data

* **external** _(data from third party sources interim)_:
    * `n+1` - (12/2016-03/2019)
    * `654_webhose-2016.tar.gz` - (2016) from [here](https://webhose.io/free-datasets/russian-news-articles/)
    * `ria.json.gz` - (01/2010-12/14) from [here](https://github.com/RossiyaSegodnya/ria_news_dataset)
* **interim** _(intermediate data that has been transformed)_:
    * `nplus1.csv.gz` - 6529 rows (12/2016-03/2019)
    * `webhose_2016.csv.gz` - 289813 rows (2016)
    * `news_lenta.csv.gz` - 699746 rows (09/1999-07/2018) from [here](https://toolbox.google.com/datasetsearch/search?query=News%20dataset%20from%20Lenta.Ru&docid=WZBj5lLTe7UR9JeoAAAAAA%3D%3D)
    * `ria.csv.gz` - 1003840 rows (01/2010-12/14)
    * only titles:
        - `yellow-only_title.csv` - 10761 rows
        - `news_lenta-only_title.csv.gz` - 699746 rows
        - `nplus1-only_title.csv.gz` - 6529 rows
        - `webhose_2016-only_title.csv.gz` - 289813 rows
        - `ria-only_title.csv.gz` - 1003840 rows
        - `concat_title_dirty.csv.gz` - concat dirty title above data (2010688 rows)
* **processed** _(the final, canonical data sets for modeling)_:
    * `...`
* **raw** _(the original, immutable data dump)_:
    * `...`