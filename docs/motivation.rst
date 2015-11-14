Motivation
==========

The motivation of writing dyplot came to me when I plotted a 10-year price chart
on a stock by matplotlib. I cannot see the exact price as the points all became
too small to see. I can zoom in if I use svg, but it is diffcult to navigate.
There is no way of interacting with data and chart.
I searched and found dygraphs. It's easy to use, flexible and allows users to 
interact with the data. It can also handles large dataset.

Then I needed to convert some of my scripts to use dygraphs, and I could not find
any python library to do that. That's the start of dyplot.

dygraphs does support line chart, so I found c3.js. In additional to line chart, c3.js supports pie and bar. To handle large data sets, c3.js is not as good as dygraphs. 
