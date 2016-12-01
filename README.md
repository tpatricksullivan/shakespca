# shakespca
I wrote this project for a class on Linear Algebra as part of the [University of Chicago MSc Analytics](https://grahamschool.uchicago.edu/credit/master-science-analytics/index) program. I simply applied Principal Component Analysis to the problem of representing high-dimensionality text analysis. My primary interest was in the plays and sonnets of William Shakespeare. To test the approach, I added two non-Shakespeare texts to the data set, _Pride_ _and_ _Prejudice_ and _Leviathan_.

## Running the analysis
I recommend running the analysis by executing the Jupyter notebook at [shakespca.ipynb](shakespca.ipynb).

## Dependencies
The Jupyter notebook above uses two libraries. Docuscope is a dictionary of words grouped by "Language Action Types" (LATs). There are multiple versions. I used the open source one available on [GitHub][gh Docuscope]. [Ubiqu-Ity][Ubiqu] is an academic tool for parsing texts that is specially written to work with Docuscope. It creates a vector for each text with the frequency of words used in each category. The source code is available from [GitHub][gh Ubiqu] under the BSD License.

If you are running this code yourself, you will need to make sure tha tyou have the Ubiqu-Ity scripts and Docuscope libraries in the right places. You may need to change path names.

[Docuscope]:http://www.cmu.edu/dietrich/english/research/docuscope.html

[gh Docuscope]:https://github.com/docuscope/DocuScope-Dictionary-June-26-2012

[Ubiqu]:http://vep.cs.wisc.edu/ubiq/

[gh Ubiqu]:https://github.com/uwgraphics/Ubiqu-Ity
